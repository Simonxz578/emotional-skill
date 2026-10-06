# Public core and private overlay

Public: instructions, generic theories, helper scripts, schemas, tests, and invented examples. Private: local profile, real texts, names, chart data, events, model files, and derived identifiable summaries. All `private/` contents are ignored. Keep the source prompt outside the repository. Never copy a user's real case into a fictional public example with names merely removed.

Read relevant local context only within the user's authorised task. Treat profile contents as revisable preferences/self-reports; do not use them as facts about another person. Keep separate person IDs and relationship histories. Store new models only on request, under ignored private storage. Never upload the overlay via commits, issues, gists, logs, or artifacts.

`validate_privacy.py` checks actual index blobs, tracked working files, and reachable commit history, including messages. It detects private paths, common email/phone/address patterns, profile markers, exact long overlay excerpts, and optional local private terms from `private/privacy-terms.json`. This local JSON must remain ignored; no public exceptions/allowlist for private data.

Stage an explicit public candidate, inspect `git diff --cached`, `git status --short`, and `git ls-files`, then run the validator. A clean untracked working directory alone is not evidence of a clean commit. Scan reachable history before and after committing, then verify the remote commit. Do not publish scanner output containing matched private text.

If accidentally staged, untrack before committing. If committed locally, repair unpublished history and rerun checks. If pushed, stop and disclose the leak; do not hide it with a later deletion. Public history retains prior blobs. Automated checks cannot detect all identifying paraphrases or unknown context, so manual review remains required.
