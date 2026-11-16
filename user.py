class User:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def show_info(self):
        print("Имя:", self.name)
        print("Возраст:", self.age)
        print("Электронная почта:", self.email)


if __name__ == "__main__":
    user = User("Александр", 20, "user@example.com")
    user.show_info()