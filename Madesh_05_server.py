import socket
import threading

clients = []

def handle_client(client_socket, address):
    print(f"New connection: {address}")
    while True:
        try:
            message = client_socket.recv(1024).decode("utf-8")
            if message:
                print(f"Message received: {message}")
                broadcast(message, client_socket)
            else:
                remove_client(client_socket)
                break
        except:
            remove_client(client_socket)
            break

def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode("utf-8"))
            except:
                remove_client(client)

def remove_client(client_socket):
    if client_socket in clients:
        clients.remove(client_socket)
        client_socket.close()

# Main server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 5555))
server.listen(5)
print("===== Chat Server Started =====")
print("Waiting for connections...")

while True:
    client_socket, address = server.accept()
    clients.append(client_socket)
    thread = threading.Thread(target=handle_client, args=(client_socket, address))
    thread.start()
