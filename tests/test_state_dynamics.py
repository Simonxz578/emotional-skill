import unittest
from scripts.state_dynamics import aggregate_events, detect_consistent_direction, compare_fast_vs_slow_signal, flag_possible_regime_shift, build_competing_hypotheses


def event(i, direction=1, dimension='trust', month=1, episode=None, source='observed_behavior'):
    return dict(event_id=f'{month}-{dimension}-{i}', timestamp=f'2026-{month:02d}-{i+1:02d}T12:00:00Z',
                episode_id=episode or f'{month}-{i}', context_id=f'c{i%2}',
                dimension=dimension, direction=direction, weight=1, source_type=source)


class DynamicsTests(unittest.TestCase):
    def test_single_event_unknown(self):
        self.assertEqual(detect_consistent_direction([event(0)])['direction'],'unknown')

    def test_repeated_independent_events(self):
        self.assertEqual(detect_consistent_direction([event(i,-1) for i in range(10)])['direction'],'negative')

    def test_dependent_episodes_not_multiplied(self):
        a = aggregate_events([event(i,episode='one') for i in range(10)],30)['trust']
        self.assertEqual(a['episodes'],1)
        self.assertEqual(a['weighted_direction'],1)

    def test_equal_conflicting_episode_neutralized(self):
        a = aggregate_events([event(0,episode='one'),event(1,-1,episode='one')],30)['trust']
        self.assertEqual(a['weighted_direction'],0)

    def test_zero_weight_events_cannot_create_repetition(self):
        events=[event(0)]+[dict(event(i),weight=0) for i in range(1,5)]
        self.assertEqual(detect_consistent_direction(events)['direction'],'unknown')

    def test_symbolic_no_behavioural_weight(self):
        self.assertEqual(detect_consistent_direction([event(i,source='symbolic') for i in range(5)])['direction'],'unknown')

    def test_window_and_future_exclusion(self):
        a = aggregate_events([event(i) for i in range(10)],2,as_of='2026-01-05T12:00:00Z')['trust']
        self.assertEqual(a['episodes'],3)

    def test_fast_slow_conflict(self):
        r=compare_fast_vs_slow_signal([event(i,-1) for i in range(3)], [event(i) for i in range(8)])
        self.assertTrue(r['conflict'])
        self.assertIn('cannot overwrite',r['guidance'])

    def test_multidimensional_persistent_shift(self):
        b=[event(i,1,d,1) for i in range(4) for d in ('trust','warmth')]
        a=[event(i,-1,d,2) for i in range(4) for d in ('trust','warmth')]
        self.assertTrue(flag_possible_regime_shift(b,a)['possible_shift'])
        self.assertFalse(flag_possible_regime_shift(b,[event(0,-1,'trust',2)])['possible_shift'])

    def test_no_shift_for_one_dimension(self):
        self.assertFalse(flag_possible_regime_shift([event(i) for i in range(4)], [event(i,-1,month=2) for i in range(4)])['possible_shift'])

    def test_input_validation(self):
        with self.assertRaises(ValueError):
            aggregate_events([event(0),event(0)],30)
        with self.assertRaises(ValueError):
            aggregate_events([],0)
        with self.assertRaises(ValueError):
            detect_consistent_direction([dict(event(0),timestamp='2026-01-01')])
        with self.assertRaises(ValueError):
            detect_consistent_direction([event(0),event(1,dimension='warmth')])
        with self.assertRaises(ValueError):
            flag_possible_regime_shift([event(0)],[event(0)])

    def test_competing_models(self):
        self.assertEqual(len(build_competing_hypotheses('Why?', ['workload','distance'])['models']),2)
        with self.assertRaises(ValueError):
            build_competing_hypotheses('Why?', ['workload'])
