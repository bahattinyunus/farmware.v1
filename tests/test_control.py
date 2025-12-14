import unittest
from core.control.steering import SteeringController
from core.control.sprayer import SprayerController

class TestControl(unittest.TestCase):
    def test_steering_navigate_to(self):
        controller = SteeringController()
        waypoint = {"lat": 49.12345, "lng": -123.12345}
        self.assertIsNone(controller.navigate_to(waypoint))

    def test_sprayer_spray(self):
        sprayer = SprayerController(spray_rate=10, tank_capacity=200)
        self.assertTrue(sprayer.spray())
        self.assertEqual(sprayer.current_tank_level, 190)

    def test_sprayer_empty_tank(self):
        sprayer = SprayerController(spray_rate=10, tank_capacity=10)
        sprayer.spray()
        self.assertFalse(sprayer.spray())

if __name__ == "__main__":
    unittest.main()

#use the following command to test /// python -m unittest discover -s tests -p "test_*.py" /// or else you will get module error