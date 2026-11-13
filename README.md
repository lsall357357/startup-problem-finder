# BP Problem Finder

`startup-problem-finder` helps founders locate clarity gaps, business-model
breaks, fundraising-story gaps, pitch-deck blockers, and likely investor
questions in idea-stage through Series A projects.

## 中文简介

`startup-problem-finder`（BP 体检）面向种子期到 A 轮的创业者：把你的项目介绍、
BP / 商业计划书、融资材料交给 Agent，它帮你找出表达断点、商业模式漏洞、
融资故事不成立的地方、无证据的主张与自相矛盾之处，并整理出投资人最可能
追问的问题和下一步该优先补的功课。

适用场景：融资前 BP 诊断、路演准备、投资人见面预演、被问住之前先自查。
它只做创始人侧的问题定位，不做投 / 不投的判断，也不代写 BP。

用法与英文版相同：给出材料，说一句「帮我看看这个 BP，投资人会在哪里卡住」，
即可开始。回复语言跟随你提问的语言。

## What It Helps With

- reviews the project material already available
- identifies where the project, business model, or fundraising story stops
  connecting
- locates unsupported claims, contradictions, and missing evidence
- organizes likely investor questions and the next checks to prioritize
- uses current research when the host supports it, or provides search queries
  when it does not

The result is founder-side problem location, not an invest-or-pass decision or
finished pitch-deck, fundraising, answer, or meeting copy.

## Start

Provide a project description, pitch deck, one-pager, memo, or other readable
material, then say what you want reviewed:

```text
Review this startup and show me where investors may get stuck.
```

The agent reads the available material and asks one concise, project-specific
intake round. You can reply “start now” to continue from the material already
available. If a file cannot be read, paste the relevant text, provide a
screenshot, or summarize the core facts.

## Scope

The main scope is idea-stage through Series A, including pitch decks,
fundraising material, and founder-meeting preparation. Post-Series-A requests
receive limited support on material clarity, question organization, and public
information research.

The skill does not make investment decisions or provide valuation, legal, tax,
securities, transaction, or fundraising-success advice.

## Install

### Quick Install (skills CLI)

```bash
npx skills add lsall357357/startup-problem-finder
```

Works with Claude Code, Codex, and other agents supported by the skills CLI.
For manual control over the install location, use one of the methods below.

Keep `SKILL.md` and `references/` together in your agent's skill directory.

### Codex

```bash
git clone https://github.com/lsall357357/startup-problem-finder.git \
  ~/.codex/skills/startup-problem-finder
```

### Claude Code

```bash
git clone https://github.com/lsall357357/startup-problem-finder.git \
  ~/.claude/skills/startup-problem-finder
```

### OpenClaw

```bash
git clone https://github.com/lsall357357/startup-problem-finder.git \
  ~/.openclaw/skills/startup-problem-finder
```

For another agent, copy the folder to its configured skills directory and load
`SKILL.md` as the entrypoint.

### Manual Installation (ZIP)

Download the [current install package](https://github.com/lsall357357/startup-problem-finder/releases/latest/download/startup-problem-finder.zip),
extract it, and place the complete `startup-problem-finder/` folder in your
agent's skill directory. Keep `SKILL.md`, `references/`, and `agents/` together.

The ZIP is a ready-to-copy snapshot of the same skill files in the repository.
It is not an executable installer and does not update an existing installation
automatically. Use it when you prefer downloading files to cloning with Git.

### Update an Existing Installation

For a Git-based Codex installation:

```bash
git -C ~/.codex/skills/startup-problem-finder pull --ff-only
```

Use the corresponding installation path for another agent. If the checkout
contains local edits, preserve them before updating.

For a ZIP-based installation, download the current package again and replace
the previously installed skill folder after preserving any local edits. Do not
merge it into an old folder, which can leave obsolete files behind.

Keep only one edition of this skill in active skill directories. If replacing
an older `early-stage-startup-problem-finder` or
`startup-roast-check-vc-lens` installation, move that copy outside the active
skill directories before installing this edition. Historical copies can remain
in an ordinary project or archive directory.

Both methods install the English distribution; replies follow the user's
language. File reading and current-information research depend on the host
agent's capabilities.

## Security

See [SECURITY.md](SECURITY.md) for security, privacy, and reporting guidance.
