import random
import tkinter as tk
from tkinter import messagebox


class NumberGuessingGame:
    def __init__(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 10
        self.root = tk.Tk()

        self.root.geometry("600x400")
        self.root.config(bg="#0C090A") #065569
        self.root.resizable(width=True, height=True)

        self.root.title("Number Guessing Game")

        self.label = tk.Label(self.root, text="Guess a number between 1 and 100:",font=("Times New Roman", 12))
        self.label.pack(pady=10)

        self.entry = tk.Entry(self.root)
        self.entry.pack(pady=5)

        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack(pady=5)

        self.attempts_label = tk.Label(self.root, text=f"Attempts left: {self.attempts}")
        self.attempts_label.pack(pady=5)

        self.check_button = tk.Button(self.root, text="Check", command=self.check_guess)
        self.check_button.pack(pady=5)

        self.play_again_button = tk.Button(self.root, text="Play Again", command=self.play_again)
        self.play_again_button.place(x=170, y=270)
        self.play_again_button.configure(state="disabled")

        self.exit_button = tk.Button(self.root, text="Exit Game", command=self.exit_game)
        self.exit_button.place(x=380, y=270)

    def check_guess(self):
        guess = self.entry.get()

        try:
            guess = int(guess)
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a valid number.")
            return

        if guess < 1 or guess > 100:
            messagebox.showerror("Error", "Number out of range. Please enter a number between 1 and 100.")
            return

        self.attempts -= 1
        self.attempts_label.config(text=f"Attempts left: {self.attempts}")

        if guess == self.secret_number:
            self.result_label.config(text="🎊Congratulations!🎊 You guessed the number.")
            self.disable_input()
            self.play_again_button.configure(state="normal")
        elif self.attempts == 0:
            self.result_label.config(text=f"Game Over😕. The number was {self.secret_number}.")
            self.disable_input()
            self.play_again_button.configure(state="normal")
        elif guess < self.secret_number:
            self.result_label.config(text="Too low!")
        else:
            self.result_label.config(text="Too high!")

        self.entry.delete(0, tk.END)

    def disable_input(self):
        self.entry.configure(state="disabled")
        self.check_button.configure(state="disabled")

    def play_again(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 10
        self.attempts_label.config(text=f"Attempts left: {self.attempts}")
        self.result_label.config(text="")
        self.enable_input()
        self.play_again_button.configure(state="disabled")

    def enable_input(self):
        self.entry.configure(state="normal")
        self.check_button.configure(state="normal")

    def exit_game(self):
        self.root.destroy()

    def run(self):
        self.root.mainloop()


game = NumberGuessingGame()
game.run()
