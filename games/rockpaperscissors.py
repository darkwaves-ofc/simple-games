import random
from login import LoginController


class RockPaperScissors:
    @staticmethod
    def main(username, game):
        states = [
            "rock",
            "paper",
            "scissors"  # Corrected the typo
        ]
        print("Welcome to Rock Paper Scissors Game!")
        print("If you win you get 5 scores, and you can leave this game by entering 'quit()' command.")
        for index, state in enumerate(states):
            print(f"{index+1}: {state}")  # Adding 1 to index to start from 1
        while True:
            choice = input("\n\nSelect your choice (1-3): ")
            try:
                choice = int(choice)
                if 1 <= choice <= 3:
                    user_choice = states[choice - 1]
                    computer_choice = RockPaperScissors.get_computer_choice()
                    print("\nYou selected:", user_choice)
                    print("Computer selected:", computer_choice)
                    RockPaperScissors.check_winner(
                        user_choice, computer_choice, username, game["score"])
                else:
                    print("Invalid choice. Please select a number between 1 and 3.")
            except ValueError:
                if choice == "quit()":
                    return
                else:
                    print("Invalid input. Please enter a number or 'quit()' to exit.")

    @staticmethod
    def get_computer_choice():
        random_number = random.randint(1, 100)
        remainder = random_number % 3
        if remainder == 1:
            return "rock"
        elif remainder == 2:
            return "paper"
        else:
            return "scissors"

    @staticmethod
    def check_winner(user_choice, computer_choice, username, score):
        controller = LoginController()
        if user_choice == computer_choice:
            print(f"\nIt's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print(f"\nCongratulations! You win!")
            controller.save_user_score(username, score)
            # Add 5 marks for the user account
            # Add your logic here to update user's score
        else:
            print(f"\nSorry! You lose!")


if __name__ == "__main__":
    RockPaperScissors.main()
