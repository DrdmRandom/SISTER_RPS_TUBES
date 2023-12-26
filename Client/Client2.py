import socket
import tkinter as tk
from tkinter import messagebox

class RPSClientGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Rock, Paper, Scissors Game")
        self.master.configure(bg='#071952')  # Set the background color 

        self.choice_label = tk.Label(master, text="Welcome to the paper, rock, scissor game!\nChoose your move:", bg='#071952', fg='white')  # Set text and label color
        self.choice_label.pack()

        button_color = '#FFFFFF'  # Set button color
        self.rock_button = tk.Button(master, text="Rock", command=lambda: self.play_game("Rock"), bg=button_color)
        self.rock_button.pack()

        self.paper_button = tk.Button(master, text="Paper", command=lambda: self.play_game("Paper"), bg=button_color)
        self.paper_button.pack()

        self.scissors_button = tk.Button(master, text="Scissors", command=lambda: self.play_game("Scissors"), bg=button_color)
        self.scissors_button.pack()

    def play_game(self, choice):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            client.connect(('192.168.1.14', 55559))
            client.send(choice.encode('utf-8'))

            result = client.recv(1024).decode('utf-8')

            if "Winner" in result:  # Check if the result contains "Winner"
                messagebox.showinfo("Congratulations!", "Congratulations! You're the winner!", icon='info', foreground='#008000')  # Set congratulatory message color
            else:
                messagebox.showinfo("Game Result", f"Game Result: {result}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
        finally:
            client.close()

if __name__ == "__main__":
    root = tk.Tk()
    gui = RPSClientGUI(root)
    root.mainloop()
