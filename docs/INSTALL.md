# Install and run

## Requirements

- An agent host that can read Agent Skills (`SKILL.md`) and local files.
- Web or connected research-source access for current verification.
- A presentation authoring and rendering tool for editable slide delivery. Codex's Presentations skill can provide this when available; it is not bundled here.
- Python 3.9+ only for the optional installer, brief builder and package validator. These scripts use the standard library. Viewing the PPTX/PDF requires no Python.

ResearchBoost itself is an instruction-and-template package. It does not call a paid API, install an agent, or automatically crawl research sites.

## Codex: project installation

Download/extract or clone the repository, then run from its root:

```sh
python3 scripts/install.py --project /path/to/research-project
```

This copies the entire self-contained skill to `.agents/skills/research-boost` under the chosen project. It refuses to overwrite an existing destination. Open that project in Codex and invoke `$research-boost`. Restart Codex if the skill is absent.

For a user-wide installation:

```sh
python3 scripts/install.py --user
```

This installs into `~/.agents/skills/research-boost`. To update, keep a backup of your installed copy, remove or move its folder yourself, then rerun the installer. There is intentionally no automatic replacement.

Manual installation: copy `skills/research-boost/` in its entirety into your host's supported skills directory. Keep `SKILL.md`, `references/`, `assets/`, `agents/` and `artifact-template.json` together. Another host may use a different directory or invocation syntax; use its documentation.

## Verify

```sh
python3 scripts/validate.py
```

Ask the agent to read the installed skill and resolve `artifact-template.json`. Try [the robotics demo brief](../examples/robotics-coordination/brief.json) or one of the [four prompts](../examples/prompts/).

Codex locations and discovery behavior were checked against [official documentation](https://learn.chatgpt.com/docs/build-skills) on 13 November 2026. Host tools and availability can differ by installation.
