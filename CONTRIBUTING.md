# Contributing

Thank you for helping map the fusion ecosystem. This index improves with every pair of eyes.

## Two ways to contribute

1. **Easiest — open an issue.** Use the [*Add a resource*](../../issues/new/choose) template with the name, link, and a sentence on what it is. A maintainer does the rest.
2. **Direct — edit the data.** Every entry lives in [`data/entries.yml`](data/entries.yml); `README.md` is generated from it. Add your entry there and open a pull request. If you can, regenerate the README too:

   ```bash
   pip install pyyaml
   python scripts/build_readme.py
   ```

   If you can't, no problem — CI will tell us and a maintainer will regenerate on merge. **Please don't edit README.md by hand**; it gets overwritten by the generator.

## What belongs here

An entry qualifies if it is:

1. **Fusion-relevant** — used in, or directly useful for, fusion energy research or development (magnetic, inertial, or alternative concepts). General tools qualify when the fusion community demonstrably uses them — say how in the description.
2. **Publicly reachable** — a public repository, a registration page, or an official distribution point, on any platform (GitHub, GitLab, Bitbucket, Hugging Face, or a project's own site). Links only: this index never re-hosts anyone's code or data.
3. **Real** — released and usable (or historically significant), not an announcement or a paper without an artifact.

We mark access status honestly on software and data:

- 🟢 `status: open` — public source or data; clone and run
- 🟡 `status: registration` — free for research after registration or a signed agreement (add an `access:` line saying where to ask — it feeds the access table)
- 🔴 `status: restricted` — export-controlled or institution-only (included so people know the front door, with an `access:` line)

Learning and community entries carry no status mark — leave the field out.

## Entry format

```yaml
- name: CodeName
  url: https://github.com/org/codename   # the OFFICIAL home, not a mirror or a paper
  status: open
  lang: Python          # main language — omit for data/learning entries
  install: pip          # easiest path: pip | conda | julia | container | binary | source | service
  desc: One factual sentence — what it is and why it matters.
```

- Plain language; superlatives only when earned ("the standard", "widely used" only when true).
- Entries are sorted automatically (🟢 first, then 🟡, then 🔴, alphabetical within each) — just add yours anywhere in the right category.
- One addition or fix per pull request — easy to review, fast to merge.

Every pull request is reviewed by a maintainer before merge. By contributing you agree your contribution is licensed under CC BY 4.0.

## Conduct

Be kind, be constructive, assume good faith. Disagreements about categorization are fine; disrespect is not. Maintainers may close contributions that don't follow this.
