# Formal generative scaffold

For person i at time t:

`P_i(t) = {theta_i, m_i(t), x_i(t), g_i(t), v_i, n_i(t), pi_i(t)}`

Theta is a relatively stable dispositional distribution and conditional signature, m a contextual mode, x current affect/cognition, g active goals, v values, n narrative self-model, and pi an action/communication policy. These symbols denote unobserved explanatory constructs, not estimated neural parameters.

`R_AB(t)` is a vector of distinct warmth, comfort, trust, admiration, specialness, attraction, romantic attraction/salience, vulnerability, dependency, reciprocity, exclusivity, commitment, opportunity cost, repair motivation, autonomy support, secure-base function, self-expansion, and future integration.

`O_t = {utterance, action, timing, omission, repair, initiative, opportunity_cost, context}`.
Context C_t includes workload, social availability, stage, conflict history, environment, and observation opportunity. The emission model is `p(O_t | P_A(t), P_B(t), R_AB(t), C_t)`. Infer `p(P_A(t), P_B(t), R_AB(t) | O_1:t, C_1:t)` while retaining uncertainty.

Let S_t collect both persons' changing states and R, M_t their modes, and A_t the actions whose consequences enter the next step. A conceptual switching state-space factorization is:

`p(S_0,M_0) product_t p(M_t|M_(t-1),C_t) p(S_t|S_(t-1),M_t,C_t,A_(t-1)) p(O_t|S_t,M_t,C_t)`.

This is a proposed representation. Markov sufficiency is an assumption: history must be represented in S/M or conditioning expanded. Joint transitions permit reciprocal effects; separate independent person transitions would erase coupling. Traits can drift at a slower rate; they need not be literally constant. No fitted HMM, dynamic Bayesian network, or variational inference is implemented.

For a binary proposition, `logit(p_t) = logit(p_(t-1)) + w_t log(BF_t)`, with `BF_t = p(E_t|H,C_t)/p(E_t|not-H,C_t)`. Weighted updates are tempered heuristics. Multiply independent factors only when justified; otherwise cluster dependent observations. For exclusive/exhaustive categorical models, normalize likelihood × prior across all models. Overlapping relationship dimensions are separate propositions; their scores must not be normalized as a categorical distribution.

Information diagnostics require distributions over identical support. All defaults use natural logarithms (nats); log base 2 yields bits. Temperature `p_T(h) proportional to p(h)^(1/T)`, T>0, is a sensitivity device: larger T flattens, smaller T concentrates. It is not emotional heat or validation. The expression `E(h) = -log p(h) + constant` reparameterizes positive probability masses in dimensionless units, not physical energy. Zero mass yields infinite E. Neither expression establishes thermodynamic causality.

Falsifiability means observable revision criteria for each substantive interpretation, with context and opportunity specified. Limitations include sparse selected data, non-identifiable latent variables, subjective likelihoods, and no calibration. Sensitivity analysis and unknowns are mandatory where assumptions decide the answer.
