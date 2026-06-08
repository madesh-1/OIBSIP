import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode("utf-8")
            if message:
                print(message)
        except:
            print("Disconnected from server.")
            break

# Main client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 5555))
print("===== Chat Application =====")
print("Connected to server! Start chatting!")
print("Type 'exit' to quit.\n")

name = input("Enter your name: ")

thread = threading.Thread(target=receive_messages, args=(client,))
thread.daemon = True
thread.start()

while True:
    message = input()
    if message.lower() == "exit":
        client.close()
        break
    client.send(f"{name}: {message}".encode("utf-8"))
