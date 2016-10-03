import unittest
import fastest_way


class TestFastestWayMethods(unittest.TestCase):

    def test_get_distance(self):
        self.assertEqual(fastest_way.get_distance((34.234, 35.344), (36.6445, 45.8989)), 32.06810423863561)

    def test_get_closest_point(self):
        self.assertEqual(fastest_way.get_closest_point(
                                        (34.234, 35.344), [(36.6445, 45.8989), (56.3435, 45.545)]),
                         (36.6445, 45.8989))

    def test_main(self):
        self.assertEqual(fastest_way.main((34.234, 35.344), [(34.234, 35.344), (36.6445, 45.8989), (56.3435, 45.545)]),
                         [(34.234, 35.344), (36.6445, 45.8989), (56.3435, 45.545)])


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFastestWayMethods)
    unittest.TextTestRunner(verbosity=2).run(suite)