import unittest
from IDM import IDM, IDMAuto
from Constants import *
from LaneChange import LaneChange
from Cars import *
from copy import copy, deepcopy
from CarFactory import *
from Street import *

class MyTestCase(unittest.TestCase):

    def test_IDM(self):
        # using the initial value of Cars
        idm = IDM(112.65 / 3.6, 0.5, 3.0, 3.0, 1.5)
        self.assertAlmostEqual(idm.veq_table[4], 0.6543521725647148)
        self.assertAlmostEqual(idm.veq_table[20], 10.690092856310587)
        self.assertAlmostEqual(idm.veq_table[90], 28.89634917614212)

    def test_LaneChange(self):
        lc = LaneChange(0.2, 0.3)

    def test_Car(self):
        lc = LaneChange(0.2, 0.3)
        model = IDM(112.65 / 3.6, 0.5, 3.0, 3.0, 1.5)
        car1 = Car(0, 10, 0, model, lc, 5)
        car2 = copy(Car)

    def test_BCCar(self):
        model = IDM(112.65 / 3.6, 0.5, 3.0, 3.0, 1.5)
        bc = BCCar(0, 10, 0, model, 0)
        bc.lane_change = "fuck"
        self.assertEqual(bc.lane_change, None)

    def test_CarFactory(self):
        cf = CarFactory(0.5, 0.5)
        car = cf.create_vehicle(1,10,0)

    def test_Street(self):
        cf = CarFactory(0.5, 0.5)
        road = Street(3, 1000, cf)
        for i  in range(100):
            road.update(2)



if __name__ == '__main__':
    unittest.main()
