import os
import unittest
import xmlrunner

class InitialTests(unittest.TestCase):

    def test_failure(self):
        """Test what happens when a unittest fails"""
        self.assertTrue("apples" != "oranges", "You can't compare apples with oranges")

    def test_succeed(self):
        """Test what happens when a test succeeds"""
        self.assertTrue("apples" == "apples")

class MoreTests(unittest.TestCase):

    def test_succes_2(self):
        """Success"""
        self.assertEqual(1, 1)

    def test_fail_2(self):
        """Fail"""
        self.assertEqual(2, 2)

if __name__ == "__main__":
    unittest.main(testRunner = xmlrunner.XMLTestRunner(output=str(os.getcwd()) + "./tests/python_reports"))