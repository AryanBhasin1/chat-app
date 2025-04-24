### **Project Description:**

**Real-Time Chat Application (Python)**

This is a simple, real-time chat application built in Python that allows users to communicate over a network using either a **Terminal Client** or a **Graphical User Interface (GUI)** client. The app supports multiple users connecting to a server, sending/receiving messages in real-time, and saves chat history locally. 

Key features include:
- **Multiple User Support**: Users can join the server and send/receive messages from multiple clients.
- **Terminal & GUI Clients**: The application has two types of clients:
  - **Terminal Client**: A simple command-line interface with color-coded messages.
  - **GUI Client**: A user-friendly interface with dark mode and emoji support.
- **Real-Time Communication**: Messages are transmitted instantly between users using threads.
- **Chat History**: All messages are logged and saved locally for future reference.
- **Emoji Support**: Users can insert emojis into messages via buttons or by typing them directly.

---

### **Project Requirements:**

To run this project, the following packages and Python version are required:

1. **Python 3.x** (Recommended: Python 3.7 or above)
2. **Required Libraries**:
   - `colorama` — for color support in terminal (used in the terminal client).
   - `tkinter` — for the GUI client.
   - `threading` — for handling real-time message communication without blocking the app.

You can install the required libraries using `pip`:
```bash
pip install colorama
```
(Note: `tkinter` comes pre-installed with most Python installations, but if not, you can install it via your system’s package manager.)

---

### **How to Run the Project:**

1. **Start the Server**:
   - Run the server by executing:
     ```bash
     python server.py
     ```

2. **Start Clients**:
   - **Terminal Client**: Run the following command in different terminal windows to simulate multiple clients:
     ```bash
     python client_terminal.py
     ```
   - **GUI Client**: Run the GUI client:
     ```bash
     python client_gui.py
     ```

3. **Communicate**: Once the clients are connected to the server, they can send and receive messages in real-time.

---

Feel free to adjust or expand on these based on your specific needs!
