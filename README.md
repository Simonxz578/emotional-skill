# Emotional Skill

A reusable skill for analysing emotional communication, personal narratives, interpersonal dynamics, and relationship signals using evidence-weighted reasoning.

## What it does

Interprets messages and behaviours, compares explanations, and revises person and relationship models as evidence changes. Internally, it combines probabilistic inference, multiscale dynamic reasoning, pragmatics, and psychological theory.

## Basic usage

Place this folder in your agent's skills directory under `emotional-analysis`, then ask it to use **emotional-analysis** with the messages, narrative, or interactions you want analysed. Read `SKILL.md` for the workflow.

Validate locally with `python3 -m unittest discover -s tests -v`, `python3 scripts/validate_skill.py`, and `python3 scripts/validate_privacy.py`.

## Privacy note

Examples are fictional. Personal context belongs only in the ignored `private/` directory. The privacy validator checks the Git index and reachable history; automated scanning cannot guarantee the absence of every identifying detail. Review public changes before publishing.
