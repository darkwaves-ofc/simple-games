from games import RockPaperScissors
from login import LoginController
from games import HangMan


def main():
    controller = LoginController()
    logged_in_user = None

    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            if controller.register_user(username, password):
                print("User registered successfully.")
        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")
            if controller.login(username, password):
                print("Login successful!")
                logged_in_user = username
                # Start game loop after successful login
                play_game(controller, logged_in_user)
        elif choice == "3":
            print("Exiting program.")
            return
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


def play_game(controller, username):
    allGames = [
        {"id": "1", "title": "Rock Paper Scissors",
            "game": RockPaperScissors.main, "score": 5},
        {"id": "2", "title": "HangMan", "game": HangMan.hangman, "score": 5}
    ]

    while True:
        print(f"\nWelcome, {username}!")
        print(f"Your score: {controller.get_user_score(username)}")

        print('\nOur All Games! Select the number of it to select.')
        for game in allGames:
            print(game["id"], ":", game["title"])

        input_no = input("\nYour Choice: ")
        if not input_no:
            return False
        try:
            input_no = int(input_no)
            if 1 <= input_no <= len(allGames):
                selected_game = allGames[input_no - 1]["game"]
                selected_game(username, allGames[input_no - 1])
            else:
                print(
                    "Invalid choice. Please select a number between 1 and", len(allGames))
        except ValueError:
            print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    main()
