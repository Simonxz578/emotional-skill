# Evidence quality and dependence

An event ledger contains event ID, time, person IDs, source, observation, context, stage, baseline, cost, impacted dimension, alternative readings, dependence cluster, and revision conditions. Keep direct quotations local and minimise identifying details.

The optional heuristic is:

`w = directness × source_reliability × repetition_factor × behavioural_cost × context_relevance × baseline_specificity × recency_factor`

All factors are explicitly chosen in [0,1], where 1 is no discount. They are not measured parameters. A direct low-cost statement can still be decisive about a boundary: behavioural cost is a relevance-specific modifier, never an excuse to discount refusal or consent. Source reliability means access and transcription fidelity, not moral worth. Repetition means independent episodes, not repeated screenshots or paraphrases. Recency means relevance to this hypothesis: years-old evidence can remain relevant to slow development.

`logit(p_new) = logit(p_old) + w log(BF)`; strength in the helper is `|log(BF)|`, direction sets the sign. These are uncalibrated scores. Avoid zero/one priors. Examine multiple plausible priors and factor choices; if the conclusion changes, lower confidence. Correlated observations require a joint likelihood or a documented discount; multiplying them independently inflates certainty.

Often informative: explicit self-report (about the stated intention); repeated cross-context behaviour; choices with opportunity cost; stress/conflict reactions; repair followed by actual change; initiative persisting after environment change; accountability. None is inherently romantic.

Often weak for relationship classification: one emoji, one reply delay, generic politeness, a typology meme, one flirtatious phrase, or the observer's preferred story. Diagnosticity is contrast-specific: an apology can distinguish indifference from concern while failing to distinguish friendship from attraction.

Omissions need an opportunity model: did the person know, have access, and have a realistic chance to act? Unobserved actions are not automatically absent actions. Keep contradiction visible instead of explaining every inconsistency away. Confidence reflects quality, independence, context coverage, and alternatives, not a numerical threshold.
