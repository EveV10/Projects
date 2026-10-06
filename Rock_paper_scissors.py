# rock paper scissors game
import random
import tkinter as tk

class RockPaperScissors:
    def __init__(self):
        self.choices = ["rock", "paper", "scissors"]

    def get_computer_choice(self):
        return random.choice(self.choices)

    def determine_winner(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            return "It's a tie!"
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "paper" and computer_choice == "rock") or \
             (player_choice == "scissors" and computer_choice == "paper"):
            return "You win!"
        else:
            return "Computer wins!"

    def play(self):
        root = tk.Tk()
        root.title("Rock, Paper, Scissors")
        root.geometry("700x500")
        root.configure(bg="SystemButtonFace")

        tk.Label(
            root,
            text="Rock, Paper, Scissors",
            font=("Arial", 20),
        ).pack(pady=(70, 25))

        tk.Label(root, text="Choose your move:", font=("Arial", 14)).pack(pady=(0, 20))

        buttons = tk.Frame(root)
        buttons.pack(padx=20)

        result_label = tk.Label(
            root,
            text="Pick a button to play!",
            font=("Arial", 14),
            justify="center",
            width=38,
            height=5,
        )
        result_label.pack(padx=30, pady=40)

        def choose(player_choice):
            computer_choice = self.get_computer_choice()
            result = self.determine_winner(player_choice, computer_choice)
            result_label.config(
                text=f"You chose: {player_choice.title()}\n"
                     f"Computer chose: {computer_choice.title()}\n\n{result}"
            )

        for choice in self.choices:
            tk.Button(
                buttons,
                text=choice.title(),
                width=12,
                height=2,
                font=("Arial", 14),
                command=lambda selected=choice: choose(selected),
            ).pack(side=tk.LEFT, padx=5)

        root.mainloop()


if __name__ == "__main__":
    RockPaperScissors().play()
