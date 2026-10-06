# Information diagnostics

For an exclusive/exhaustive hypothesis variable H with model-relative p:

- Entropy: `H(H) = -sum_h p(h) log p(h)`, with `0 log 0 = 0`.
- Conditional entropy: `H(H|E) = sum_e p(e) H(H|E=e)`; entropy of the posterior after one observed event is `H(H|E=e)`, not the full expectation.
- Surprisal: `I(e) = -log p(e)`; p=0 gives infinity. Rare is not necessarily informative about the question.
- Mutual information: `I(H;E) = sum_(h,e) p(h,e) log[p(h,e)/(p(h)p(e))] = H(H)-H(H|E)`. Requires a joint distribution; one anecdote cannot establish it.
- KL divergence: `D_KL(p_new || p_old) = sum_h p_new(h) log[p_new(h)/p_old(h)]`. It measures directional model revision, is not symmetric or a metric, and is infinite if new mass occupies an old zero. It does not establish truth.
- Expected information gain: `sum_e p(e) D_KL(p(H|e)||p(H))`, equal to MI under the specified model. This expectation is not the realized entropy difference of one event.

Surprisal is observation rarity; Bayesian surprise is posterior-to-prior divergence. A realized event can raise posterior entropy while producing positive KL. Lower entropy can reflect overconfidence. Scripts validate distributions rather than silently normalize arbitrary numbers; qualitative bands are arbitrary aids, not validated cutoffs.

For a fictional cue equally likely under friendship and romance, its likelihood ratio is 1 even if both assign it low probability. A repair may be likely under important friendship and romance, but unlikely under indifference. It is diagnostic for importance while remaining weak for relationship type.

Maximum entropy chooses a distribution maximizing H subject to known constraints and a specified state space/reference measure. With no constraints a finite categorical uniform distribution follows; adding justified constraints changes it. Here the anti-overfit analogy is: do not fill unknown romance/exclusivity with certainty merely because warmth/trust are supported. This is not a computed MaxEnt solution to real relationships.

Ask for naturally occurring discriminators (sustained initiative once workload changes, enacted plans, direct expression), not manipulative experimental interventions. Consent and autonomy outrank a desire to reduce uncertainty.
