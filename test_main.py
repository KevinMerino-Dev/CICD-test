import unittest
from datetime import datetime
from main import dias_restantes

class TestMain(unittest.TestCase):
    
    def test_calculate_days_left(self):
        # Calcular el número de días restantes hasta el fin de año
        today = datetime.now()
        end_year = datetime(today.year, 12, 31)
        expected_result = (end_year - today).days  # Calcular el valor esperado

        # Comparar el valor calculado por la función con el valor esperado
        self.assertEqual(dias_restantes(), expected_result)


if __name__ == '__main__':
    try:
        unittest.main(exit=False)
    except SystemExit:
        pass
    print(f"No hay errores y faltan {dias_restantes()} días")