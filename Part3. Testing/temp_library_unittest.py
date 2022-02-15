import unittest
from temp_library import reverse_string


class TestReverseString(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(reverse_string(''), '')

    def test_odd_len(self):
        self.assertEqual(reverse_string('abc'), 'cba')
        self.assertEqual(reverse_string('qwert'), 'trewq')
        self.assertEqual(reverse_string('abcxdba'), 'abdxcba')

    def test_wrong_type(self):
        with self.assertRaises(TypeError):
            reverse_string(1)
        with self.assertRaises(TypeError):
            reverse_string([1, 2, 3])


if __name__ == '__main__':
    unittest.main()

