import socket
import threading
from colorama import init, Fore, Style

init(autoreset=True)

HOST = '127.0.0.1'
PORT = 55555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def save_chat_line(msg):
    with open('my_chat_log.txt', 'a') as f:
        f.write(msg + '\n')

def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'USERNAME':
                client.send(username.encode('utf-8'))
            else:
                if message.startswith(username + ":"):
                    print(Fore.GREEN + message)
                elif f"{username} has joined" in message or f"{username} has left" in message:
                    print(Fore.CYAN + message)
                else:
                    print(Fore.YELLOW + message)
                save_chat_line(message)
        except:
            print(Fore.RED + "Disconnected from server.")
            client.close()
            break

def write():
    while True:
        msg = input('')
        message = f'{username}: {msg}'
        client.send(message.encode('utf-8'))

username = input("Choose your username: ")

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
