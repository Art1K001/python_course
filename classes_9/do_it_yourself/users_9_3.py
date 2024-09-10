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


user_1 = User("artur", "bilyak", 22, "volleyball", "arut")
user_1.describe_user()
user_1.greet_user()

user_2 = User("artem", "vaschuk", 41, "muay-thai", "skullbusher")
user_2.describe_user()
user_2.greet_user()

user_3 = User("max", "maka", 22, "music", "pussy hunter")
user_3.describe_user()
user_3.greet_user()
