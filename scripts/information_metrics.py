"""Distribution diagnostics in nats by default; base=2 gives bits.

These describe supplied model distributions, not calibrated interpersonal truth.
"""
import math
try:
    from .belief_update import finite_number
except ImportError:
    from belief_update import finite_number


def distribution(values):
    values = [finite_number(v, 'probability') for v in values]
    if not values or any(v < 0 or v > 1 for v in values):
        raise ValueError('nonempty probabilities in [0, 1] required')
    if not math.isclose(math.fsum(values), 1.0, rel_tol=0, abs_tol=1e-9):
        raise ValueError('probabilities must sum to 1; no silent normalization')
    return values


def log_unit(base):
    base = finite_number(base, 'base')
    if base <= 1:
        raise ValueError('log base must exceed 1')
    return math.log(base)


def entropy(probabilities, base=math.e):
    p, unit = distribution(probabilities), log_unit(base)
    return -math.fsum(x * math.log(x) for x in p if x > 0) / unit


def kl_divergence(p, q, base=math.e):
    p, q, unit = distribution(p), distribution(q), log_unit(base)
    if len(p) != len(q):
        raise ValueError('distributions must share the same ordered support')
    if any(a > 0 and b == 0 for a, b in zip(p, q)):
        return math.inf
    return max(0.0, math.fsum(a * (math.log(a) - math.log(b)) for a, b in zip(p, q) if a > 0) / unit)


def surprisal(probability, base=math.e):
    p, unit = finite_number(probability, 'probability'), log_unit(base)
    if not 0 <= p <= 1:
        raise ValueError('probability must be in [0, 1]')
    return math.inf if p == 0 else -math.log(p) / unit


def normalized_entropy(probabilities):
    p = distribution(probabilities)
    return 0.0 if len(p) == 1 else entropy(p) / math.log(len(p))


def qualitative_information_gain(prior, posterior):
    """Posterior-to-prior KL; heuristic bands, not measured mutual information.

    A realized update can increase entropy while having positive KL divergence.
    """
    prior, posterior = distribution(prior), distribution(posterior)
    value = kl_divergence(posterior, prior)
    return {'kl_nats': value, 'entropy_change_nats': entropy(posterior) - entropy(prior),
            'qualitative_band': 'low' if value < 0.05 else 'medium' if value < 0.5 else 'high',
            'caveat': 'Bands are arbitrary display aids; KL measures model revision, not truth.'}
