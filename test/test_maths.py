import unittest
import numpy as np

from src.maths import Maths


class TestMaths(unittest.TestCase):

  def setUp(self):
    self.math = Maths()

  def test_friis_formula(self):
    gain=10
    watt=10
    wifi_wave_length = 0.12
    dist = self.math.friis_formula(watt=watt, gain=gain)
    true_dist = wifi_wave_length * 0.1 * gain / (4 * np.pi * np.sqrt(watt))
    self.assertEqual(dist, true_dist)

  def test_watt_to_db(self):
    watt = self.math.dbm_to_watt(dbm=0)
    self.assertEqual(watt, 0.001)

  def test_calc_circle_intersection(self):
    point_1, point_2 = self.math.\
      calc_circle_intersection(circle1=(1,1,2),circle2=(4,1,1))
    self.assertEqual((3.0, 1.0), point_1)
    self.assertEqual((3.0, 1.0), point_2)

  def test_check_and_modify(self):
    base_stations = {
      'B1x': 1,
      'B1y': 1,
      'B2x': 9,
      'B2y': 1,
      'B3x': 9,
      'B3y': 9,
      'B4x': 1,
      'B4y': 1
    }
    point = self.math.check_and_modify(xpoint=1, ypoint=9,
                                       base_stations=base_stations)
    self.assertEqual((1, 1), point)


if __name__ == "__main__":
  unittest.main()