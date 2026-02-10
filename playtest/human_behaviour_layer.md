## Human Behaviour Layer

This module tracks how real players actually behave, not how the rules claim they behave in the designer’s head.

A rulebook is a polite fiction: it assumes attention, goodwill, and perfect recall. A table does not. A table has snacks, ego, time pressure, and that one player who “gets it” after doing it wrong three times.

So the Human Behaviour Layer exists to answer a blunt question:

Where does the game break when humans touch it?

Not because people are stupid. Because people are people.

What this layer is for

Rules analysis catches contradictions on paper. Useful. Necessary.

But most rules failures aren’t formal contradictions. They’re behavioural. They happen in the gap between:

what the rule says

what a player thinks it says

what the table lets them get away with

The Human Behaviour Layer maps that gap. Then it gives you fixes you can actually ship.

Focus areas
1) Misreads and assumptions

Misreads aren’t random. They cluster around predictable patterns:

Ambiguous verbs (“may”, “can”, “must”, “instead”, “immediately”)

Timing haze (“after”, “when”, “during”, “at the start of”)

Hidden hierarchies (general rule vs exception vs “special case” buried in a sidebar)

Similar terms that aren’t synonyms but look like they want to be (“round” vs “turn”, “move” vs “advance”, “discard” vs “remove”)

Rule-by-component drift (card text contradicts the rulebook; the table follows the card because it’s in front of them)

Concrete example:
If your rules say “After moving, you may attack”, half the table will interpret that as “you can’t attack unless you moved”. Someone will then win or lose on that mistake, and it’ll feel unfair in a very specific way.

Log it. Not as “players confused”. As: what did they do, and what phrase made them do it?

2) Attention drift

Attention isn’t a moral quality. It’s a resource. And your rules spend it.

Drift tends to appear at:

Downtime spikes (long turns, long resolution chains, long “wait for your next go”)

Upkeep clusters (three trackers updated in four places, every round)

Rare exceptions (the rule you only need once per game, so nobody remembers it)

Hidden state (the board doesn’t show what matters; the truth lives in someone’s head)

Concrete example:
If a player must remember that two ongoing effects expire at different times—and neither is physically tracked—you’ve created a quiet failure point. Somebody will forget. Somebody else will “forget”.

Either way, the game state becomes a negotiated story rather than a system.

3) Emotional spikes

Emotions aren’t flavour. They’re telemetry.

In playtests, spikes usually come from:

Perceived unfairness (“I didn’t know that was possible”)

Sudden loss of agency (stun-locks, chained denial, forced skips)

Gotcha interactions (counterplay exists, but only if you already knew to expect it)

Swingy resolution at high stakes (one roll deciding the whole arc)

Public humiliation moments (social games are brutal when the spotlight turns)

Concrete example:
The “emotion spike” isn’t just someone being salty. It’s a signal that the game’s contract with the player was broken. They believed they were playing one kind of contest; the system revealed it was another.

Log what triggered it, and what the player thought they were entitled to.

4) Social pressure at the table

This is the part designers often pretend doesn’t exist. It exists anyway.

Social pressure shows up as:

Targeting bias (attack the loud player, spare the new one, punish the winner)

Coalitions and pile-ons (explicit or silent)

Kingmaking (intentional or accidental)

Quarterbacking (co-op control by the confident optimiser)

Norm enforcement (“we don’t play that way”, even if the rule says you can)

Concrete example:
A negotiation rule that technically allows any deal may, in practice, become: “You’re not allowed to be ruthless, because the table won’t forgive you.” That’s not a rules issue on paper. It’s still a design issue if your win condition depends on ruthless play.

The Human Behaviour Layer logs the actual incentives: who gets punished socially, not just mechanically.

How to use this layer during playtests
Step 1: Observe like a journalist, not a judge

Write down what happened. The literal action. The phrase someone pointed at. The moment everyone stopped smiling.

Step 2: Classify the event

Use one of the four buckets above. Don’t overthink it.

Step 3: Capture the “why”, lightly

A short hypothesis is enough:

“Players assumed ‘round’ meant ‘each player’s turn’.”

“Downtime caused skimming; card text became the rules.”

“That crit felt like theft because it reversed 20 minutes of setup.”

Step 4: Patch the artefact, not the player

Fix the sentence. Add a tracker. Move the reminder onto the component. Change the timing word.

If your solution is “players should pay more attention”, your solution is imaginary.

Output expectations for reviewers using this layer

When reporting, the reviewer should produce:

A misread map (common misreads + the exact wording that triggered them)

Attention breakpoints (where focus collapses, and what the table does next)

Emotion triggers (what caused spikes, and what belief was violated)

Social dynamics (coalitions, targeting norms, quarterbacking, kingmaking)

Concrete fixes (rewrite the clause, change the component, add an aid)