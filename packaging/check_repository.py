"""Audit the explicit Git publication inventory using only the standard library."""
from __future__ import annotations

import argparse
import io
import json
from pathlib import Path, PurePosixPath
import re
import subprocess
from urllib.parse import unquote
import zipfile
import zlib

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"\[([^\]\n]*)\]\(([^)\n]+)\)")
PATTERNS = {
    "private-machine-path": re.compile(r"(?i)(?:[a-z]:[/\\]+(?:Users[/\\]|博士)|/(?:Users|home)/[\w.-]+/)"),
    "github-token": re.compile(r"\b(?:gh[pousr]_[A-Za-z0-9]{36,}|github_pat_[A-Za-z0-9_]{40,})\b"),
    "aws-access-key": re.compile(r"\b(?:AKIA|ASIA)[A-Z0-9]{16}\b"),
    "private-key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
}


def inventory(name):
    entries = [line.strip() for line in (ROOT / 'packaging' / name).read_text(encoding='utf-8').splitlines()
               if line.strip() and not line.startswith('#')]
    assert len(entries) == len({p.casefold() for p in entries}), 'Duplicate inventory paths'
    for name in entries:
        relative = PurePosixPath(name)
        assert not relative.is_absolute() and '..' not in relative.parts and '\\' not in name and ':' not in name, name
        path = ROOT / name
        assert path.is_file() and path.resolve().is_relative_to(ROOT), name
        assert not any(p.is_symlink() for p in [path, *path.parents] if p != ROOT), name
    return entries


def scan(name, data, depth=0):
    assert depth <= 4, 'Unexpected nested archive depth'
    findings = []
    texts = [data.decode('utf-8', errors='ignore')]
    # JSON encodes backslashes; scan decoded values as well as the original bytes.
    if name.endswith('.json'):
        try:
            texts.append(json.dumps(json.loads(texts[0]), ensure_ascii=False).replace('\\\\', '\\'))
        except (ValueError, TypeError):
            pass
    if name.endswith('.pdf'):
        for stream in re.findall(rb'stream\r?\n(.*?)\r?\nendstream', data, flags=re.S):
            try:
                texts.append(zlib.decompress(stream).decode('utf-8', errors='ignore'))
            except zlib.error:
                pass
    for rule, pattern in PATTERNS.items():
        if any(pattern.search(text) for text in [name, *texts]):
            findings.append({'file': name, 'rule': rule})
    if name.endswith(('.zip', '.pptx', '.xlsx', '.docx')):
        with zipfile.ZipFile(io.BytesIO(data)) as archive:
            assert archive.testzip() is None, name
            for item in archive.infolist():
                path = PurePosixPath(item.filename)
                assert not path.is_absolute() and '..' not in path.parts and '\\' not in item.filename, item.filename
                if not item.is_dir():
                    findings.extend(scan(name + '!' + item.filename, archive.read(item), depth + 1))
    return findings


def probe_scanner():
    private_path = ('C:' + '/Users/' + 'publication-probe/source.txt').encode()
    assert scan('probe.txt', private_path)
    token = ('ghp_' + 'x' * 36).encode()
    assert scan('probe.txt', token)
    for suffix, member in [('.zip', 'notes.txt'), ('.pptx', 'docProps/core.xml')]:
        stream = io.BytesIO()
        with zipfile.ZipFile(stream, 'w', zipfile.ZIP_DEFLATED) as archive:
            archive.writestr(member, private_path)
        assert scan('probe' + suffix, stream.getvalue())
    pdf = b'%PDF-1.4\nstream\n' + zlib.compress(private_path) + b'\nendstream\n'
    assert scan('probe.pdf', pdf)
    return ['text', 'token', 'ZIP', 'PPTX XML', 'compressed PDF stream']


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--staged', action='store_true', help='Also require the Git index to exactly match the reviewed inventory')
    args = parser.parse_args()
    entries = inventory('repository-files.txt')
    names = set(entries)
    assert set(inventory('release-files.txt')) <= names
    findings = []
    links = 0
    for name in entries:
        data = (ROOT / name).read_bytes()
        findings.extend(scan(name, data))
        if name.endswith('.md'):
            for match in LINK.finditer(data.decode('utf-8-sig')):
                target = match.group(2).strip('<>').split('#')[0]
                if not target or re.match(r'[a-zA-Z][a-zA-Z0-9+.-]*:', target):
                    continue
                path = (ROOT / name).parent / unquote(target)
                resolved = path.resolve()
                assert resolved.is_relative_to(ROOT), (name, target)
                relative = resolved.relative_to(ROOT).as_posix()
                assert relative in names or any(n.startswith(relative.rstrip('/') + '/') for n in names), (name, target)
                links += 1
    assert not findings, json.dumps(findings, ensure_ascii=False)
    if args.staged:
        result = subprocess.run(['git', 'ls-files', '-z'], cwd=ROOT, check=True, capture_output=True)
        tracked = set(result.stdout.decode('utf-8').rstrip('\0').split('\0'))
        assert tracked == names, {'extra': sorted(tracked - names), 'missing': sorted(names - tracked)}
        # Validate the exact index bytes too, not only their working-tree counterparts.
        different = subprocess.run(['git', 'diff', '--name-only', '-z'], cwd=ROOT, check=True, capture_output=True)
        assert not different.stdout, 'Tracked working files differ from the staged content'
    print(json.dumps({'status': 'passed', 'repository_files': len(entries), 'local_markdown_links': links,
                      'inventory_matches_index': args.staged, 'scanner_probes': probe_scanner(),
                      'findings': 0, 'scope': 'Pattern checks of reviewed files and archive contents; not an exhaustive security audit'},
                     ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
