<p align="center">
  <img src="../../.branding/tabarc-icon.png" width="180" alt="TABARC-Code Icon">
</p>

# Playtester Persona Bank (v1)

This is a deliberately over-sized set of playtester personas. The point is range, not a fictional “average player”.
Work in progress. Add your own. Delete the ones that don’t match your tables.

## How to use it

Pick four to seven personas that match the game’s audience, plus at least one from **Accessibility and reading**. For each one, work through its `breaks_on` list and answer its `review_questions` against the rules. Report what that persona specifically breaks, with the phrase that broke it. A list of names isn’t a review.

When logging a real playtest, set `persona_id` on each player in the event log to the closest match. Over a few sessions that tells you which kinds of player your rules keep failing.

### Suggested sets

- **First rules draft:** P001, P014, P028, P041, P049, P015
- **Family or gateway game:** P001, P024, P025, P063, P054, P072
- **Heavy euro or engine builder:** P004, P005, P017, P061, P037, P058
- **Competitive or tournament:** P012, P019, P021, P047, P049, P067
- **Wargame:** P011, P027, P057, P060, P047, P048
- **Co-op or campaign:** P016, P023, P044, P053, P070
- **Social, negotiation or hidden role:** P008, P032, P055, P051, P059, P065
- **Pre-print rulebook pass:** P041, P062, P064, P067, P069, P035

## Fields

| Field | What it’s for |
|---|---|
| `likes`, `hates_or_struggles`, `table_behaviours`, `play_goals` | Who they are at the table. |
| `rules_tolerance` | How much rules overhead they’ll put up with (`low` / `medium` / `high`). |
| `conflict_style`, `analysis_style`, `attention_profile`, `feedback_style` | Fixed vocabularies; see `persona_bank_v1.schema.json` for the allowed values. |
| `likely_failure_modes` | What goes wrong when they play. |
| `red_flags_to_watch` | Design features that should worry you if this persona is in your audience. |
| `breaks_on` | Rule structures and wording this persona reliably breaks. The core of a persona pass. |
| `review_questions` | Questions to answer about the rules when simulating them. |
| `sample_quote` | What you’ll hear from them at the table. |
| `use_when` | Which games or review passes they’re worth including in. |

## Newcomers and casual players

Most real tables have at least one. Start here for anything teachable.

- **P001**: Never Played Anything (board gamer (complete novice), never played)
- **P002**: Basic Board Gamer (board gamer (casual), casual)
- **P003**: Party Game Regular (board gamer (party), casual)
- **P014**: Never Reads Rulebooks (board gamer (casual), casual)
- **P024**: Family Game Parent (board gamer (family), casual)
- **P025**: Child Player, Age 8–10 (board gamer (child), new)
- **P028**: Overconfident Newbie (board gamer (new to the hobby), new)
- **P038**: Lapsed Gamer, Returning (board gamer (returning after years away), casual)
- **P040**: Convention Demo Drop-In (board gamer (convention), casual)
- **P053**: Quiet Optimiser (board gamer (casual-to-regular), casual)
- **P054**: Conflict-Averse Peacemaker (board gamer (social), casual)
- **P058**: Tired After Work (board gamer (weeknight player), casual)
- **P063**: Luck-Loving Casual (board gamer (family / casual), casual)
- **P065**: Distracted Phone Checker (board gamer (casual), casual)
- **P070**: Late Arrival (board gamer (joins mid-game), casual)

## Accessibility and reading

Run these on every game. They catch production and wording problems nobody else will.

- **P015**: Accessibility Advocate (board gamer (UX-focused), regular)
- **P035**: Second-Language Reader (board gamer (English not first language), regular)
- **P042**: Component Confuser (board gamer (casual), regular)
- **P048**: Colour-Blind Player (board gamer (colour vision deficiency), regular)
- **P050**: Low-Vision Player (board gamer (low vision), regular)
- **P068**: Iconography Reader (board gamer (visual learner), regular)
- **P069**: Player-Aid Dependent (board gamer (reference-card user), casual)
- **P072**: Dyslexic Player (board gamer (dyslexia), regular)

## Hobby regulars and experts

Engine, euro, 4X, dice and thematic players: depth, pacing, variance and snowball checks.

- **P004**: Gateway Euro Convert (board gamer (euro), regular)
- **P005**: Heavy Euro Planner (board gamer (heavy euro), expert)
- **P007**: 18xx Learner With Teeth (board gamer (18xx-focused), regular)
- **P008**: 4X Diplomat (board gamer (4X-focused), regular)
- **P009**: 4X Spreadsheet Admiral (board gamer (4X-focused), expert)
- **P013**: Chess Club Mind (board gamer (abstract / chess-trained), expert)
- **P017**: Analysis Paralysis Maximalist (board gamer (heavy euro), expert)
- **P018**: Abstract Purist (board gamer (abstract / strategy), expert)
- **P020**: Speedrunner (board gamer (fast play), regular)
- **P022**: Deluxe Component Collector (board gamer (crowdfunding backer), regular)
- **P030**: Theme-First Immersion Player (board gamer (thematic), regular)
- **P033**: Turn-Timer Advocate (board gamer (casual-to-regular), regular)
- **P034**: Rulebook Skimmer (board gamer (experienced), expert)
- **P036**: TTRPG Convert (board gamer (roleplaying background), regular)
- **P037**: Deckbuilder Optimiser (board gamer (deckbuilder), expert)
- **P039**: Old Hand, Low Patience (board gamer (veteran), expert)
- **P043**: Dice Goblin (board gamer (dice-heavy / skirmish), regular)
- **P061**: Engine-Builder Snowballer (board gamer (engine builder), expert)

## Competitive and adversarial

They will find the exploit. Better they find it now.

- **P006**: 18xx Shark (board gamer (18xx-focused), expert)
- **P010**: Card Game Grinder (board gamer (card-driven / CCG-trained), expert)
- **P012**: Pro Tournament Wargamer (wargamer (competitive), expert)
- **P019**: Meta-Chaser (board gamer (competitive / card-driven), expert)
- **P021**: Salty Loser (board gamer (competitive), regular)
- **P026**: Competitive Teen (board gamer (casual / video-game trained), casual)
- **P032**: Negotiation Monster (board gamer (negotiation / political), expert)
- **P049**: Edge-Case Hunter (board gamer (rules lawyer), expert)
- **P051**: Chaos Gremlin (board gamer (party / chaotic), regular)
- **P055**: Hidden-Role Liar (board gamer (social deduction), regular)
- **P059**: Kingmaker By Accident (board gamer (multiplayer), regular)
- **P067**: Rules-as-Written Literalist (board gamer (literal reader), expert)

## Wargamers

Measurement, line of sight, scenario length and bot opponents.

- **P011**: Wargame Grognard (wargamer (historical), expert)
- **P027**: Club Night Historical Wargamer (wargamer (historical), regular)
- **P047**: Tournament Judge (wargamer (organised play), expert)
- **P057**: Miniatures Painter-Hobbyist (wargamer (skirmish / hobby), regular)
- **P060**: Solo Wargamer vs Bot (wargamer (solo), regular)
- **P066**: Wargame Umpire (wargamer (refereed / umpired), expert)

## Co-op, campaign and solo

State that has to survive between sessions, or with nobody to ask.

- **P016**: Co-op Quarterback (board gamer (co-op), regular)
- **P023**: Campaign Game Master (board gamer (campaign / legacy), regular)
- **P029**: Solo Rules Auditor (board gamer (solo), regular)
- **P044**: Legacy Completionist (board gamer (legacy), regular)

## Teachers, editors and process

The people who teach, edit, log and test the game. They break the rulebook, not the game.

- **P031**: Streamer Brain (board gamer (content creator), regular)
- **P041**: The Group's Teacher (board gamer (explainer), expert)
- **P045**: Scenario Designer (board gamer (modder / scenario designer), expert)
- **P046**: Spreadsheet Enjoyer (board gamer (stat tracker), expert)
- **P052**: Digital Implementation Player (board gamer (digital / online), regular)
- **P056**: Boardgame Café Staff (board gamer (café teacher), expert)
- **P062**: Grumpy Rules Editor (board gamer (professional editor), expert)
- **P064**: Forum Rules Checker (board gamer (online community), regular)
- **P071**: Print-and-Play Prototyper (board gamer (prototype tester), regular)
