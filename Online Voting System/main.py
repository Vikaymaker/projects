import tkinter as tk
from tkinter import messagebox

class VotingSystem:
    def __init__(self, master):
        self.master = master
        self.master.title("Voting System")

        self.candidate1_label = tk.Label(master, text='Enter the 1st candidate name:')
        self.candidate1_label.pack()

        self.candidate1_entry = tk.Entry(master)
        self.candidate1_entry.pack()

        self.candidate2_label = tk.Label(master, text='Enter the 2nd candidate name:')
        self.candidate2_label.pack()

        self.candidate2_entry = tk.Entry(master)
        self.candidate2_entry.pack()

        self.candidate1_votes = 0
        self.candidate2_votes = 0

        self.voters_id = set(range(10))
        self.no_of_votes = len(self.voters_id)

        self.create_widgets()

    def create_widgets(self):
        self.voters_id_label = tk.Label(self.master, text='Enter your Voter id:')
        self.voters_id_label.pack()

        self.voters_id_entry = tk.Entry(self.master)
        self.voters_id_entry.pack()

        self.submit_voter_button = tk.Button(self.master, text='Submit Voter ID', command=self.submit_voter_id)
        self.submit_voter_button.pack()

    def submit_voter_id(self):
        try:
            voter_id = int(self.voters_id_entry.get())

            if voter_id in self.voters_id:
                messagebox.showinfo('Voter Eligibility', 'You are a voter.')
                self.voters_id.remove(voter_id)

                self.vote_options()
            else:
                messagebox.showerror('Voter Ineligibility', 'Sorry...You are not eligible to vote -_-')
                self.master.destroy()

        except ValueError:
            messagebox.showerror('Invalid Input', 'Please enter a valid numeric Voter ID.')

    def vote_options(self):
        self.vote_options_label = tk.Label(self.master, text='Vote Options:')
        self.vote_options_label.pack()

        self.candidate1_button = tk.Button(self.master, text=f'Vote {self.candidate1_entry.get()}', command=lambda: self.cast_vote(1))
        self.candidate1_button.pack()

        self.candidate2_button = tk.Button(self.master, text=f'Vote {self.candidate2_entry.get()}', command=lambda: self.cast_vote(2))
        self.candidate2_button.pack()

    def cast_vote(self, vote):
        if vote == 1:
            self.candidate1_votes += 1
            messagebox.showinfo('Vote Confirmation', f'Thank you for voting for {self.candidate1_entry.get()}!')
        elif vote == 2:
            self.candidate2_votes += 1
            messagebox.showinfo('Vote Confirmation', f'Thank you for voting for {self.candidate2_entry.get()}!')

        if not self.voters_id:
            self.display_results()

    def display_results(self):
        if self.candidate1_votes > self.candidate2_votes:
            percent = (self.candidate1_votes / self.no_of_votes) * 100
            messagebox.showinfo('Election Results', f'Congratulations! {self.candidate1_entry.get()} has won by {percent}%')
        elif self.candidate2_votes > self.candidate1_votes:
            percent = (self.candidate2_votes / self.no_of_votes) * 100
            messagebox.showinfo('Election Results', f'Congratulations! {self.candidate2_entry.get()} has won by {percent}%')

if __name__ == '__main__':
    root = tk.Tk()
    voting_system = VotingSystem(root)
    root.mainloop()
