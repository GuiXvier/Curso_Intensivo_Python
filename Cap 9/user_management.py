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