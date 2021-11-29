import os
import unittest
import xmlrunner

print(os.getcwd)
class InitialTests(unittest.TestCase):

    def test_failure(self):
        """Test what happens when a unittest fails"""
        self.assertTrue("apples" == "oranges", "You can't compare apples with oranges")

    def test_succeed(self):
        """Test what happens when a test succeeds"""
        self.assertTrue("apples" == "apples")

with open(str(os.getcwd()) + '/testresults.xml', 'w+b') as output:
    unittest.main(testRunner = xmlrunner.XMLTestRunner(output=output))