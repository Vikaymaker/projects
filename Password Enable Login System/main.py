import tkinter as tk
from tkinter import messagebox

class LoginSystem:
    def __init__(self, master):
        self.master = master
        self.master.title("Login System")

        self.username_label = tk.Label(master, text="Username:")
        self.username_label.pack()

        self.username_entry = tk.Entry(master)
        self.username_entry.pack()

        self.password_label = tk.Label(master, text="Password:")
        self.password_label.pack()

        self.password_entry = tk.Entry(master, show="*")
        self.password_entry.pack()

        self.login_button = tk.Button(master, text="Login", command=self.login)
        self.login_button.pack()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # In a real-world scenario, you would check the credentials against a database.
        # For simplicity, using hardcoded values here.
        valid_username = "user"
        valid_password = "pass123"

        if username == valid_username and password == valid_password:
            messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
        else:
            messagebox.showerror("Login failed", "wrong password Type again")

if __name__ == "__main__":
    root = tk.Tk()
    login_system = LoginSystem(root)
    root.mainloop()
