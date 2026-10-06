import math
import unittest
from scripts.information_metrics import entropy, normalized_entropy, kl_divergence, surprisal, qualitative_information_gain


class InformationTests(unittest.TestCase):
    def test_entropy_units_and_zeros(self):
        self.assertAlmostEqual(entropy([.5,.5]), math.log(2))
        self.assertAlmostEqual(entropy([.5,.5], base=2), 1)
        self.assertEqual(entropy([0,1]), 0)

    def test_normalized_entropy(self):
        self.assertAlmostEqual(normalized_entropy([.25]*4), 1)
        self.assertEqual(normalized_entropy([1]), 0)

    def test_kl_direction_and_zero(self):
        self.assertEqual(kl_divergence([1,0],[1,0]), 0)
        self.assertEqual(kl_divergence([1,0],[0,1]), math.inf)
        self.assertNotAlmostEqual(kl_divergence([.8,.2],[.5,.5]), kl_divergence([.5,.5],[.8,.2]))

    def test_surprisal(self):
        self.assertEqual(surprisal(0), math.inf)
        self.assertEqual(surprisal(1), 0)
        self.assertAlmostEqual(surprisal(.25, base=2), 2)

    def test_positive_revision_can_raise_entropy(self):
        r = qualitative_information_gain([.99,.01],[.5,.5])
        self.assertGreater(r['kl_nats'], 0)
        self.assertGreater(r['entropy_change_nats'], 0)

    def test_equal_distributions_no_gain(self):
        self.assertEqual(qualitative_information_gain([.5,.5],[.5,.5])['kl_nats'], 0)

    def test_invalid_distributions(self):
        for p in [[], [.2,.2], [-1,2], [math.nan,1], [True,0]]:
            with self.subTest(p=p), self.assertRaises(ValueError):
                entropy(p)
        with self.assertRaises(ValueError):
            kl_divergence([1],[.5,.5])
        for p in [-.1,1.1,math.nan]:
            with self.assertRaises(ValueError):
                surprisal(p)
        with self.assertRaises(ValueError):
            entropy([1],base=1)
