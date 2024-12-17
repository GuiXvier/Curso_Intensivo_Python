import unittest
import city_functions

#  11.1 – Cidade, país:

class TestCity(unittest.TestCase):
    def test_city_country(self):
        result = city_functions.cidade_pais('Santiago', 'Chile')
        self.assertEqual(result, 'Santiago, Chile')

if __name__ == '__main__':
    unittest.main()
    
# 11.2 – População: ==============================================================================================

class TestCity(unittest.TestCase):
    def test_city_country(self):
        result = city_functions.cidade_pais('Santiago', 'Chile')
        self.assertEqual(result, 'Santiago, Chile - ')
    
    def test_city_country_population(self):
        result = city_functions.cidade_pais('Santiago', 'Chile', population=5000000)
        self.assertEqual(result, 'Santiago, Chile - Population: 5000000')
        
# 11.3 – Funcionário: ==============================================================================================

"""
    Feito nos arquivos employee.py e test_employee.py
"""