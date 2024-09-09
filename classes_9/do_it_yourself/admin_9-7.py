class User:
    def __init__(self, first_name, last_name, age, hobby, nickname):
        self.name = first_name
        self.surname = last_name
        self.age = age
        self.hobby = hobby
        self.nickname = nickname

    def describe_user(self):
        print(f"\nThis user: {self.name.title()} {self.surname.title()} have {self.age} years old and like {self.hobby.upper()}")

    def greet_user(self):
        print(f"\tWelcome {self.nickname.title()} in our comunity SpacePirates")




"""Написати класс Адмін, що наслідує Юзер"""
class Admin(User):
    """додати атрибут Переваги, що міститиме список"""
    def __init__(self, first_name, last_name, age, hobby, nickname, privileges):
        super().__init__(first_name, last_name, age, hobby, nickname)
        self.privileges = privileges

    def show_privileges(self):
        for privileges in self.privileges:
            print(f"{privileges}")

admin = Admin("Artem", "Vaschuk", 41, "Muay Thai", "SkullBasher", ["can add post", "can delete post", "can ban user"])
print(f"{admin.name} {admin.surname}, he's {admin.age}")
print(f"Admin's nickname: {admin.nickname}")
admin.show_privileges()
print(f"and tell you the secret of his hobby {admin.hobby}, so it's best not to leak it")