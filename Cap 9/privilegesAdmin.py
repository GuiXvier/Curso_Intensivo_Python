from user import User

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