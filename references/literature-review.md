# A Unified Framework for Evidence-Weighted Inference of Persons, Language, and Relationships

## Abstract

Interpersonal interpretation requires inference about psychological states that are only partly observable, from communications selected by context, goals, and an observer's access. This conceptual review proposes Unified Relational Inference Dynamics (URID), an interpretable architecture connecting probabilistic comparison, information diagnostics, dynamic personality representation, pragmatic language inference, narrative development, and relationship processes. Its contribution is a mapping of responsibilities across existing ideas rather than the discovery of a common physical law. Bayesian reasoning disciplines comparison; information theory distinguishes uncertainty, rarity, and revision; coarse-graining provides a bounded multiscale analogy; psychological constructs give latent variables meaning; pragmatics connects goals to utterances; narrative identity represents slower self-model change. Implementation consists of transparent uncalibrated numerical helpers and an evidence-grounded analysis protocol. It is neither a clinical diagnostic model nor an empirically validated predictor. Sparse observations, missing baselines, selection bias, non-identifiability, and fluent retrospective storytelling constrain every interpretation. Prospective falsifiers, countermodels, privacy separation, respect for boundaries, and the ability to remain uncertain are therefore architectural requirements. Human-facing synthesis should compress evidence and mechanisms into understandable language without presenting subjective scores as measured probabilities.

### Scope and verification method

This is a focused conceptual review, not a systematic review or meta-analysis of the entire literature. The seed bibliography was checked against Crossref DOI records, with selected publisher, PubMed and PMC checks for scope and metadata conflicts. Additional sources address attachment variability, self-inclusion, dyadic coping, and criticism of free-energy explanations. Metadata were verified on 2026-10-06; a compact provenance record is in `literature-metadata.json`. Abstracts and accessible primary/review material inform construct descriptions; no inaccessible article is represented as fully read. No effect sizes are pooled or transferred to individual predictions. Conceptual proposals below are identified as URID design choices, not findings established by the cited studies.

## 1. The problem

Everyday interpersonal analysis often starts with a conspicuous event: a delayed response, an affectionate symbol, a vulnerable disclosure, or a paragraph about change. The observation is real, but its relation to an enduring motive is ambiguous. A response can express friendliness, manage conflict, preserve dignity, fulfil an obligation, or disclose attraction. Several functions may coexist. The observational unit and the explanatory unit are therefore different: the analyst sees an event while trying to explain a person or an evolving relationship.

URID defines the practical problem as maintaining a revisable idiographic account. Idiographic means that a specific person's history and baseline matter. It does not mean that enough anecdotes reveal a hidden essence. The same observed delay can have different implications under chronic workload, a stable low-frequency communication style, and a recent explicitly stated withdrawal. A model must therefore represent opportunities, context, and history alongside the action itself.

Common errors follow from ignoring this gap. Single-cue inference elevates one event into a trait. Narrative confirmation protects an existing interpretation by explaining away every contradiction. Generic dualities sound insightful because they fit almost anyone. A polished account may combine these failures while feeling persuasive. The problem is not solved by using more theory names: additional latent motives can increase explanatory flexibility without increasing discrimination.

The proposed remedy is an architecture that makes the unit of evidence, the target proposition, and the strongest alternative explicit. It requires a stated revision condition. “The connection matters” and “the connection is exclusive” are different propositions with different evidence requirements. When the supplied material supports only the former, leaving the latter unknown is a substantive result. Missing closure is often more faithful to the evidence than an emotionally satisfying ending.

## 2. Social understanding as inference under uncertainty

Ong, Zaki, and Goodman (2019) organise computational emotion inference around an intuitive causal theory connecting events, appraisals, emotions, and other mental states. FeldmanHall and Shenhav (2019) describe social uncertainty and processes of inference, learning, and action that can reduce it. These reviews motivate a distinction between what a person experiences and what an observer can infer about that experience. [Emotion inference review](https://doi.org/10.1111/tops.12371); [social uncertainty review](https://doi.org/10.1038/s41562-019-0590-x).

URID's design implication is a provenance-sensitive evidence ledger. A direct quotation provides evidence that a position was expressed. An observer's impression provides evidence about that observer's appraisal. A third-party account additionally depends on access, memory, and transmission. These can all be relevant without being interchangeable. Keeping their types separate prevents the analyst from treating the user's certainty as another person's confession.

Mental-state inference also has an inverse-problem character. Multiple combinations of goals and states can produce the same expression. A carefully worded apology might follow guilt, affection, duty, fear of reputational damage, or several motives together. Adding one hidden state to explain each detail can fit the record perfectly while making no useful predictions. A parsimonious countermodel is needed to test whether the elaborate explanation earns its complexity.

This framework is normative and analytical: it describes how the skill should discipline its reasoning. It does not imply people consciously calculate probabilities or that a language model has direct access to a speaker's beliefs. The analyst is another fallible participant in the interpretive process. Selection of evidence, emotional investment, and cultural expectations affect the observer's model. Explicit uncertainty helps expose these dependencies but cannot remove them merely by being named.

## 3. Shannon information theory

Shannon's framework defines information quantities relative to distributions and communication channels. For discrete H, entropy is `H(H)=-sum p(h) log p(h)`. Conditional entropy averages residual uncertainty across possible evidence values. Mutual information equals `H(H)-H(H|E)` and depends on a joint distribution. Individual-event surprisal is `-log p(e)`. Log base determines units: natural logarithms yield nats; base two yields bits. [Shannon, first instalment](https://doi.org/10.1002/j.1538-7305.1948.tb01338.x); [second instalment](https://doi.org/10.1002/j.1538-7305.1948.tb00917.x). Sayood (2018) reviews applications to cognition while highlighting the gap between mathematical information and subjective meanings. [Review](https://doi.org/10.3390/e20090706).

The URID application is a question about discrimination, not emotional intensity. Suppose an affectionate cue is equally likely in valued friendship and romantic interest. It can feel emotionally significant to the recipient while contributing little to that particular comparison. Conversely, a mundane choice to keep an agreed plan despite a competing demand can discriminate investment from indifference without being verbally affectionate.

The observational channel matters. A transcript can omit tone; a screenshot can omit preceding context; an observer can report only memorable interactions. “Noise” here includes uncertainty introduced by these transformations, not a claim that all missing information is random. It may be systematically selected. A model built on unusually emotional moments can misrepresent the ordinary baseline even when every supplied event is authentic.

URID consequently uses qualitative diagnosticity when no joint distribution is known. It cannot honestly calculate mutual information from a handful of anecdotes by assigning arbitrary numbers and then relabelling the output as a measured property. Numerical diagnostics may describe explicitly supplied model distributions, but they remain conditional on the analyst's assumptions. The human answer should identify which distinction the evidence helps resolve and which distinctions it leaves open.

## 4. Jaynes: inference under incomplete knowledge

Jaynes (1957a, 1957b) connects information-theoretic reasoning with statistical mechanics. The maximum-entropy principle selects a distribution with maximal entropy subject to specified constraints, on a specified state space or reference measure. It does not mean treating every imaginable proposition as equally likely. [Part I](https://doi.org/10.1103/PhysRev.106.620); [Part II](https://doi.org/10.1103/PhysRev.108.171).

URID adopts a bounded epistemic analogy: do not add certainty where observations impose no relevant constraint. If available evidence supports warmth, trust, and repair motivation, that does not automatically constrain exclusivity. Completing the relationship story by inventing romance introduces a commitment that the evidence has not earned. The converse error is also possible: a present friendship label does not logically make all future change impossible, though it remains a present boundary to respect.

This distinction separates uncertainty from indecision. A model can confidently describe observed responsiveness while remaining uncertain about romantic interest. Different coordinates need different confidence assessments. A blanket “unknown” would discard real information; a blanket “certain” would invent it. The architecture aims to preserve supported structure and leave unsupported structure incomplete.

A literal interpersonal MaxEnt computation would need a defined space of states, constraints, and a reference measure. This skill does not provide those. Calling the restraint rule “MaxEnt-inspired” is therefore more accurate than claiming that its ordinary prose solves a maximum-entropy optimization. Formal elegance should not conceal absent modelling choices. The conceptual borrowing is useful because it makes unsupported completion visible, not because a relationship has become a thermodynamic ensemble.

## 5. Bayesian cognition and sequential comparison

Knill and Pouget (2004) discuss uncertainty in neural computation; Jacobs and Kruschke (2011) review Bayesian learning models in cognition. These provide computational perspectives rather than blanket proof that all human judgments are Bayes-optimal. [Neural uncertainty](https://doi.org/10.1016/j.tins.2004.10.007); [cognitive learning review](https://doi.org/10.1002/wcs.80). Baldi and Itti (2010) formulate Bayesian surprise through belief change, motivating the distinction between event rarity and model revision. [Bayesian surprise](https://doi.org/10.1016/j.neunet.2009.12.007).

URID uses `posterior proportional to likelihood × prior` as a discipline for competing explanations. Binary log odds update by the log Bayes factor. The supplied helper tempers that change by a chosen quality weight: `logit(p_new)=logit(p_old)+w log(BF)`. Because neither likelihoods nor weights are calibrated here, this is a reasoning scaffold. It does not justify statements such as an exact chance that another person is in love.

For exclusive, exhaustive hypotheses, a posterior distribution can be normalized across alternatives. Many interpersonal propositions are not exclusive: someone can be friendly, attracted, uncertain, and committed to a boundary simultaneously. Normalizing their separate scores would create a false competition. The skill therefore distinguishes binary propositions from categorical partitions and records an open model boundary when explanations are incomplete.

Sequential updating requires care about dependence. Several screenshots of the same conversation are not several independent episodes. A self-report and the action it describes may share a source or arise from the same underlying event. Treating every fragment as an independent likelihood multiplies confidence without adding new observations. URID clusters related fragments and asks whether a later event adds a distinct constraint.

The prior also needs transparency. A plausible range of starting assumptions may produce different outcomes under weak evidence. Sensitivity analysis should reveal that dependence rather than hide it beneath a single precise score. A strong contrary event can reduce confidence or change the preferred account. Bayesian surprise measures the extent of that revision under the model; it does not certify that the revision moved closer to reality. Truth still depends on evidence quality and model adequacy.

## 6. From statistical mechanics to multiscale interpersonal dynamics

A physical microstate is a complete microscopic configuration; a macrostate groups microstates under macroscopic descriptors. An observed message is plainly not a physical microstate of a person. URID's event-to-pattern language is a computational analogy for aggregation across episodes. Its purpose is to prevent one local fluctuation from becoming an enduring claim.

Coarse-graining can be represented as `M_t=f(O_(t-k):t,C_(t-k):t)`. The analyst must specify the window, episode independence, relevant contexts, and missing observations. A summary of repeated direction is informative only if it retains the conditions that generate exceptions. Averaging deadline behaviour and relaxed social behaviour into “moderately firm” may erase a useful switching signature.

State-space descriptions permit recurrent trajectories such as uncertainty → reassurance-seeking → experienced pressure → withdrawal → more uncertainty. Calling a trajectory attractor-like describes recurrence; it does not establish a mathematically estimated attractor. Metastability similarly names relative persistence that can change. A close undefined relationship may remain in that configuration for a long time without progressing to romance. There is no inevitable endpoint built into the metaphor.

A possible regime transition requires more than a memorable phrase. URID looks for multiple dimensions changing, a significant event or context shift, and persistence in subsequent independent episodes. The implemented flag detects only a narrow descriptive pattern of sustained sign reversals. It neither proves a transition nor captures every meaningful change. Human review must consider whether a new environment altered opportunities instead of motives.

Path dependence means history affects interpretation. Hysteresis is stronger: response under comparable current conditions depends on the direction or history of transition. Evidence that one phrase means different things before and after conflict is sufficient for historical conditioning, not necessarily hysteresis. Dimensionless energy `-log p` and posterior temperature are optional mathematical reparameterizations. They do not measure emotional forces or heat. Kyselo and Tschacher (2014) offer a theoretical dynamical account of dyadic relations, supporting consideration of interaction while not validating URID. [Dyadic systems account](https://doi.org/10.3389/fpsyg.2014.00452).

### Free-energy reference and critique

Friston (2010) presents the influential free-energy principle; Fiorillo (2010) offers a critical neurocentric perspective on Bayesian inference. Sims (2016) raises a problem of scope, and Colombo and Wright (2021; first online 2018) examine the principle's scientific status and explanatory limits. [Friston](https://doi.org/10.1038/nrn2787); [Fiorillo](https://doi.org/10.1038/nrn2787-c1); [Sims](https://doi.org/10.1080/09515089.2016.1200024); [Colombo & Wright](https://doi.org/10.1007/s11229-018-01932-w).

URID uses generative-model framing, latent-state inference, and the observation that actions affect future evidence. It does not implement variational inference or minimize a variational free-energy objective. Psychological discomfort is not free energy; surprisal, prediction error, and entropy are different quantities. A broad principle cannot replace specifying a falsifiable local mechanism. These boundaries let the architecture borrow a useful modelling orientation without presenting contested universal claims as established interpersonal facts.

## 7. Personality as dynamic distributions

Mischel and Shoda's (1995) CAPS account connects stable personality structure with situation-sensitive cognitive-affective organisation. Fleeson (2001) represents traits through density distributions of states, and Fleeson and Jayawickreme (2015) develop Whole Trait Theory with descriptive and explanatory components. [CAPS](https://doi.org/10.1037/0033-295X.102.2.246); [state distributions](https://doi.org/10.1037/0022-3514.80.6.1011); [Whole Trait Theory](https://doi.org/10.1016/j.jrp.2014.10.009).

The URID representation has four practical layers: relatively stable tendencies, contextual modes, current state, and developmental trajectory. A person can be gentle in ordinary conversation and firm when a shared deadline is threatened. The useful hypothesis identifies the trigger and goal, not a generic “both strong and soft” description. A temporary state explanation remains a rival until enough observations distinguish it from a conditional policy.

Mode labels such as achievement, intimacy, threat, or recovery are analyst-generated descriptions. They do not identify neurological modules or validated categories. The skill must ask whether the labels compress recurring observations or merely rename them. A switching rule should make a prospective conditional prediction: when the same relevant trigger occurs with comparable opportunity, a particular response should become more likely.

Sparse records cannot estimate a state density. A qualitative tendency is consequently more defensible than an invented trait percentile. Nor should a slow trait model be frozen: major transitions and sustained new behaviour can revise it. The important distinction is timescale and coverage. A week of exhaustion informs current state; repeated responses across months and contexts provide a different type of constraint. Both belong in the model without forcing one to erase the other.

## 8. Emotion and regulation

McRae and Gross (2020) review emotion regulation. Ayduk and Kross (2010) examine spontaneous self-distancing in reflection, and Carver and Harmon-Jones (2009) review anger's approach-related character. These sources help separate experienced emotion, regulation strategy, and resulting behaviour. [Regulation](https://doi.org/10.1037/emo0000703); [self-distancing](https://doi.org/10.1037/a0019205); [anger and approach](https://doi.org/10.1037/a0013965).

URID asks how a person moves from emotion to action under particular constraints. Reappraisal, distancing, attentional shifts, response restraint, and practical action may serve different goals. Calm wording does not prove low emotional intensity, and anger does not establish loss of control. The model needs observations of what changed and what followed rather than reading the outward expression as a transparent window.

Rosenbaum, Gong, and Potts (2014) report hastened subgoal completion at additional physical cost, while Epley, Waytz, and Cacioppo (2007) theorise anthropomorphism. [Precrastination](https://doi.org/10.1177/0956797614532657); [anthropomorphism](https://doi.org/10.1037/0033-295X.114.4.864). These narrow constructs provide possible descriptions, not general-purpose explanations of interpersonal behaviour. A motor-task finding does not automatically explain rapid messaging; affectionate language to a device does not prove universal human empathy.

The URID bridge is deliberately conditional. A construct should be used only if it explains a contrast that ordinary context does not already explain. A warm statement, a distressed metaphor, and a task-closing action might have unrelated functions. Applying one broad theory to all three would remove distinctions the model is supposed to preserve. Literature can suggest a mechanism, but evidence from the case must determine whether it is relevant.

## 9. Language as probabilistic action

Goodman and Frank (2016) review pragmatic interpretation as probabilistic inference. Rational Speech Act models connect a listener's interpretation with a model of a speaker's context-sensitive communicative choice. A schematic speaker balances informativeness and cost; a pragmatic listener inverts that policy using priors. [Pragmatic inference](https://doi.org/10.1016/j.tics.2016.08.005).

URID translates this into close reading: literal content, conversational function, plausible goal, expression cost, available alternatives, omissions, baseline, and history. A statement may repair, soften, invite, reassure, defer, or set a boundary. It can do several things at once. Its relational effect depends on what follows and how it compares with the speaker's ordinary style.

Counterfactual utterance space is useful but dangerous. A specific apology can be more costly than a generic polite exit, supporting an account of relational importance. Yet the analyst cannot assume the speaker consciously evaluated every possible phrase. Language competence, local norms, fatigue, habitual scripts, and fear can restrict the available choices. The model must distinguish an alternative the analyst imagines from one the speaker plausibly had.

Omissions also require opportunity. Not using a romantic label may reflect lack of such intent, reluctance, ambiguity, or simply a conversation that did not call for it. The absence becomes informative only under assumptions that should be stated. Explicit boundaries receive a different treatment: they guide conduct even if the analyst imagines uncertain underlying motives. Pragmatic subtlety cannot turn refusal into consent.

The communication model is therefore an explanatory scaffold, not a mind-reading mechanism. A short cue may support only a short, low-confidence interpretation. Greater depth should come from relevant context and comparison, not multiplying speculative motives. Human-facing analysis can say what the utterance accomplished in the interaction while admitting that its private intention remains partly unknown.

## 10. Narrative identity as a slow self-model

McAdams and McLean (2013) describe narrative identity as an evolving life story connecting reconstructed past and imagined future. McLean, Pasupathi, and Pals (2007) develop a process account of stories and self-development. [Narrative identity](https://doi.org/10.1177/0963721413475622); [self-development process](https://doi.org/10.1177/1088868307301034).

URID treats narrative as a slow layer with practical consequences: experience → appraisal → meaning making → self-model revision → action-rule revision → later behaviour. An essay can reveal how the author currently organises continuity, rupture, agency, loss, or possibility. It does not directly establish a complete personality or verify every event it recounts.

The developmental inference requires distinctions between retrospective meaning, declared intention, enacted change, and stable new practice. “I learned to ask for help” supports a reported rule. A later relevant request provides behavioural evidence of using it. Repeated use after setbacks provides stronger support for persistence. This sequence allows meaningful interpretation without taking a growth story as its own validation.

Agency, redemption, contamination, and future-self themes are descriptive patterns, not moral rankings. A narrative need not redeem loss to be coherent or valuable. Refusal of a hopeful ending can preserve truth. Public genre, audience, and cultural scripts affect what is told. Elegance may make a pattern legible while providing no additional reason to believe it is enacted.

The architecture integrates rather than isolates narrative: a changed self-story may suggest a new communication policy, which future interaction can support or contradict. If behaviour contradicts it, revise the policy hypothesis while preserving the reality of the expressed aspiration. This is how the model recognises becoming without claiming that every articulate person has already become the person they describe.

## 11. Relationship science as latent-state semantics

Canevello and Crocker (2010) examine responsiveness, relationship quality, and interpersonal goals. Ryan and Deci (2000) provide the self-determination perspective on autonomy and related needs. Feeney and Thrush (2010) examine secure-base support for exploration in adulthood. [Responsiveness](https://doi.org/10.1037/a0018186); [self-determination](https://doi.org/10.1037/0003-066X.55.1.68); [secure base](https://doi.org/10.1037/a0016961).

Laurenceau, Barrett, and Pietromonaco (1998) test an interpersonal process account linking disclosure and perceived responsiveness with experienced intimacy. [Intimacy-process study](https://doi.org/10.1037/0022-3514.74.5.1238). URID uses these constructs to keep care, closeness, choice, and exploration distinguishable. Feeling understood is not the same as being agreed with. Support can encourage independent activity; autonomy need not mean low connection. Conversely, intrusive involvement should not be classified as supportive merely because it involves effort. The relevant question is how the recipient's choice and needs enter the interaction.

Le and Agnew's (2003) investment-model meta-analysis concerns commitment and theorized determinants. Aron, Aron, and Smollan (1992) study self-inclusion and interpersonal closeness. Girme et al. (2018) examine within-person variation in relationship-specific attachment. [Commitment](https://doi.org/10.1111/1475-6811.00035); [self-inclusion](https://doi.org/10.1037/0022-3514.63.4.596); [attachment variability](https://doi.org/10.1037/pspi0000115).

These sources motivate separate coordinates for commitment, self-expansion, and security-related variation. The self-inclusion paper is a narrower source than a complete theory of self-expansion. Aron et al. (2000) additionally examine shared novel/arousing activities and experienced relationship quality, supporting an activity-based bridge while not proving attraction from shared novelty. [Shared activity study](https://doi.org/10.1037/0022-3514.78.2.273). Population findings similarly cannot identify a particular person's motive. Investment may support persistence without proving satisfaction, safety, or a duty to remain.

Rose (2002) introduces co-rumination, relating repeated problem-focused talk to friendship and emotional adjustment in young people. Falconier et al. (2015) meta-analyse dyadic coping and relationship satisfaction. [Co-rumination](https://doi.org/10.1111/1467-8624.00509); [dyadic coping](https://doi.org/10.1016/j.cpr.2015.07.002). Their scope cautions against treating all deep conversation as either healing or harmful.

URID's constructive co-reflection contrast is a descriptive proposal: does discussion broaden perspective, revise a rule, or support feasible action, or mainly repeat distress? It is not a new validated diagnostic category. Likewise intrusive romantic thinking can have many causes; the present review does not validate a limerence classifier. Repair is assessed through accountability and follow-through, not promises alone. These distinctions provide human meanings for latent variables without collapsing all relationships into attachment types.

## 12. Unified URID architecture

The proposed integration assigns each theoretical family a specific job. Psychological research specifies candidate variables; pragmatics specifies how communication can depend on intentions and context; probabilistic comparison keeps alternative accounts alive; information diagnostics describe changes in a specified explanatory distribution; multiscale aggregation checks whether episodes justify a persistent pattern; narrative analysis tracks slower self-policy development.

```text
Context and observation opportunity
                 |
Person A state <-> Relationship state <-> Person B state
                 |
       utterances / actions / timing / repair
                 |
      provenance-sensitive evidence ledger
                 |
   competing models -> belief revision -> information audit
                 |
     multiepisode/context coarse-graining
                 |
     dynamic and narrative human synthesis
                 |
    natural future evidence -> next revision
```

Let `P_i(t)={theta_i,m_i(t),x_i(t),g_i(t),v_i,n_i(t),pi_i(t)}` collect disposition, mode, current state, goals, values, narrative model, and policy. Let R represent relationship dimensions and C context. The emission is `p(O_t|P_A(t),P_B(t),R(t),C_t)`. A switching state-space transition represents current states as conditional on previous states, modes, context, and prior actions. Full factorization appears in `formal-model.md`.

Coupling matters because an action changes subsequent conditions. One person's demand for reassurance can alter the other's experienced pressure; the resulting delay can alter the first person's uncertainty. A pair of static personality labels cannot represent this loop. The proposed model instead separates actor contribution, partner contribution, and their interaction, without claiming causal identification from sparse chronology.

The architecture's unity is methodological, not ontological. Entropy does not become emotion, narrative does not become energy, and responsiveness does not become a Bayes factor without assumptions. The bridges coordinate questions and evidence types. Formal validity within one layer does not establish validity of every mapping to another layer. This separation is the central safeguard against using “unified” to imply empirical completeness.

## 13. Inference workflow

The skill parses people, dates, stage, quotations, actions, omissions, and context changes. It records facts separately from inferred motives and keeps person IDs distinct. The ledger adds source quality, baseline, opportunity cost, ambiguity, and episode dependence. It then forms two to four competing accounts for the core question while preserving an unmodelled possibility.

Comparison asks which account makes an observation more expected. An information audit identifies genuine model-changing evidence, redundant confirmation, and surprising but irrelevant cues. Coarse-graining checks repeated direction, cross-context coverage, recovery, and switching rules. Dynamic analysis looks for reciprocal loops; psychological semantics explains the narrowest useful mechanism. Narrative and pragmatic layers are used only when the supplied material supports them.

A countermodel and strongest disconfirming observation are mandatory for major conclusions. When contrary evidence is absent from the supplied record, the answer should say so rather than pretend it has exhaustively searched a life. A falsifier specifies a naturally observable event or a boundary that would require a downgrade. Discriminating future evidence should be tied to realistic opportunities.

The final answer distinguishes known, likely, plausible, and unknown. It leads with what changed, close-reads observations, explains conditional mechanisms and development, situates the reciprocal relationship, and only then offers existential interpretation if warranted. One to three sentences may compress the insight, but the ending cannot introduce a stronger conclusion than the preceding evidence established.

This sequence is not a demand to publish every intermediate mental operation. The default output is human language. When asked for a model trace, the skill provides an auditable summary of evidence, hypotheses, revisions, and uncertainty. It does not reveal hidden chain-of-thought or present subjective scores as calibrated measurements.

## 14. Worked fictional example

Consider an entirely invented pair, Person A and Person B. A usually replies irregularly during intensive work but follows through on agreed meetings. B notices one three-day silence and interprets it as indifference. A later acknowledges that an agreed follow-up was missed, apologises specifically, and proposes a practical schedule. Over the next month A follows the schedule twice and initiates once after the busy period ends.

The first ledger separates a delay from B's interpretation. Workload and an irregular baseline make the delay weak evidence for indifference. The later apology has more relevant content: responsibility for a specific expectation and a proposed repair. The later enacted schedule is a distinct episode, providing evidence about a revised contact policy rather than merely repeating the apology's wording.

Useful competing accounts are ordinary friendship with conscientious repair, special relational importance, and possible attraction. These may overlap, so they are not automatically a categorical distribution. Evidence of initiative after a context change discriminates some baseline explanations, but it still does not establish exclusivity. B's hope that it means romance is evidence about B's appraisal, not an additional observation of A's intentions.

A possible switching rule is that open-ended messaging receives lower priority during intensive work, while explicit shared commitments activate accountability. A rival is impression management after a complaint. Sustained follow-through without further prompting would favour the accountable-policy account; repeated missed arrangements without correction would weaken it. Neither account requires a permanent attachment label.

The relationship model can now describe increased repair motivation, some reciprocity, and uncertain romantic type. A natural future discriminator is whether A independently integrates B into realistic plans and communicates their meaning. A direct conversation is also possible if B wants clarity, with respect for A's present boundaries. Deliberately disappearing to provoke anxiety would change the interaction through manipulation rather than reveal an unaltered truth.

An earned human synthesis is: the repair and follow-through make it harder to interpret the connection as disposable. They say more about preserving it than about naming it. The uncertainty that remains concerns the kind of importance, not whether the observed efforts happened.

## 15. Falsifiability and model revision

An interpretation earns explanatory status by risking revision. “A repairs important relationships” should specify what counts as repair, what opportunity existed, and how repeated failures without follow-through would affect the model. “A is secretly attracted regardless of every refusal” has no usable falsifier and must be rejected. Reinterpretation cannot be an unlimited licence to protect an emotionally preferred story.

Falsifiers are often graded rather than a single decisive event. Consistent baseline-specific initiative may upgrade specialness; evidence that the same behaviour is universal may downgrade it. Explicit changed intentions can revise a past interpretation. The skill must preserve temporal indexing: an earlier account may have been plausible then and become inadequate now, without pretending the earlier observations never occurred.

Prospective predictions should be conditional on opportunity and context. If a person has no chance to follow through, nonoccurrence is not the same observation as declining a feasible commitment. The hypothesis should be precise enough to make this distinction before the next event, reducing hindsight flexibility. Prediction records should remain local when they concern real people.

Revision also applies to the framework's representation. If ordinary workload explains the observations better than an elaborate narrative mechanism, remove the extra mechanism. If no proposed explanation distinguishes future observations, acknowledge non-identifiability. A useful analysis can leave several models viable while identifying what each would require. This is a disciplined incomplete model, not a failure to answer.

## 16. Ethical limits

This skill is not a clinical diagnosis, crisis assessment, treatment, or deterministic mind-reading tool. It should route urgent safety or health needs to appropriate workflows rather than reinterpret them as relationship ambiguity. Literary language about emptiness or mortality alone does not establish symptoms. A label should not substitute for understanding the expressed experience.

Respect for autonomy constrains information seeking. Jealousy induction, deceptive tests, fake withdrawal, covert monitoring, and surveillance are not acceptable routes to clarification. Another person's stated boundary guides conduct even when a model considers conflicting feelings possible. The goal is more accurate understanding, not leverage over the person being described.

Privacy is an architectural property: the public skill contains generic instructions, schemas, scripts, theory, and independently invented fixtures. Local overlays contain personal preferences and identifiable records, remain ignored, and are never uploaded merely because the public framework is open source. The actual Git index and reachable history require inspection; deleting a current file does not remove its earlier public versions.

Warmth in output does not require optimistic conclusions. It means treating uncertainty honestly, preserving both participants' agency, and making the structure understandable without humiliation or flattery. An analysis should not encourage endless decoding of tiny cues. Sometimes a boundary, a practical decision, or a respectful direct question is more useful than another layer of speculative interpretation.

## 17. Limitations

URID has no empirical calibration or demonstrated predictive superiority. Its numerical factors are chosen heuristics. A posterior-like score reflects assumptions, not an observed frequency. Scores may be highly sensitive to priors, likelihood judgments, or which competing explanations were included. Static validation cannot turn those assumptions into measured psychological parameters.

Sparse and selected data are the ordinary case. Users may supply emotionally salient excerpts, omit mundane contacts, misremember timing, or have little access to a person's baseline. Missing evidence is often informative about the observation process rather than the person. Cultural differences in politeness, disclosure, scheduling, and relationship labels can change the meaning of otherwise similar events.

Observer projection creates another limitation. A user's valued qualities may be perceived more readily in a desired partner. A language model can amplify this projection by building a coherent story from selected material. Coherence and elegance can make an explanation feel verified even when alternatives remain equally compatible. The explicit countermodel mitigates this risk without eliminating it.

Non-identifiability is pervasive: different state, goal, and policy combinations can generate the same action. Temporal ordering does not establish causal effects. Relationships are open systems influenced by work, family, health, institutions, and unobserved interactions. Coupled dynamics are a useful representation, not evidence that the observed pair forms a closed system with stable transition parameters.

Conceptual borrowing has its own hazards. Coarse-graining can erase conditional signatures; mode labels can become new stereotypes; narrative development can be inferred from prose without action; information quantities can imply false precision. Statistical-mechanical analogy does not establish a physical mechanism. The FEP reference is contested and optional, not a foundation that makes every local account true.

Finally, this is a conceptual bridge rather than empirical unification. Tests verify helper invariants and privacy failure cases; semantic fixtures specify expected behaviour. Neither proves that a language model consistently follows the protocol or understands an individual accurately. Future evaluation must measure both performance and failure modes under realistic conditions. Until then, restraint, unknowns, and explicit limits belong in ordinary use.

## 18. Research agenda

A credible validation programme would begin with consented longitudinal interaction corpora, not scraped private communications. Records would need context, observation opportunity, baseline behaviour, and independent outcome labels. Multi-informant accounts could distinguish the user's appraisal from the partner's reported intention and independently observed conduct. Privacy and consent would determine what could be retained or shared.

Prospective preregistration would limit hindsight storytelling. Analysts could specify hypotheses, confidence, falsifiers, and conditional predictions before subsequent interactions occur. Evaluation would assess whether new evidence revises old accounts, whether incorrect certainty is reduced, and whether models remain discriminative when ordinary counterexplanations are introduced. Absent opportunities should be coded rather than treated as failed predictions.

A numerical model, if later developed, would need held-out calibration curves, proper scoring rules, coverage across cultures and relationship stages, and clear separation of training and evaluation individuals. Hierarchical Bayesian or switching state-space models could be compared with simpler baselines. Adding complexity would need demonstrable value rather than prestige. Neural probabilistic models remain future work, not current capability.

Human expert comparisons should evaluate source handling, distinctions between constructs, and practical usefulness, not simply agreement with a preferred romantic conclusion. Ablations could remove pragmatics, history, narrative evidence, countermodels, or dependence discounting to test which components improve performance. Synthetic fixtures would remain useful for stress-testing, but naturalistic prospective outcomes would be necessary for validity claims.

The key research question is whether this architecture improves calibrated restraint and explanatory discrimination while preserving human usefulness. A skill that says “unknown” accurately may outperform one that confidently names a hidden motive. Genuine progress would combine prospective prediction, transparent failure analysis, privacy protection, and an ability to revise the architecture itself when simpler or better-supported alternatives emerge.

## References

The following APA-style entries use DOI-verified authors, venues, volume/issue and
pages or article numbers. Print/issue years are used where online-first years differ.


Aron, A., Aron, E. N., & Smollan, D. (1992). Inclusion of Other in the Self Scale and the structure of interpersonal closeness. *Journal of Personality and Social Psychology, 63*(4), 596–612. https://doi.org/10.1037/0022-3514.63.4.596

Aron, A., Norman, C. C., Aron, E. N., McKenna, C., & Heyman, R. E. (2000). Couples' shared participation in novel and arousing activities and experienced relationship quality. *Journal of Personality and Social Psychology, 78*(2), 273–284. https://doi.org/10.1037/0022-3514.78.2.273

Ayduk, Ö., & Kross, E. (2010). From a distance: implications of spontaneous self-distancing for adaptive self-reflection. *Journal of Personality and Social Psychology, 98*(5), 809–829. https://doi.org/10.1037/a0019205

Baldi, P., & Itti, L. (2010). Of bits and wows: a Bayesian theory of surprise with applications to attention. *Neural Networks, 23*(5), 649–666. https://doi.org/10.1016/j.neunet.2009.12.007

Canevello, A., & Crocker, J. (2010). Creating good relationships: responsiveness, relationship quality, and interpersonal goals. *Journal of Personality and Social Psychology, 99*(1), 78–106. https://doi.org/10.1037/a0018186

Carver, C. S., & Harmon-Jones, E. (2009). Anger is an approach-related affect: evidence and implications. *Psychological Bulletin, 135*(2), 183–204. https://doi.org/10.1037/a0013965

Colombo, M., & Wright, C. (2021). First principles in the life sciences: the free-energy principle, organicism, and mechanism. *Synthese, 198*(Suppl. 14), 3463–3488. https://doi.org/10.1007/s11229-018-01932-w

Epley, N., Waytz, A., & Cacioppo, J. T. (2007). On seeing human: a three-factor theory of anthropomorphism. *Psychological Review, 114*(4), 864–886. https://doi.org/10.1037/0033-295X.114.4.864

Falconier, M. K., Jackson, J. B., Hilpert, P., & Bodenmann, G. (2015). Dyadic coping and relationship satisfaction: a meta-analysis. *Clinical Psychology Review, 42*, 28–46. https://doi.org/10.1016/j.cpr.2015.07.002

Feeney, B. C., & Thrush, R. L. (2010). Relationship influences on exploration in adulthood: the characteristics and function of a secure base. *Journal of Personality and Social Psychology, 98*(1), 57–76. https://doi.org/10.1037/a0016961

FeldmanHall, O., & Shenhav, A. (2019). Resolving uncertainty in a social world. *Nature Human Behaviour, 3*(5), 426–435. https://doi.org/10.1038/s41562-019-0590-x

Fiorillo, C. D. (2010). A neurocentric approach to Bayesian inference. *Nature Reviews Neuroscience, 11*(8), 605–605. https://doi.org/10.1038/nrn2787-c1

Fleeson, W. (2001). Toward a structure- and process-integrated view of personality: traits as density distributions of states. *Journal of Personality and Social Psychology, 80*(6), 1011–1027. https://doi.org/10.1037/0022-3514.80.6.1011

Fleeson, W., & Jayawickreme, E. (2015). Whole trait theory. *Journal of Research in Personality, 56*, 82–92. https://doi.org/10.1016/j.jrp.2014.10.009

Friston, K. (2010). The free-energy principle: a unified brain theory?. *Nature Reviews Neuroscience, 11*(2), 127–138. https://doi.org/10.1038/nrn2787

Girme, Y. U., Agnew, C. R., VanderDrift, L. E., Harvey, S. M., Rholes, W. S., & Simpson, J. A. (2018). The ebbs and flows of attachment: within-person variation in attachment undermine secure individuals’ relationship wellbeing across time. *Journal of Personality and Social Psychology, 114*(3), 397–421. https://doi.org/10.1037/pspi0000115

Goodman, N. D., & Frank, M. C. (2016). Pragmatic language interpretation as probabilistic inference. *Trends in Cognitive Sciences, 20*(11), 818–829. https://doi.org/10.1016/j.tics.2016.08.005

Jacobs, R. A., & Kruschke, J. K. (2011). Bayesian learning theory applied to human cognition. *WIREs Cognitive Science, 2*(1), 8–21. https://doi.org/10.1002/wcs.80

Jaynes, E. T. (1957a). Information theory and statistical mechanics. *Physical Review, 106*(4), 620–630. https://doi.org/10.1103/PhysRev.106.620

Jaynes, E. T. (1957b). Information theory and statistical mechanics. ii. *Physical Review, 108*(2), 171–190. https://doi.org/10.1103/PhysRev.108.171

Knill, D. C., & Pouget, A. (2004). The Bayesian brain: the role of uncertainty in neural coding and computation. *Trends in Neurosciences, 27*(12), 712–719. https://doi.org/10.1016/j.tins.2004.10.007

Kyselo, M., & Tschacher, W. (2014). An enactive and dynamical systems theory account of dyadic relationships. *Frontiers in Psychology, 5*, Article 452. https://doi.org/10.3389/fpsyg.2014.00452

Laurenceau, J.-P., Barrett, L. F., & Pietromonaco, P. R. (1998). Intimacy as an interpersonal process: the importance of self-disclosure, partner disclosure, and perceived partner responsiveness in interpersonal exchanges. *Journal of Personality and Social Psychology, 74*(5), 1238–1251. https://doi.org/10.1037/0022-3514.74.5.1238

Le, B., & Agnew, C. R. (2003). Commitment and its theorized determinants: a meta–analysis of the Investment Model. *Personal Relationships, 10*(1), 37–57. https://doi.org/10.1111/1475-6811.00035

McAdams, D. P., & McLean, K. C. (2013). Narrative identity. *Current Directions in Psychological Science, 22*(3), 233–238. https://doi.org/10.1177/0963721413475622

McLean, K. C., Pasupathi, M., & Pals, J. L. (2007). Selves creating stories creating selves: a process model of self-development. *Personality and Social Psychology Review, 11*(3), 262–278. https://doi.org/10.1177/1088868307301034

McRae, K., & Gross, J. J. (2020). Emotion regulation. *Emotion, 20*(1), 1–9. https://doi.org/10.1037/emo0000703

Mischel, W., & Shoda, Y. (1995). A cognitive-affective system theory of personality: reconceptualizing situations, dispositions, dynamics, and invariance in personality structure. *Psychological Review, 102*(2), 246–268. https://doi.org/10.1037/0033-295X.102.2.246

Ong, D. C., Zaki, J., & Goodman, N. D. (2019). Computational models of emotion inference in theory of mind: a review and roadmap. *Topics in Cognitive Science, 11*(2), 338–357. https://doi.org/10.1111/tops.12371

Rose, A. J. (2002). Co–rumination in the friendships of girls and boys. *Child Development, 73*(6), 1830–1843. https://doi.org/10.1111/1467-8624.00509

Rosenbaum, D. A., Gong, L., & Potts, C. A. (2014). Pre-crastination: hastening subgoal completion at the expense of extra physical effort. *Psychological Science, 25*(7), 1487–1496. https://doi.org/10.1177/0956797614532657

Ryan, R. M., & Deci, E. L. (2000). Self-determination theory and the facilitation of intrinsic motivation, social development, and well-being. *American Psychologist, 55*(1), 68–78. https://doi.org/10.1037/0003-066X.55.1.68

Sayood, K. (2018). Information theory and cognition: a review. *Entropy, 20*(9), Article 706. https://doi.org/10.3390/e20090706

Shannon, C. E. (1948a). A mathematical theory of communication. *Bell System Technical Journal, 27*(3), 379–423. https://doi.org/10.1002/j.1538-7305.1948.tb01338.x

Shannon, C. E. (1948b). A mathematical theory of communication. *Bell System Technical Journal, 27*(4), 623–656. https://doi.org/10.1002/j.1538-7305.1948.tb00917.x

Sims, A. (2016). A problem of scope for the free energy principle as a theory of cognition. *Philosophical Psychology, 29*(7), 967–980. https://doi.org/10.1080/09515089.2016.1200024
