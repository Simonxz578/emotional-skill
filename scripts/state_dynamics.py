"""Transparent descriptive helpers; no fitted HMM or phase-transition predictor.

Event input: event_id, ISO timestamp, episode_id, context_id, dimension, direction
(-1/0/1), weight [0,1], optional source_type. Window is a positive number of days.
"""
from collections import defaultdict
from datetime import datetime, timedelta, timezone
try:
    from .belief_update import finite_number
except ImportError:
    from belief_update import finite_number


def timestamp(value):
    if not isinstance(value, str):
        raise ValueError('timestamp must be an ISO string')
    try:
        dt = datetime.fromisoformat(value.replace('Z', '+00:00'))
    except ValueError as exc:
        raise ValueError('invalid timestamp') from exc
    if dt.tzinfo is None:
        raise ValueError('timestamp must include timezone')
    return dt.astimezone(timezone.utc)


def checked(events):
    result, ids = [], set()
    for event in events:
        for key in ('event_id', 'episode_id', 'context_id', 'dimension'):
            if not isinstance(event.get(key), str) or not event[key]:
                raise ValueError(f'{key} required')
        if event['event_id'] in ids:
            raise ValueError('duplicate event_id')
        ids.add(event['event_id'])
        direction = finite_number(event.get('direction'), 'direction')
        weight = finite_number(event.get('weight'), 'weight')
        if direction not in (-1, 0, 1) or not 0 <= weight <= 1:
            raise ValueError('direction must be -1/0/1; weight in [0,1]')
        copy = dict(event, _time=timestamp(event.get('timestamp')))
        # Symbolic evidence cannot contribute behavioural support.
        if copy.get('source_type') == 'symbolic':
            copy['weight'] = 0.0
        result.append(copy)
    return sorted(result, key=lambda e: e['_time'])


def aggregate_events(events, window, as_of=None):
    days = finite_number(window, 'window')
    if days <= 0:
        raise ValueError('window must be positive days')
    items = checked(events)
    end = timestamp(as_of) if as_of else (items[-1]['_time'] if items else None)
    if end is None:
        return {}
    start = end - timedelta(days=days)
    groups = defaultdict(dict)
    for e in items:
        if start <= e['_time'] <= end:
            # One contribution per episode/dimension. Strongest observation wins;
            # tied conflicting observations neutralize rather than double count.
            old = groups[e['dimension']].get(e['episode_id'])
            if old is None or e['weight'] > old['weight']:
                groups[e['dimension']][e['episode_id']] = e
            elif e['weight'] == old['weight'] and e['direction'] != old['direction']:
                groups[e['dimension']][e['episode_id']] = dict(old, direction=0)
    return {d: {'episodes': sum(e['weight'] > 0 for e in es.values()), 'recorded_episodes': len(es), 'weighted_direction': sum(e['direction'] * e['weight'] for e in es.values()),
                'total_weight': sum(e['weight'] for e in es.values()),
                'contexts': sorted({e['context_id'] for e in es.values() if e['weight'] > 0})}
            for d, es in groups.items()}


def detect_consistent_direction(events):
    items = checked(events)
    if len({e['dimension'] for e in items}) > 1:
        raise ValueError('compare one dimension at a time')
    aggregate = aggregate_events(events, 365000)
    if not aggregate:
        return {'direction': 'unknown', 'episodes': 0, 'consistency': 0.0}
    a = next(iter(aggregate.values()))
    ratio = abs(a['weighted_direction']) / a['total_weight'] if a['total_weight'] else 0
    direction = 'mixed'
    if a['total_weight'] == 0 or a['episodes'] < 3:
        direction = 'unknown'
    elif ratio >= 0.75:
        direction = 'positive' if a['weighted_direction'] > 0 else 'negative'
    return {'direction': direction, 'episodes': a['episodes'], 'consistency': ratio}


def compare_fast_vs_slow_signal(fast_events, slow_events):
    f, s = detect_consistent_direction(fast_events), detect_consistent_direction(slow_events)
    conflict = {f['direction'], s['direction']} == {'positive', 'negative'}
    return {'fast': f, 'slow': s, 'conflict': conflict,
            'guidance': 'Investigate state/context switching; fast evidence alone cannot overwrite slow structure.'}


def flag_possible_regime_shift(before, after, min_episodes=3):
    if isinstance(min_episodes, bool) or not isinstance(min_episodes, int) or min_episodes < 3:
        raise ValueError('min_episodes must be an integer >= 3')
    b, a = checked(before), checked(after)
    if b and a and max(e['_time'] for e in b) >= min(e['_time'] for e in a):
        raise ValueError('before and after must be chronological nonoverlapping periods')
    changed = []
    for dim in {e['dimension'] for e in b} & {e['dimension'] for e in a}:
        bs = detect_consistent_direction([e for e in before if e['dimension'] == dim])
        ax = [e for e in after if e['dimension'] == dim]
        aa = detect_consistent_direction(ax)
        if ({bs['direction'], aa['direction']} == {'positive', 'negative'}
                and aa['episodes'] >= min_episodes
                and len({e['context_id'] for e in ax if e['weight'] > 0 and e.get('source_type') != 'symbolic'}) >= 2):
            changed.append(dim)
    return {'possible_shift': len(changed) >= 2, 'changed_dimensions': sorted(changed),
            'caveat': 'Descriptive flag only; inspect context, cost, sampling and persistence manually.'}


def build_competing_hypotheses(question, explanations):
    if not isinstance(question, str) or not question.strip():
        raise ValueError('question required')
    if not 2 <= len(explanations) <= 4 or any(not isinstance(s, str) or not s.strip() for s in explanations):
        raise ValueError('supply 2–4 nonempty explanations')
    if len(set(explanations)) != len(explanations):
        raise ValueError('explanations must be distinct')
    return {'question': question, 'models': [{'id': f'H{i+1}', 'explanation': s,
            'support': [], 'counterevidence': [], 'falsifiers': [], 'confidence': 'low'}
            for i, s in enumerate(explanations)], 'other_explanations_possible': True}
