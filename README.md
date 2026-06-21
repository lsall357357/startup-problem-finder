# Startup Problem Finder

`startup-problem-finder` is a cross-agent skill for finding clarity gaps,
business-model breaks, fundraising-story gaps, pitch-deck blockers, and likely
investor questions in idea-stage through Series A startups.

It is designed for founders preparing an early project or fundraising material.
An investor or adviser may also use it to structure questions before a founder
meeting. It does not issue invest-or-pass recommendations.

## What It Does

- reads the material already provided before asking questions
- asks one concise, project-specific intake round
- checks whether the project can be understood clearly
- locates business-model and fundraising-story breaks
- finds pitch-deck claims, gaps, contradictions, and attention blockers
- lists likely investor questions without supplying scripted answers
- organizes next checks and states judgment limits
- uses current web research when the host supports it, or provides search
  queries when it does not

The workflow finds problems and evidence gaps. It does not write a finished
pitch deck, fundraising narrative, investor answer, or meeting script.

## Requirements

- An agent that can load a directory containing `SKILL.md`.
- A file-reading tool if you want the agent to inspect PDF, PPT, DOCX, or local
  files. If the host cannot read a file, paste the key text or export it to a
  supported format.
- A search tool only when current market, fund, policy, or competitor facts are
  needed. The core diagnosis works without internet access.

## Install

Clone the repository into the appropriate skill directory.

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

For a project-only installation, clone or copy the folder to:

```text
.claude/skills/startup-problem-finder
```

### OpenClaw

```bash
git clone https://github.com/lsall357357/startup-problem-finder.git \
  ~/.openclaw/skills/startup-problem-finder
```

OpenClaw may also load the skill from a workspace `skills/` directory or an
extra directory configured by the user.

### Other Agents

Keep `SKILL.md` and `references/` together. Configure the agent to load
`SKILL.md` as the entrypoint and follow the resource map when a referenced
workflow is needed.

## Example Requests

- "I have a startup idea. Help me find what is unclear."
- "Read this pitch deck and show me where investors may get stuck."
- "Roast this project professionally."
- "Use a VC lens on the fundraising story."
- "What questions should I expect in a founder meeting?"
- "Does the business model connect to the use of funds?"
- "What does this skill do and what material should I provide?"

The first project response reads the available material, summarizes what was
available, and asks one optional intake round. The user may skip the questions
and request an immediate diagnosis based on current information.

## Scope

Primary scope:

- idea-stage projects
- prototype and MVP projects
- angel, seed, pre-Series A, and Series A preparation
- pitch decks, one-pagers, memos, and pasted fundraising material
- founder-meeting preparation and investor-question organization

Post-Series-A requests receive limited support on material clarity, question
organization, and public-information research. The skill is not designed for
growth-stage transaction strategy, M&A, debt structuring, or complex finance.

## Privacy

The skill package contains no external API integration, crawler, analytics, or
automatic upload code. It does not independently transmit project material.

The host agent may use cloud models, plugins, file processors, or search tools.
Its privacy policy and configuration determine where user data is processed.
Remove credentials, personal identifiers, customer lists, bank details,
unpublished contracts, and other unnecessary sensitive information before
sharing material with any agent.

## Limits

The skill does not provide legal, tax, accounting, securities, valuation,
investment, transaction, or fundraising-success advice. Calculations and
public research still require professional verification when they affect a
real decision.

See `SECURITY.md` for security and reporting information.
