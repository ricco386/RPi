import unittest
from rpi_doorman.rpi_doorman import Doorman

class DoormanObjectTestCase(unittest.TestCase):
    def setUp(self):
        self.d = Doorman()

    def tearDown(self):
        self.d = None

    def test_constants(self):
        self.assertEqual(self.d.door_open, 1)
        self.assertEqual(self.d.door_closed, 0)

    def test_get_door_state(self):
        self.d.door_state = 1
        self.assertEqual(self.d.get_door_state(), 'Door is open')
        self.d.door_state = 0
        self.assertEqual(self.d.get_door_state(), 'Door is closed')


if __name__ == '__main__':
    unittest.main()
