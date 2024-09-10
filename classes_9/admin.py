from user import User

class Privileges:
    def __init__(self, privileges=["can add post", "can delete post", "can ban user"]):
        self.privileges = privileges

    def show_privileges(self):
        for privileges in self.privileges:
            print(f"{privileges}")

"""Написати класс Адмін, що наслідує Юзер"""
class Admin(User):
    """додати атрибут Переваги, що міститиме список"""
    def __init__(self, first_name, last_name, age, hobby, nickname, ):
        super().__init__(first_name, last_name, age, hobby, nickname)
        self.privileges = Privileges()

    def show_privileges(self):
        for privileges in self.privileges:
            print(f"{privileges}")



