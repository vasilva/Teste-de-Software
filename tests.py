import unittest
from data import Data
from hora import Hora

class TestData(unittest.TestCase):
      
    def test_data_valida(self):
        dt = Data(2, 3, 2004)
        self.assertTrue(dt.valido())

if __name__ == "__main__":
    unittest.main()