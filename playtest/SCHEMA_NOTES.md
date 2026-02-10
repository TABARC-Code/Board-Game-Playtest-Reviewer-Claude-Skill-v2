# Playtest Logging Schemas (WIP)

These schemas exist because “it felt weird” is not data.

If you want useful iteration, log what happened in a way you can compare across sessions.

## Files

- `playtest_event_log_v1.schema.json`  
  Event stream logging. Misreads, lookups, emotion spikes, social pressure, pacing issues. The messy stuff.

- `playtest_session_summary_v1.schema.json`  
  A post-session summary that turns the stream into actionable changes.

- `misread_catalog_v1.schema.json`  
  Optional, but handy. Over time you build a catalogue of repeated misreads and the phrases that caused them.

## Minimal workflow

1) During play: log events (even if it’s scrappy).
2) After play: write one summary.
3) Patch rules.
4) Next session: see if the same problems come back.

Repeated confusion is a design signal. Not a player defect.


## Persona bank

Use **playtest/personas/** to simulate how different brains will break your rules.
