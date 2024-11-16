"""Conjunto de Classes para representar restaurantes"""

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"Olá, bem vindo ao {self.restaurant_name}, aqui nossa cozinha é {self.cuisine_type}")

    def open_restaurant(self):
        print("O restaurante esta aberto")

    number_served = 0

    def set_number_served(self, nPessoasServidas):
        self.number_served = nPessoasServidas

    def increment_number_served(self, novasPessoasAtendidas):
        self.number_served += novasPessoasAtendidas