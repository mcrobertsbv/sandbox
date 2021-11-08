from hello_world import hello, goodbye
import unittest
import xmlrunner

class TestFinances(unittest.TestCase):
    def test_hello_output(self):
        self.assertEqual(hello(), 'Hello World')

    def test_goodbye_output(self):
        self.assertEqual(goodbye(), 'Goodbye')

if __name__ == '__main__':
    unittest.main(testRunner = xmlrunner.XMLTestRunner(output='reports'))
