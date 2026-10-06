#!/usr/bin/env python3
"""Uncalibrated reasoning scaffold, not a psychological prediction model.

Evidence strength is the nonnegative magnitude of a log Bayes factor in nats.
Weight tempers that log factor; repeated dependent observations need discounting.
"""
import argparse
import json
import math


def finite_number(value, name):
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
        raise ValueError(f'{name} must be a finite number')
    return float(value)


def update_belief(prior, direction, strength, weight=1.0):
    prior = finite_number(prior, 'prior')
    strength = finite_number(strength, 'strength')
    weight = finite_number(weight, 'weight')
    if not 0 < prior < 1:
        raise ValueError('prior must be strictly between 0 and 1; avoid irreversible certainty')
    signs = {'support': 1, 'contradict': -1, 'neutral': 0}
    if direction not in signs:
        raise ValueError('direction must be support, contradict, or neutral')
    if strength < 0 or not 0 <= weight <= 1:
        raise ValueError('strength must be nonnegative and weight in [0, 1]')
    delta = signs[direction] * strength * weight
    log_odds = math.log(prior) - math.log1p(-prior) + delta
    if log_odds >= 0:
        posterior = 1 / (1 + math.exp(-log_odds))
    else:
        e = math.exp(log_odds)
        posterior = e / (1 + e)
    # Keep output usable for another update when floating-point arithmetic saturates.
    posterior = min(math.nextafter(1.0, 0.0), max(math.nextafter(0.0, 1.0), posterior))
    return {'posterior': posterior, 'log_odds': log_odds, 'weighted_log_bayes_factor': delta,
            'explanation': f'{direction}: add {delta:.6g} nats to prior log odds; this is an uncalibrated internal score.'}


def effective_weight(**factors):
    allowed = {'directness', 'source_reliability', 'repetition_factor', 'behavioural_cost',
               'context_relevance', 'baseline_specificity', 'recency_factor'}
    if set(factors) != allowed:
        raise ValueError('supply all seven documented quality factors')
    values = [finite_number(v, k) for k, v in factors.items()]
    if any(not 0 <= v <= 1 for v in values):
        raise ValueError('quality factors must be in [0, 1]')
    return math.prod(values)


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--prior', type=float, required=True)
    p.add_argument('--direction', choices=['support', 'contradict', 'neutral'], required=True)
    p.add_argument('--strength', type=float, required=True)
    p.add_argument('--weight', type=float, default=1)
    args = p.parse_args()
    try:
        print(json.dumps(update_belief(args.prior, args.direction, args.strength, args.weight), indent=2))
    except ValueError as exc:
        p.error(str(exc))
