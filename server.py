import socket
import threading
from datetime import datetime

HOST = '0.0.0.0'
PORT = 55555
LOGFILE = 'chat_log.txt'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []
usernames = []

def log_message(message):
    with open(LOGFILE, 'a') as f:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        f.write(f"[{timestamp}] {message}\n")

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            log_message(message.decode('utf-8'))
            broadcast(message)
        except:
            index = clients.index(client)
            client.close()
            username = usernames[index]
            clients.remove(client)
            usernames.remove(username)
            leave_msg = f"{username} has left the chat."
            broadcast(leave_msg.encode('utf-8'))
            log_message(leave_msg)
            break

def receive():
    print(f"Server running on {HOST}:{PORT}")
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}")

        client.send("USERNAME".encode('utf-8'))
        username = client.recv(1024).decode('utf-8')
        usernames.append(username)
        clients.append(client)

        join_msg = f"{username} has joined the chat!"
        broadcast(join_msg.encode('utf-8'))
        log_message(join_msg)

        client.send("Connected to the chat server.".encode('utf-8'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

receive()
