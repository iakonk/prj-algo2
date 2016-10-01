import unittest
import justify_string


class TestFindLongestSubstMethods(unittest.TestCase):

    def test_count_matches(self):
        self.assertEqual(justify_string.count_matches('world', 'wolf'),
                         [[0, 0, 0, 0, 0],
                          [0, 1, 1, 1, 1],
                          [0, 1, 2, 2, 2],
                          [0, 1, 2, 2, 2],
                          [0, 1, 2, 3, 3],
                          [0, 1, 2, 3, 3]])

        self.assertEqual(justify_string.count_matches(' world', ' wolf'),
                         [[0, 0, 0, 0, 0],
                          [0, 1, 1, 1, 1],
                          [0, 1, 2, 2, 2],
                          [0, 1, 2, 2, 2],
                          [0, 1, 2, 3, 3],
                          [0, 1, 2, 3, 3]])

    def test_get_longest_subst(self):
        self.assertEqual(justify_string.test_get_longest_subst(' world', ' wolf',
                          [[0, 0, 0, 0, 0],
                          [0, 1, 1, 1, 1],
                          [0, 1, 2, 2, 2],
                          [0, 1, 2, 2, 2],
                          [0, 1, 2, 3, 3],
                          [0, 1, 2, 3, 3]], 5, 4), ' ')

    def test_get_longest_subst(self):
        self.assertEqual(justify_string.get_longest_subst(' world', ' wolf',
                          [[0, 0, 0, 0, 0],
                          [0, 1, 1, 1, 1],
                          [0, 1, 2, 2, 2],
                          [0, 1, 2, 2, 2],
                          [0, 1, 2, 3, 3],
                          [0, 1, 2, 3, 3]], 4, 3), 'l')

    def test_get_longest_subst(self):
        self.assertEqual(justify_string.get_longest_subst(' world', ' wolf',
                          [[0, 0, 0, 0, 0],
                          [0, 1, 1, 1, 1],
                          [0, 1, 2, 2, 2],
                          [0, 1, 2, 2, 2],
                          [0, 1, 2, 3, 3],
                          [0, 1, 2, 3, 3]], 3, 2), 'o')

    def test_get_longest_subst(self):
        self.assertEqual(justify_string.get_longest_subst(' world', ' wolf',
                          [[0, 0, 0, 0, 0],
                          [0, 1, 1, 1, 1],
                          [0, 1, 2, 2, 2],
                          [0, 1, 2, 2, 2],
                          [0, 1, 2, 3, 3],
                          [0, 1, 2, 3, 3]], 2, 1), 'w')


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFindLongestSubstMethods)
    unittest.TextTestRunner(verbosity=4).run(suite)