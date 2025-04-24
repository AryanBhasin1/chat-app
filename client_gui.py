import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, simpledialog
from datetime import datetime

HOST = '127.0.0.1'
PORT = 55555

root = tk.Tk()
root.withdraw()
username = simpledialog.askstring("Username", "Enter your username:")
if not username:
    exit()

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def save_chat_line(msg):
    with open('my_chat_log.txt', 'a') as f:
        f.write(msg + '\n')

win = tk.Tk()
win.title(f"Chat - {username}")
win.geometry("600x550")
win.configure(bg="#1e1e1e")

fg_color = "#ffffff"
bg_color = "#1e1e1e"
entry_bg = "#2e2e2e"

def style(widget, fg=fg_color, bg=bg_color, **kwargs):
    widget.configure(fg=fg, bg=bg, insertbackground=fg, **kwargs)

chat_label = tk.Label(win, text="Chat:", font=("Arial", 12))
chat_label.pack(pady=5)
style(chat_label)

text_area = scrolledtext.ScrolledText(win, wrap='word')
text_area.pack(padx=20, pady=5, expand=True, fill='both')
text_area.config(state='disabled')
style(text_area)

msg_label = tk.Label(win, text="Message:", font=("Arial", 12))
msg_label.pack(pady=5)
style(msg_label)

input_area = tk.Text(win, height=2)
input_area.pack(padx=20, pady=5, fill='x')
style(input_area, bg=entry_bg)

def write():
    msg = input_area.get("1.0", 'end').strip()
    input_area.delete("1.0", 'end')
    if msg:
        full_msg = f"{username}: {msg}"
        client.send(full_msg.encode('utf-8'))

send_button = tk.Button(win, text="Send", command=write, bg="#3e3e3e", fg="#ffffff")
send_button.pack(pady=5)

emoji_frame = tk.Frame(win, bg=bg_color)
emoji_frame.pack()

emojis = ['😊', '😂', '🔥', '👍', '🎉', '😎', '😭', '❤️']

def insert_emoji(emoji):
    input_area.insert(tk.END, emoji)

for emoji in emojis:
    b = tk.Button(emoji_frame, text=emoji, command=lambda e=emoji: insert_emoji(e), font=("Arial", 12), bg="#2e2e2e", fg=fg_color)
    b.pack(side='left', padx=3, pady=3)

def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'USERNAME':
                client.send(username.encode('utf-8'))
            else:
                timestamp = datetime.now().strftime('%H:%M')
                full = f"[{timestamp}] {message}"
                text_area.config(state='normal')
                text_area.insert('end', full + '\n')
                text_area.yview('end')
                text_area.config(state='disabled')
                save_chat_line(message)
        except:
            break

receive_thread = threading.Thread(target=receive, daemon=True)
receive_thread.start()

win.mainloop()
