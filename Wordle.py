import random
import tkinter as tk
from tkinter import messagebox

WORDS = [
    # August 4- 2024 
    "LOWER", "ENSUE", "ANVIL", "MACAW", "SAUCY", "OUNCE", "MEDIC", "SCONE", "SKIFF", "NEIGH", "SHORE", "ACORN",
    "BRACE", "STORM", "LANKY", "METER", "DELAY", "MULCH", "BRUTE", "LEECH", "FILET", "SKATE", "STAKE", "CROWN",
    "LITHE", "FLUNK", "KNAVE", "SPOUT",
    # random
    "APPLE", "BANJO", "CRISP", "DANCE", "EAGLE", "FABLE", "GHOST", "HONEY", "IVORY", "JOKER", "KAYAK", "LUNCH",
    "MANGO", "NINJA", "OCEAN", "PIZZA", "QUILT", "ROBOT", "SALAD", "TANGO", "ULTRA", "VIVID", "WALTZ", "XENON", 
    "YACHT", "ZEBRA", "ALIVE", "BLAZE", "CANDY", "DELTA", "EPOCH", "FROST", "GLASS", "HUMAN", "INDEX", "JELLY", 
    "KNOCK", "LEMON", "MUSIC", "NOBLE", "OASIS", "PRISM", "QUARK", "RHYME", "SWEET", "TIGER", "UNITY", "VIRUS", 
    "WISER", "XENIA", "YOUTH", "LIGHT", "MORAL", "NURSE", "OFFER", "PRIDE", "QUOTA", "RIVAL", "SCOPE", "TROOP", 
    "UNITY", "VIVID", "WORRY", "XENON", "YIELD", "ZEBRA"

]

class Wordle:
    def __init__(self, root):

        self.root = root
        self.root.title("Wordle")
        self.root.geometry("420x620")

        self.root.resizable(False, False)

        self.secret_word = random.choice(WORDS)

        self.current_row = 0
        self.max_guesses = 6

        self.game_over = False

        title_label = tk.Label(self.root, text="Wordle", font=("Arial", 22, "bold"))
        title_label.pack(pady=(16, 6))

        self.board = []

        for row_index in range(self.max_guesses):
            row = []
            frame = tk.Frame(self.root)
            frame.pack(pady=2)

            for col_index in range(5):
                label = tk.Label(

                    frame,

                    text="",
                    width=4,
                    height=2,
                    font=("Arial", 18, "bold"),
                    borderwidth=2,
                    relief="solid",
                    bg="#d9d9d9",

                )

                label.grid(row=row_index, column=col_index, padx=2, pady=2)

                row.append(label)

            self.board.append(row)

        input_frame = tk.Frame(self.root)
        input_frame.pack(pady=(18, 8))

        self.guess_var = tk.StringVar()
        self.guess_entry = tk.Entry(

            input_frame,

            textvariable=self.guess_var,
            width=12,
            font=("Arial", 16),
            justify="center",
        )

        self.guess_entry.grid(row=0, column=0, padx=(0, 8))

        self.guess_entry.bind("<Return>", lambda event: self.submit_guess())

        self.submit_button = tk.Button(input_frame, text="Guess", command=self.submit_guess, font=("Arial", 12, "bold"))

        self.submit_button.grid(row=0, column=1)

        self.status_label = tk.Label(self.root, text="Enter a 5-letter word.", font=("Arial", 11), fg="#333333")

        self.status_label.pack(pady=(4, 14))

        self.new_game_button = tk.Button(self.root, text="New Game", command=self.reset_game, font=("Arial", 11))

        self.new_game_button.pack()

    def get_feedback(self, guess, target):

        result = ["X"] * 5

        remaining = {}

        for index, letter in enumerate(target):

            if guess[index] == letter:

                result[index] = "G"

            else:

                remaining[letter] = remaining.get(letter, 0) + 1

        for index, letter in enumerate(guess):

            if result[index] == "G":

                continue

            if letter in remaining and remaining[letter] > 0:

                result[index] = "Y"

                remaining[letter] -= 1

        return result

    def update_row(self, row_index, guess, feedback):

        colors = {

            "G": "#6aaa64",
            "Y": "#c9b458",
            "X": "#787c7e",

        }

        for col_index, letter in enumerate(guess):

            label = self.board[row_index][col_index]

            label.config(text=letter, bg=colors[feedback[col_index]], fg="white")

    def submit_guess(self):

        if self.game_over:

            return

        guess = self.guess_var.get().strip().upper()

        if len(guess) != 5 or not guess.isalpha():

            self.status_label.config(text="Please enter a valid 5-letter word.")

            return

        feedback = self.get_feedback(guess, self.secret_word)

        self.update_row(self.current_row, guess, feedback)

        if guess == self.secret_word:

            self.status_label.config(text=f"You solved it in {self.current_row + 1} guesses!")
            self.game_over = True
            self.guess_entry.config(state="disabled")
            self.submit_button.config(state="disabled")

            return

        self.current_row += 1

        if self.current_row >= self.max_guesses:

            self.status_label.config(text=f"You lost. The word was {self.secret_word}.")
            self.game_over = True
            self.guess_entry.config(state="disabled")
            self.submit_button.config(state="disabled")

            return

        self.status_label.config(text=f"Guess {self.current_row + 1} of {self.max_guesses}")

        self.guess_var.set("")

    def reset_game(self):
        self.secret_word = random.choice(WORDS)
        self.current_row = 0
        self.game_over = False

        for row in self.board:

            for label in row:

                label.config(text="", bg="#d9d9d9", fg="black")

        self.guess_var.set("")
        self.guess_entry.config(state="normal")
        self.submit_button.config(state="normal")
        self.status_label.config(text="Enter a 5-letter word.")

if __name__ == "__main__":

    root = tk.Tk()
    app = Wordle(root)
    root.mainloop()
