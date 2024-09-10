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



