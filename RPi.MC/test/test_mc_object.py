import unittest
from raspi_mc.magnetic_contact import MC


class MCObjectTestCase(unittest.TestCase):
    def setUp(self):
        self.mc = MC()

    def tearDown(self):
        self.mc = None

    def test_constants(self):
        self.assertEqual(self.mc.door_open, 1)
        self.assertEqual(self.mc.door_closed, 0)

    def test_get_door_state(self):
        self.mc.door_state = 1
        self.assertEqual(self.mc.get_door_state(), 'Door is open')
        self.mc.door_state = 0
        self.assertEqual(self.mc.get_door_state(), 'Door is closed')


if __name__ == '__main__':
    unittest.main()
