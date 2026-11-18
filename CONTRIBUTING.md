# Maintaining Paper-Express / 维护说明

The repository root is the maintained skill source. `paper-skills` is its original local directory name; a Git checkout may be named `paper-express`. The installable ZIP always contains one `paper-express/` directory and one root `SKILL.md`. Users install with Codex, Claude Code, or their agent's file tools; Python below is for maintainers only.

仓库根目录保存维护源，五个模块各有 `SKILL.md`。构建时将子模块入口转换为 `GUIDE.md`，安装包只注册 `paper-express`。修改维护源后重新构建，不直接修改 ZIP 中的文件。

## Edit and validate / 修改与检查

1. Edit the relevant module and its referenced templates. Keep evidence, assumptions, provenance, and validation status accurate. Update both READMEs when changing user-facing behavior.
2. Add intended release resources to `packaging/release-files.txt`, one repository-relative file per line. Add intended Git files to `packaging/repository-files.txt`. These are reviewed allowlists; new files are not published automatically.
3. With Python 3.10+ and its standard library, run from the repository root:

   ```sh
   python packaging/test_release.py
   python packaging/check_repository.py
   ```

   The first command rebuilds the ZIP, checks deterministic output, validates links and hashes, and copies it into isolated example agent directories. Temporary output stays in ignored `.build/`. The second audits the publication inventory, source links, private paths, and obvious credential patterns, including ZIP/PPTX contents. Neither command installs a global skill.
4. For changes to figure or table code, install the dependencies in `paper-figures-tables/requirements.txt` and run `python paper-figures-tables/scripts/validate_package.py`. Regenerate affected example outputs and audit records; see the module's [running guide](paper-figures-tables/references/running.md).
5. For theory changes, follow the [Lean workflow](paper-theory/static/lean/workflow.md), run the locked project, and record the actual proof status. Packaging checks do not re-prove mathematical claims.
6. Update `packaging/VALIDATION.md` with the checks actually run. Review the Git diff and stage only inventory files. Commit the rebuilt `dist/paper-express-3.0.0.zip` and its `.sha256` together with the source changes.

清单只包含本项目资源；不要加入本地论文库、上游压缩包、运行时、凭据、临时文件或历史安装目录。新增资源时同步检查许可与来源。图表的 CSV、源码和资产保留原始字节，避免换行转换使审计散列失效。

## Versioning / 版本维护

`packaging/build_release.py` defines the distribution version. For a new version, update the ZIP name in documentation, maintenance checks, and the repository inventory together. `manifest.yaml` uses `version` for its routing schema, not the distribution version. Root and module validation records describe their recorded runs; a new Git commit does not silently refresh old scientific checks.

## Contributions / 提交修改

Use a focused branch and pull request for subsequent contributions. Explain the changed behavior and validation performed. Preserve [LICENSE](LICENSE), [NOTICE.md](NOTICE.md), and module-specific source notices. Do not include real confidential manuscript data in examples; use clearly labelled synthetic inputs.
