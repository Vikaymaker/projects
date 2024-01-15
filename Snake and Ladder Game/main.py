import tkinter as tk
import random

class SnakeAndLadderGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Snake and Ladder Game")

        self.canvas = tk.Canvas(master, width=400, height=400)
        self.canvas.pack()

        self.draw_board()

        self.player_position = 1

        self.roll_button = tk.Button(master, text="Roll Dice", command=self.roll_dice)
        self.roll_button.pack()

        self.info_label = tk.Label(master, text="Roll the dice to start the game!")
        self.info_label.pack()

    def draw_board(self):
        for i in range(1, 101):
            row, col = self.get_row_col(i)
            x = (col - 1) * 40
            y = 360 - (row - 1) * 40
            self.canvas.create_rectangle(x, y, x + 40, y + 40, outline="black", fill="white")
            self.canvas.create_text(x + 20, y + 20, text=str(i), font=("Helvetica", 10), fill="black")

    def get_row_col(self, position):
        row = (position - 1) // 10 + 1
        col = (position - 1) % 10 + 1
        if row % 2 == 0:
            col = 10 - col + 1
        return row, col

    def roll_dice(self):
        dice_value = random.randint(1, 6)
        self.info_label.config(text=f"You rolled a {dice_value}!")

        self.move_player(dice_value)

    def move_player(self, steps):
        new_position = self.player_position + steps
        if new_position <= 100:
            self.player_position = new_position
            self.update_player_position()

            if new_position in ladder_positions:
                self.player_position = ladder_positions[new_position]
                self.update_player_position()
                self.info_label.config(text="Climbed a ladder! 🚀")

            elif new_position in snake_positions:
                self.player_position = snake_positions[new_position]
                self.update_player_position()
                self.info_label.config(text="Encountered a snake! 🐍")

            if new_position == 100:
                self.info_label.config(text="Congratulations! You won!")

    def update_player_position(self):
        row, col = self.get_row_col(self.player_position)
        x = (col - 1) * 40 + 20
        y = 360 - (row - 1) * 40 - 20
        self.canvas.create_oval(x - 10, y - 10, x + 10, y + 10, outline="blue", fill="blue")

# Snake and ladder positions
ladder_positions = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}
snake_positions = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}

if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeAndLadderGame(root)
    root.mainloop()
