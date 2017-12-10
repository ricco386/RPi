import unittest
from test_doorman_object import DoormanObjectTestCase

def create_suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(DoormanObjectTestCase())
    return test_suite


if __name__ == '__main__':
   suite = create_suite()

   runner=unittest.TextTestRunner()
   runner.run(suite)

