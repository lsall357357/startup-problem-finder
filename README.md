# Startup Problem Finder

`startup-problem-finder` helps founders locate clarity gaps, business-model
breaks, fundraising-story gaps, pitch-deck blockers, and likely investor
questions in idea-stage through Series A projects.

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

## Security

See [SECURITY.md](SECURITY.md) for security, privacy, and reporting guidance.
