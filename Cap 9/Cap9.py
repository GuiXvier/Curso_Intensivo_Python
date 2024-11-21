# 9.1 =============================================================================================

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"Olá, bem vindo ao {self.restaurant_name}, aqui nossa cozinha é {self.cuisine_type}")

    def open_restaurant(self):
        print("O restaurante esta aberto")

saborear = Restaurant("Saborear", "Pizzaria")

saborear.describe_restaurant()
saborear.open_restaurant()

# 9.2 ===============================================================================================
saborear = Restaurant("Saborear", "Pizzaria")
saborear.describe_restaurant()

sushiHouse = Restaurant("SushiHouse", "Oriental")
sushiHouse.describe_restaurant()

cancacoBurguer = Restaurant("Cangaço Burger", "Haburgueria")
cancacoBurguer.describe_restaurant()

# 9.3 =================================================================================================

class User:
    def __init__(self, first_name, last_name, user_nick, user_email, user_passWord):
        self.first_name = first_name
        self.last_name = last_name
        self.user_nick = user_nick
        self.user_email = user_email
        self.user_passWord = user_passWord

    def describe_user(self):
        print(f"Olá me chamo {self.first_name}, atendo pelo nick {self.user_nick} se", end=" ")
        print(f"quiser entra em contato comigo, aqui esta meu Email: {self.user_email}")

    def greet_user(self, saudacao):
        print(saudacao)

# Instância 1
user1 = User("Alice", "Silva", "AliS", "alice.silva@example.com", "senha123")
user1.describe_user()
user1.greet_user("Bem-vinda, Alice!\n")

# Instância 2
user2 = User("Bruno", "Souza", "BrunoS", "bruno.souza@example.com", "senha456")
user2.describe_user()
user2.greet_user("Olá, Bruno!\n")

# Instância 3
user3 = User("Carla", "Fernandes", "CarlaF", "carla.fernandes@example.com", "senha789")
user3.describe_user()
user3.greet_user("Seja bem-vinda, Carla!\n")

# Instância 4
user4 = User("Daniel", "Costa", "DanC", "daniel.costa@example.com", "senha321")
user4.describe_user()
user4.greet_user("Oi, Daniel!\n")

# Instância 5
user5 = User("Eduarda", "Moraes", "DudaM", "eduarda.moraes@example.com", "senha654")
user5.describe_user()
user5.greet_user("Olá, Eduarda!\n")

# Instância 6
user6 = User("Felipe", "Santos", "FeliS", "felipe.santos@example.com", "senha987")
user6.describe_user()
user6.greet_user("Bem-vindo, Felipe!\n")

# Instância 7
user7 = User("Gabriela", "Almeida", "GabiA", "gabriela.almeida@example.com", "senha147")
user7.describe_user()
user7.greet_user("Oi, Gabriela!\n")

# Instância 8
user8 = User("Henrique", "Oliveira", "HenryO", "henrique.oliveira@example.com", "senha258")
user8.describe_user()
user8.greet_user("Bem-vindo, Henrique!\n")

# Instância 9
user9 = User("Isabela", "Lima", "IsaL", "isabela.lima@example.com", "senha369")
user9.describe_user()
user9.greet_user("Seja bem-vinda, Isabela!\n")

# Instância 10
user10 = User("João", "Martins", "JoaoM", "joao.martins@example.com", "senha741")
user10.describe_user()
user10.greet_user("Olá, João!\n")

# 9.4 ===============================================================================================

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

restaurante = Restaurant("Restaurante", "Pizzaria")

print(f'Numero de pessoas servidas: {restaurante.number_served}')

restaurante.number_served = 100

print(f'Numeros de pessoas servidas hoje: {restaurante.number_served}')

restaurante.set_number_served(40)

print(f'Numeros de pessoas servidas pelo metodo: {restaurante.number_served}')

restaurante.increment_number_served(30)

print(f'Novas pessoas atendidas: {restaurante.number_served}')

# 9.5 =========================================================================================

class User:
    def __init__(self, first_name, last_name, user_nick, user_email, user_passWord):
        self.first_name = first_name
        self.last_name = last_name
        self.user_nick = user_nick
        self.user_email = user_email
        self.user_passWord = user_passWord

    def describe_user(self):
        print(f"Olá me chamo {self.first_name}, atendo pelo nick {self.user_nick} se", end=" ")
        print(f"quiser entra em contato comigo, aqui esta meu Email: {self.user_email}")

    def greet_user(self, saudacao):
        print(saudacao)

    login_attempts = 0

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

alice = User("Alice", "Silva", "AliS", "alice.silva@example.com", "senha123")

alice.increment_login_attempts()
alice.increment_login_attempts()
alice.increment_login_attempts()
alice.increment_login_attempts()
alice.increment_login_attempts()

print(f'Alice tentou logar: {alice.login_attempts} vezes')

alice.reset_login_attempts()

print(f'Resetei as tentativas de Login: {alice.login_attempts}')

# 9.6 =========================================================================================

class Sorveteria(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def saboresSorvete(self):
        print("Nos temos os seguintes sabores: ")
        i = 1
        for sabor in self.flavors:
            print(f'{i}º: {sabor}')
            i += 1

estrela = Sorveteria("Estrela", "Lanchonete", ['Bariloche', 'Chocolate', 'Menta'])
estrela.saboresSorvete()

# 9.7 =========================================================================================

class Admin(User):
    def __init__(self, first_name, last_name, user_nick, user_email, user_passWord, privileges):
        super().__init__(first_name, last_name, user_nick, user_email, user_passWord)
        self.privileges = privileges

    def show_privileges(self):
        print("Aqui estao seus privilegios:")
        for privilege in self.privileges:
            print(privilege)

# Criando uma instância de Admin com uma lista de privilégios
admin_user = Admin("João", "Silva", "adminjoao", "joao.silva@example.com", "senha123", 
                   ["pode adicionar postagens", "pode deletar postagens", "pode banir usuários"])

admin_user.show_privileges()

# 9.8 ==============================================================================================

class Privileges():
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        print("Aqui estao seus privilegios:")
        for privilege in self.privileges:
            print(privilege)

class Admin(User):
    def __init__(self, first_name, last_name, user_nick, user_email, user_passWord, privileges):
        super().__init__(first_name, last_name, user_nick, user_email, user_passWord)
        self.privileges = Privileges(privileges)

# Criando uma instância de Admin com uma lista de privilégios
admin_user = Admin("João", "Silva", "adminjoao", "joao.silva@example.com", "senha123",
                   ["pode adicionar postagens", "pode deletar postagens", "pode banir usuários"])

admin_user.privileges.show_privileges()

# 9.9 ==========================================================================================

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        print("This cas has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def fill_gas_tank(self):
        print("This car needs a gas tank!")

class Battery:
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range) + \
                  " miles on a full charge."
        print(message)
    
    def upgrade_battery(self):
       if self.battery_size != 85:
           self.battery_size = 85

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        print("This car doesn\'t need a gas tank!")

tesla = ElectricCar("Tesla", "CyberTruck", "2022")

tesla.battery.get_range()
tesla.battery.upgrade_battery()
tesla.battery.get_range()

# 9.10 =========================================================================================

from restaurant import Restaurant

estrelaSorveteria = Restaurant("Estrela Sorveteria", "Sorveteria")
estrelaSorveteria.describe_restaurant()

#9.11 ===========================================================================================

from user_management import Admin

admin_user = Admin("Maria", "Oliveira", "adminmaria", "maria.oliveira@example.com", "senha456",
                   ["pode editar postagens", "pode bloquear usuários", "pode acessar relatórios"])

admin_user.privileges.show_privileges()

#9.12 ===========================================================================================

from privilegesAdmin import Admin

admin_user2 = Admin("Carlos", "Santos", "admincarlos", "carlos.santos@example.com", "senha789",
                    ["pode criar usuários", "pode redefinir senhas", "pode moderar comentários"])

admin_user2.privileges.show_privileges()

# 9.13 ===============================================================================================
from collections import OrderedDict

ordered_glossario = OrderedDict()
ordered_glossario['Chapter_1'] = 'numbers'
ordered_glossario['Chapter_2'] = 'names_cases'
ordered_glossario['Chapter_3'] = 'list'

for key, value in ordered_glossario.items():
    print(f'At {key} was studied {value}')

# 9.14 ===============================================================================================
from random import randint

class Die:
    def __init__(self, sides = 6):
        self.sides = sides
    
    def roll_die(self):
        val = randint(1, self.sides)
        print(f'This is a d{self.sides} and you rolled: {val}')
    
d6 = Die()
d10 = Die(10)
d20 = Die(20)

for i in range(d6.sides + 1):
    d6.roll_die()

for i in range(d10.sides + 1):
    d10.roll_die()

for i in range(d20.sides + 1):
    d20.roll_die()

# 9.15 ================================================================================================

#PESQUISA