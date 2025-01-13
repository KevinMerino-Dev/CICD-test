import unittest
from main import dias_restantes

class TestMain(unittest.TestCase):
    def test_calculate_days_left(self):
        self.assertEqual(dias_restantes(), <resultado esperado>)

if __name__ == '__main__':
    unittest.main()