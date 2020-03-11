import unittest
from . import Calc_Address

class TestCalcAdress(unittest.TestCase):
    def test_upper(self):
        self.assertEqual(Calc_Address("43.9496","4.81774","48.9123484","2.362144"),614.8746673909387)

if __name__ == '__main__':
    unittest.main()

##command : python -m unittest test.py

