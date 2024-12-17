#  11.3 – Funcionário: ==========================================================================================

class Employee():
    def __init__(self, nome, sobrenome, salario_anual):
        self.nome = nome
        self.sobrenome = sobrenome
        self.salario_anual = salario_anual
        
    def give_raise(self, aumento = 5000):
        self.salario_anual += aumento
        return self.salario_anual
    
    
        