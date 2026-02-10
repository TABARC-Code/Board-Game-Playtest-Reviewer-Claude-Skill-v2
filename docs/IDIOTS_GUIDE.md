# Idiot’s Guide (WIP)

Yes, it’s called that on purpose. If you’re already an expert, good for you. If not, this is the on-ramp.

This repo is **work in progress**. Expect missing sections. Expect contradictions. If you find one, log it, fix it, or at least swear at it in a useful way.

## The basic idea

This is a review system for tabletop rules. It behaves like a code reviewer:

- clarity problems are “bugs”
- edge cases are “unhandled exceptions”
- balance issues are “degenerate strategies”
- player confusion is “UX failure under load”

## How to use it in a real project

### 1) Feed it a ruleset (or a chunk)
Start with something concrete: turn structure, combat, scoring, whatever. Don’t dump a 90-page tome and expect miracles.

### 2) Run a pass: logic first, humans second
- First pass: does the rules machine make sense?
- Second pass: how will real people misread it when tired, hungry, and slightly competitive?

### 3) Log playtests like you mean it
Use the schemas in **playtest/schemas/**.

Don’t just write: “Game felt swingy.”
Log what happened:
- who misread what
- when attention drifted
- what caused the emotional spike
- what social pressure warped decisions

### 4) Patch the rules, then check blast radius
Fixing one clause often breaks three others. Track the dependency chain. Be boring about it. Boring is how systems survive.

## Persona bank (why it exists)

There is no “typical player”. There are a dozen typical players that contradict each other.

Use **playtest/personas/** to pressure-test:
- teachability for new players
- tolerance for fiddly exceptions
- appetite for conflict
- analysis paralysis risk
- social dynamics (kingmaking, table talk, ‘helpful’ sabotage)

Motto:

Write rules like they’ll be executed by people who didn’t write them. Because they will.
