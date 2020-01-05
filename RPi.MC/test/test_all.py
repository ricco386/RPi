import unittest
from .test_mc_object import MCObjectTestCase

def create_suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(MCObjectTestCase())
    return test_suite


if __name__ == '__main__':
   suite = create_suite()

   runner=unittest.TextTestRunner()
   runner.run(suite)
