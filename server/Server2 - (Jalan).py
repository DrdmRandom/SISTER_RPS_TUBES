import socket
import threading

clients = []
choices = []
clients_lock = threading.Lock()

def rps_game(c1_choice, c2_choice):
    if c1_choice == c2_choice:
        return "Draw"
    elif (c1_choice == "Rock" and c2_choice == "Scissors") or \
            (c1_choice == "Scissors" and c2_choice == "Paper") or \
            (c1_choice == "Paper" and c2_choice == "Rock"):
        return "Client 1 Wins"
    else:
        return "Client 2 Wins"

def handle_client(conn, addr):
    global choices
    print(f"[NEW CONNECTION] {addr} connected.")

    choice = conn.recv(1024).decode('utf-8')
    choices.append(choice)

    while len(choices) < 2:
        continue

    result = rps_game(choices[0], choices[1])
    with clients_lock:
        for client in clients:
            if client.fileno() != -1:  # Cek apakah socket masih terbuka
                try:
                    client.sendall(result.encode('utf-8'))
                except Exception as e:
                    print(f"Error sending data to {client}: {e}")

    conn.close()
    with clients_lock:
        clients.remove(conn)

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('192.168.1.14', 55559))
    server.listen(2)

    while len(clients) < 2:
        conn, addr = server.accept()
        with clients_lock:
            clients.append(conn)
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

    print(f"[STARTING] Game starting with {len(clients)} players.")

if __name__ == "__main__":
    start_server()
