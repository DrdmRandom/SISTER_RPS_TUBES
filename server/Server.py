import socket
import threading

# Server setup
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Allow the socket to reuse the address
server.bind(('192.168.1.14', 5001))  # Use a valid IP and port
server.listen()  # Set the number of unaccepted connections that the system will allow before refusing new connections

# Store client info
clients = []
choices = [None, None]

# Synchronization primitive
choices_made = threading.Condition()

def client_thread(connection, player):
    global choices
    try:
        connection.sendall('Welcome to Rock Paper Scissors! Please choose Rock, Paper, or Scissor:'.encode())
        choice = connection.recv(1024).decode().strip()
        with choices_made:
            choices[player] = choice
            # Check if both players made a choice
            choices_made.notify_all()  # Notify any waiting threads
            choices_made.wait_for(lambda: all(c is not None for c in choices))  # Wait until all choices are made

        result = determine_winner(choices[0], choices[1])
        connection.sendall(result.encode())
    finally:
        connection.close()

def determine_winner(choice1, choice2):
    def determine_winner(choice1, choice2):
        # Mapping of what beats what
        beats = {'Rock': 'Scissors', 'Scissors': 'Paper', 'Paper': 'Rock'}

        if choice1 == choice2:
            return "It's a tie!"
        elif beats[choice1] == choice2:
            return "Player 1 wins!"
        else:
            return "Player 2 wins!"
    pass

# Function to start the game and accept clients
def start_game():
    while len(clients) < 2:  # We need exactly 2 clients for a game
        conn, addr = server.accept()
        print(f"Connected by {addr}")
        clients.append(conn)
        player_number = len(clients) - 1
        thread = threading.Thread(target=client_thread, args=(conn, player_number))
        thread.start()

# Start the game
start_game()
