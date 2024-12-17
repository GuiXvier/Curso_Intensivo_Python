import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
       self.nome = 'João'
       self.sobrenome = 'Moares'
       self.salario_anual = 5000
       
       self.meu_funcionario = Employee(self.nome, self.sobrenome, self.salario_anual)
         
    def test_give_default_raise(self):
        self.assertEqual(self.meu_funcionario.give_raise(), 10000)
    
    def test_give_custom_raise(self, custom_raise = 2000):
        self.assertEqual(self.meu_funcionario.give_raise(custom_raise), 7000)
    
if __name__ == '__main__':
    unittest.main()