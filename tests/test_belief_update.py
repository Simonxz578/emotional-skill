import math
import unittest
from scripts.belief_update import update_belief, effective_weight


class BeliefTests(unittest.TestCase):
    def test_support_increases(self):
        self.assertGreater(update_belief(.4, 'support', 1)['posterior'], .4)

    def test_contradiction_decreases(self):
        self.assertLess(update_belief(.6, 'contradict', 1)['posterior'], .6)

    def test_strength_and_discount(self):
        small = update_belief(.5, 'support', .5)['posterior']
        self.assertGreater(update_belief(.5, 'support', 2)['posterior'], small)
        self.assertLess(update_belief(.5, 'support', .5, .2)['posterior'], small)

    def test_known_bayes_factor(self):
        self.assertAlmostEqual(update_belief(.5, 'support', math.log(3))['posterior'], .75)

    def test_inverse_update(self):
        x = update_belief(.3, 'support', 2)['posterior']
        self.assertAlmostEqual(update_belief(x, 'contradict', 2)['posterior'], .3)

    def test_neutral_and_zero(self):
        self.assertAlmostEqual(update_belief(.7, 'neutral', 8)['posterior'], .7)
        self.assertAlmostEqual(update_belief(.7, 'support', 8, 0)['posterior'], .7)

    def test_extreme_stable_and_reusable(self):
        for direction in ('support', 'contradict'):
            x = update_belief(.5, direction, 1e308)['posterior']
            self.assertTrue(0 < x < 1)
            update_belief(x, 'neutral', 0)

    def test_invalid_inputs(self):
        for args in [(0, 'support', 1), (1, 'support', 1), (.5, 'bad', 1),
                     (.5, 'support', -1), (.5, 'support', 1, 2),
                     (math.nan, 'support', 1), (.5, 'support', math.inf),
                     (True, 'support', 1)]:
            with self.subTest(args=args), self.assertRaises(ValueError):
                update_belief(*args)

    def test_weight_product(self):
        factors = dict(directness=1, source_reliability=.5, repetition_factor=1,
                       behavioural_cost=1, context_relevance=1, baseline_specificity=.5, recency_factor=1)
        self.assertEqual(effective_weight(**factors), .25)
        factors['baseline_specificity'] = -1
        with self.assertRaises(ValueError):
            effective_weight(**factors)
