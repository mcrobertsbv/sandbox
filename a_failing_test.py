# This is a failing test

import unittest

class TestKees(unittest.TestCase):
    def test_a_test(self):
        self.assertEqual(1, 2)

if __name__ == '__main__':
    unittest.main()
