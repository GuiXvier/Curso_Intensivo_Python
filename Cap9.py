# 1 =============================================================================================

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

# 2 ===============================================================================================
saborear = Restaurant("Saborear", "Pizzaria")
saborear.describe_restaurant()

sushiHouse = Restaurant("SushiHouse", "Oriental")
sushiHouse.describe_restaurant()

cancacoBurguer = Restaurant("Cangaço Burger", "Haburgueria")
cancacoBurguer.describe_restaurant()

# 3 =================================================================================================

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

# 9.8 =========================================================================================

class Privileges():
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        print("Aqui estao seus privilegios:")
        for privilege in self.privileges:
            print(privilege)

class Admin(User):
    def __init__(self, first_name, last_name, user_nick, user_email, user_passWord):
        super().__init__(first_name, last_name, user_nick, user_email, user_passWord)

    privileges = ["pode adicionar postagens", "pode deletar postagens", "pode banir usuários"]
    admin_privileges = Privileges(privileges)

    

# Criando uma instância de Admin com uma lista de privilégios
admin_user = Admin("João", "Silva", "adminjoao", "joao.silva@example.com", "senha123")
admin_user.admin_privileges.show_privileges()
    