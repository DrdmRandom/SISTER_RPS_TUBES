import socket
import threading
import tkinter as tk
from tkinter import messagebox
from tkinter.font import Font
from PIL import Image, ImageTk

def send_choice(choice):
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(('192.168.1.14', 55559))  # Sesuaikan dengan alamat IP dan port server Anda
        client.send(choice.encode('utf-8'))
        result = client.recv(1024).decode('utf-8')
        messagebox.showinfo("Game Result", result)
        client.close()
    except ConnectionError:
        messagebox.showerror("Connection Error", "Could not connect to the server.")

def on_button_click(choice, window):
    threading.Thread(target=send_choice, args=(choice, window)).start()

def main():
    window = tk.Tk()
    window.title("Rock Paper Scissors Game")
    window.geometry('360x200')  # Ukuran window disesuaikan untuk layout horizontal

    # Definisikan font yang lebih besar
    my_font = Font(family="Helvetica", size=14, weight="bold")

    # Buat tombol dengan font yang lebih besar dan ukuran yang disesuaikan
    tk.Button(window, text="Rock", command=lambda: on_button_click("Rock", window), font=my_font).grid(row=0, column=0, padx=20, pady=20)
    tk.Button(window, text="Paper", command=lambda: on_button_click("Paper", window), font=my_font).grid(row=0, column=1, padx=20, pady=20)
    tk.Button(window, text="Scissors", command=lambda: on_button_click("Scissors", window), font=my_font).grid(row=0, column=2, padx=20, pady=20)

    window.mainloop()

if __name__ == "__main__":
    main()
