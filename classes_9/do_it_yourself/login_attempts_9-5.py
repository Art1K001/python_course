class User:
    def __init__(self, name, last_name, age, hobby, nickname):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.hobby = hobby
        self.nickname = nickname
        self.login_attempts = 0

    def describe_user(self):
        print(f"\nThis user: {self.name.title()} {self.last_name.title()} have {self.age} years old and like {self.hobby.upper()}")

    def greet_user(self):
        print(f"\tWelcome {self.nickname.title()} in our comunity SpacePirates")

    def increment_login_attempts(self):
        self.login_attempts += 1
        print(f"\tUser tried to login: {self.login_attempts} time")

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f"\tНезнаю, що тут написати: {self.login_attempts}")

user_1 = User("artur", "bilyak", 22, "volleyball", "arut")
user_1.describe_user()
user_1.greet_user()
user_1.increment_login_attempts()
user_1.reset_login_attempts()

