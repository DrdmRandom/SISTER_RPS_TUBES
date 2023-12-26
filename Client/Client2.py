import socket

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('192.168.1.14', 55559))

    choice = input("Enter your choice (Rock, Paper, Scissors): ")
    client.send(choice.encode('utf-8'))

    # Menerima hasil dari server
    result = client.recv(1024).decode('utf-8')
    print("Game Result:", result)

    client.close()

if __name__ == "__main__":
    main()


    def rps_game(c1_choice, c2_choice):
        if c1_choice == c2_choice:
            return "Draw"
        elif (c1_choice == "Rock" and c2_choice == "Scissors") or \
                (c1_choice == "Scissors" and c2_choice == "Paper") or \
                (c1_choice == "Paper" and c2_choice == "Rock"):
            return "Client 1 Wins"
        else:
            return "Client 2 Wins"
