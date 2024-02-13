import json


class LoginController:
    def __init__(self):
        self.users = []
        self.load_users()

    def load_users(self):
        try:
            with open("users.json", "r") as file:
                self.users = json.load(file)
        except FileNotFoundError:
            self.users = []

    def save_users(self):
        with open("users.json", "w") as file:
            json.dump(self.users, file)

    def register_user(self, username, password):
        for user in self.users:
            if user["username"] == username:
                print("Username already exists. Please choose a different one.")
                return False
        new_user = {"username": username, "password": password, "scores": 0}
        self.users.append(new_user)
        self.save_users()
        print("User registered successfully.")
        return True

    def login(self, username, password):
        for user in self.users:
            if user["username"] == username and user["password"] == password:
                print("Login successful!")
                return True
        print("Invalid username or password.")
        return False

    def get_user_score(self, username):
        # for user in self.users:
        #     if user["username"] == username:
        #         return user["scores"]
        try:
            with open("users.json", "r") as file:
                users = json.load(file)
        except FileNotFoundError:
            users = []
            return None
        for user in users:
            if user["username"] == username:
                return user["scores"]

    def save_user_score(self, username, score):
        for user in self.users:
            if user["username"] == username:
                user["scores"] = score + user["scores"]
                self.save_users()
                return True
