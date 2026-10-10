# Board-Game-Playtest-Reviewer-Claude-Skill-v2
A modular skill and behaviour framework for reviewing tabletop rules and playtests with the mindset of a tired-but-precise systems engineer:

<p align="center">
  <img src=".branding/tabarc-icon.png" width="180" alt="TABARC-Code Icon">
</p>

# Board Game Playtest Reviewer (Claude Skill)

Built and maintained by **Tabarc-Code**

This repo is a **work in progress**. Bits will move. Labels will change. Some pages are blunt because they’re meant to be useful, not polite. It’s what it is.

## What it does

A modular skill and behaviour framework for reviewing tabletop rules and playtests with the mindset of a tired-but-precise systems engineer: It’s basically cranky but fair.

- Treat rules and rule writing like executable logic, so it looks for logic flaws
- Treat players like chaotic users
- Should treat ambiguity like a bug. 

It currently covers:

- Boardgames & wargame rules analysis
- Playtest behaviour modelling (human, messy, real-table focused)
- Negative feedback loop design for small-format games
- A UK-orientated educated-human writing model for docs, reports, and notes - In UK English
- A large playtester persona bank (because one “average player” is a myth. It’s based around player types and averages.)

## Where to start

- **docs/IDIOTS_GUIDE.md** for the practical on-ramp
- **claude_skill/SKILL.md** for the Claude-ready skill prompt + operating rules
- **playtest/schemas/** for logging formats
- **playtest/examples/** for filled-in logs, a session summary and a misread catalogue (copy these)
- **playtest/personas/** for the playtester persona bank
- **design/negative_feedback.md** if your game is small and swingy

## Using it with Claude

- **As a skill:** copy `claude_skill/` into your skills folder. `SKILL.md` has the frontmatter the loader needs. For the supporting docs to be readable, keep the whole repo alongside it.
- **As a prompt:** paste `claude_skill/SKILL.md` (minus the frontmatter) into your system prompt, then give it a chunk of rules.

## Checking your changes

If you edit the persona bank or add logs, run:

```sh
pip install jsonschema
python3 tools/validate.py
```

It checks that every JSON file parses and matches its schema, that persona IDs line up across the bank, README, examples and `SKILL.md`, and that every manifest path exists. The same check runs on every pull request.

## Licence

MIT. Use it. Fork it. Improve it. Just don’t do the weird thing where you claim you invented it.
