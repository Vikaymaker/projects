import tkinter as tk
from tkinter import messagebox
import random

class NumberGuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Number Guessing Game")

        self.lower_label = tk.Label(master, text="Enter Lower Bound:")
        self.lower_label.pack()

        self.lower_entry = tk.Entry(master)
        self.lower_entry.pack()

        self.upper_label = tk.Label(master, text="Enter Upper Bound:")
        self.upper_label.pack()

        self.upper_entry = tk.Entry(master)
        self.upper_entry.pack()

        self.start_button = tk.Button(master, text="Start Game", command=self.start_game)
        self.start_button.pack()

    def start_game(self):
        try:
            lower_bound = int(self.lower_entry.get())
            upper_bound = int(self.upper_entry.get())

            if lower_bound >= upper_bound:
                messagebox.showerror("Error", "Upper bound must be greater than lower bound.")
                return

            target_number = random.randint(lower_bound, upper_bound)

            guess_label = tk.Label(self.master, text="Enter Your Guess:")
            guess_label.pack()

            guess_entry = tk.Entry(self.master)
            guess_entry.pack()

            guess_button = tk.Button(self.master, text="Submit Guess", command=lambda: self.check_guess(target_number, guess_entry.get()))
            guess_button.pack()

        except ValueError:
            messagebox.showerror("Error", "Please enter valid numeric values for bounds.")

    def check_guess(self, target_number, user_guess):
        try:
            user_guess = int(user_guess)
            if user_guess == target_number:
                messagebox.showinfo("Congratulations!", "You guessed the correct number!")
            elif user_guess < target_number:
                messagebox.showinfo("Try Again", "Too low! Try a higher guess.")
            else:
                messagebox.showinfo("Try Again", "Too high! Try a lower guess.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid numeric guess.")

if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()
