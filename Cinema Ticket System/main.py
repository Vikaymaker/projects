import tkinter as tk
from tkinter import messagebox

class CinemaTicketSystem:
    def __init__(self, master):
        self.master = master
        self.master.title("Cinema Ticket System")

        self.movies = ["LEO", "JAILER", "AYALAN"]
        self.selected_movie = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Movie Selection
        movie_label = tk.Label(self.master, text="Select Movie:")
        movie_label.grid(row=0, column=0, pady=10)

        movie_menu = tk.OptionMenu(self.master, self.selected_movie, *self.movies)
        movie_menu.grid(row=0, column=1, pady=10)

        # Number of Tickets
        tickets_label = tk.Label(self.master, text="Number of Tickets:")
        tickets_label.grid(row=1, column=0, pady=10)

        self.tickets_entry = tk.Entry(self.master)
        self.tickets_entry.grid(row=1, column=1, pady=10)

        # Calculate Button
        calculate_button = tk.Button(self.master, text="Calculate Total", command=self.calculate_total)
        calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

    def calculate_total(self):
        try:
            selected_movie = self.selected_movie.get()
            num_tickets = int(self.tickets_entry.get())

            if num_tickets <= 0:
                messagebox.showerror("Error", "Number of tickets must be greater than zero.")
                return

            # Ticket Prices (replace with actual prices)
            movie_prices = {"LEO": 100, "JAILER": 110, "AYALAN": 130}

            if selected_movie not in movie_prices:
                messagebox.showerror("Error", "Invalid movie selection.")
                return

            ticket_price = movie_prices[selected_movie]
            total_cost = num_tickets * ticket_price

            messagebox.showinfo("Total Cost", f"Total Cost for {num_tickets} tickets to {selected_movie}: ${total_cost}")

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number for the number of tickets.")

if __name__ == "__main__":
    root = tk.Tk()
    cinema_ticket_system = CinemaTicketSystem(root)
    root.mainloop()
