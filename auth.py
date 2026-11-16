class Auth:
    def __init__(self):
        self.users = {}

    def register(self, username, password):
        if username in self.users:
            return False

        self.users[username] = password
        return True

    def login(self, username, password):
        if username in self.users and self.users[username] == password:
            return True

        return False


if __name__ == "__main__":
    auth = Auth()

    print("Регистрация:", auth.register("alex", "12345"))
    print("Вход:", auth.login("alex", "12345"))
    print("Неверный пароль:", auth.login("alex", "00000"))