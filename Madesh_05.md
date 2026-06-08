# 💬 Python Chat Application

A beginner-friendly command-line Chat Application built with Python using a client-server model.

---

## 📋 Features
- **Real-time messaging** between multiple users
- Simple **client-server model**
- Supports **multiple clients** at the same time
- Displays **username** with every message
- No external libraries needed!

---

## 🛠️ Requirements
- Python 3.x
- No external libraries needed!

---

## 📁 Files
| File | Description |
|------|-------------|
| `Madesh_05_server.py` | Runs the chat server |
| `Madesh_05_client.py` | Runs the chat client |

---

## ▶️ How to Run

**Step 1 — Start the Server:**
1. Open **Command Prompt**
2. Navigate to your project folder
3. Type:
```
python Madesh_05_server.py
```

**Step 2 — Start the Client(s):**
1. Open a **second Command Prompt**
2. Navigate to your project folder
3. Type:
```
python Madesh_05_client.py
```

**Step 3 — Chat:**
- Open a **third Command Prompt** and run the client again
- Now two users can chat with each other in real-time!

---

## 💡 Example

```
===== Chat Application =====
Connected to server! Start chatting!
Type 'exit' to quit.

Enter your name: Madesh
Hello!
John: Hi Madesh, how are you?
Madesh: I'm good, thanks!
```

---

## 🔧 How It Works
- The **server** listens for incoming connections
- Each **client** connects to the server and sends messages
- The server **broadcasts** messages to all other connected clients

---

## 👤 Author
Madesh

---

## 📝 License
This project is for educational purposes.
