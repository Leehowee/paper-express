"""Collect reproducible Lean build/axiom evidence; semantic review is separate."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone


def without_comments_and_strings(text: str) -> str:
    """Mask nested Lean comments and strings, preserving line positions."""
    out = []
    i = 0
    depth = 0
    string = False
    while i < len(text):
        if depth:
            if text.startswith('/-', i):
                depth += 1; out.extend('  '); i += 2
            elif text.startswith('-/', i):
                depth -= 1; out.extend('  '); i += 2
            else:
                out.append('\n' if text[i] == '\n' else ' '); i += 1
        elif string:
            if text[i] == '\\' and i + 1 < len(text):
                out.extend('  '); i += 2
            else:
                if text[i] == '"': string = False
                out.append('\n' if text[i] == '\n' else ' '); i += 1
        elif text.startswith('--', i):
            end = text.find('\n', i)
            end = len(text) if end < 0 else end
            out.extend(' ' * (end - i)); i = end
        elif text.startswith('/-', i):
            depth = 1; out.extend('  '); i += 2
        elif text[i] == '"':
            string = True; out.append(' '); i += 1
        else:
            out.append(text[i]); i += 1
    return ''.join(out)


def project_files(project: Path):
    for folder, dirs, files in os.walk(project):
        dirs[:] = [d for d in dirs if d not in {'.lake', '.git', '__pycache__'}]
        for name in files:
            if name.endswith('.lean') or name in {'lean-toolchain', 'lakefile.toml', 'lake-manifest.json'}:
                yield Path(folder) / name


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('project', type=Path)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--lake', default='lake')
    parser.add_argument('--audit', default='Audit.lean')
    parser.add_argument('--timeout', type=int, default=600)
    args = parser.parse_args()
    project = args.project.resolve(strict=True)
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=True)
    lake = shutil.which(args.lake)
    audit = (project / args.audit).resolve()
    report = {
        'checked_at_utc': datetime.now(timezone.utc).isoformat(),
        'project': str(project), 'commands': [], 'source_hashes': {},
        'markers_requiring_review': [], 'axioms_by_theorem': {},
        'semantic_mapping': 'not_reviewed_by_script',
        'coverage': 'build and explicitly listed axiom-audit entries only',
        'build_status': 'not_run',
        'lean_status': 'source_unrun',
    }
    problems = []
    if not lake: problems.append('Lake executable not found')
    if not audit.is_relative_to(project) or not audit.is_file():
        problems.append('Audit file must exist inside the project')
    if not (project / 'lake-manifest.json').is_file():
        problems.append('Missing dependency lock lake-manifest.json')
    for file in sorted(project_files(project)):
        relative = file.relative_to(project).as_posix()
        report['source_hashes'][relative] = hashlib.sha256(file.read_bytes()).hexdigest()
        if file.suffix == '.lean':
            code = without_comments_and_strings(file.read_text(encoding='utf-8'))
            for match in re.finditer(r'\b(sorry|admit|axiom|unsafe|native_decide)\b|debug\.skipKernelTC', code):
                report['markers_requiring_review'].append({
                    'file': relative, 'line': code[:match.start()].count('\n') + 1,
                    'marker': match.group(),
                })
    entries = []
    if audit.is_file() and audit.is_relative_to(project):
        entries = re.findall(r'#print\s+axioms\s+([A-Za-z_][A-Za-z0-9_.]*)',
                             without_comments_and_strings(audit.read_text(encoding='utf-8')))
    if not entries: problems.append('No explicit #print axioms entries found')
    report['audit_entries'] = entries

    if not problems:
        commands = [
            ('lake-version', [lake, '--version']),
            ('lean-version', [lake, 'env', 'lean', '--version']),
            ('build', [lake, 'build']),
            ('axioms', [lake, 'env', 'lean', args.audit]),
        ]
        for label, command in commands:
            try:
                result = subprocess.run(command, cwd=project, capture_output=True,
                                        encoding='utf-8', errors='replace', timeout=args.timeout)
                log = result.stdout + result.stderr
                code = result.returncode
            except (OSError, subprocess.TimeoutExpired) as exc:
                log = str(exc); code = None
            log_path = output / f'{label}.log'
            log_path.write_text(log, encoding='utf-8')
            report['commands'].append({'label': label, 'argv': command, 'cwd': str(project),
                                       'exit_code': code, 'log': log_path.name})
            if label == 'build':
                report['build_status'] = 'passed' if code == 0 else 'failed'
            if code != 0:
                problems.append(f'{label} failed; inspect {log_path.name}')
                break
            if label == 'axioms':
                for name, deps in re.findall(r"'([^']+)' depends on axioms:\s*\[([^\]]*)\]", log, re.S):
                    report['axioms_by_theorem'][name] = [d.strip() for d in deps.split(',') if d.strip()]
                for name in re.findall(r"'([^']+)' does not depend on any axioms", log):
                    report['axioms_by_theorem'][name] = []

    standard = {'propext', 'Classical.choice', 'Quot.sound'}
    for name in entries:
        if name not in report['axioms_by_theorem']:
            problems.append(f'Missing successful axiom output for {name}')
        elif set(report['axioms_by_theorem'][name]) - standard:
            problems.append(f'Additional axiom dependencies for {name}')
    if report['markers_requiring_review']:
        problems.append('Source markers require review; no clean validation reported')
    report['problems'] = problems
    report['status'] = 'checked' if not problems else 'not_cleared'
    if report['build_status'] != 'not_run':
        report['lean_status'] = 'checked' if not problems else 'check_failed'
    report['proof_integrity_status'] = (
        'clear_for_audited_entries' if not problems else
        'requires_review' if report['markers_requiring_review'] or report['axioms_by_theorem'] else
        'not_audited'
    )
    (output / 'verification.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'status': report['status'], 'lean_status': report['lean_status'],
                      'build_status': report['build_status'], 'audit_entries': len(entries),
                      'problems': problems, 'report': str(output / 'verification.json')}, ensure_ascii=False, indent=2))
    return 1 if problems else 0


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    raise SystemExit(main())
