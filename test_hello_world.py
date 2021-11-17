from hello_world import hello, goodbye
import unittest
import xmlrunner
import os

class TestHelloWorld(unittest.TestCase):
    def test_hello_output(self):
        self.assertEqual(hello(), 'Hello World')

    def test_goodbye_output(self):
        self.assertEqual(goodbye(), 'Goodbye')

if __name__ == '__main__':
    # test using gitlab environment variable:
    print('testvariable from gitlab cicd has value: ' + os.environ['TESTVARIABLE'])

    # Run tests
    unittest.main(testRunner = xmlrunner.XMLTestRunner(output='reports'))
    
