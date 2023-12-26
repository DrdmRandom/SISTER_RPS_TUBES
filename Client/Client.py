import socket

HOST = '192.168.1.14'  # Server's hostname or IP address
PORT = 12346# The port used by the server

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))  # Connect to the server


message = client_socket.recv(1024)
print(message.decode())

choice = input("Enter your choice: ")
client_socket.send(choice.encode())

result = client_socket.recv(1024)
print(result.decode())
client_socket.close()
