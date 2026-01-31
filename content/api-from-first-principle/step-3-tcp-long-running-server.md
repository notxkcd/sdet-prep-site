---
title: "Step 3: TCP Long-Running Server"
date: 2026-01-31
---

## 1. What problem this step solves
In Step 2, the server was tied to its input stream. When that stream closed, the server died. Real APIs need to be "Long-Running"—they sit and wait for hours or days for any number of different clients to connect, send a request, and disconnect.

## 2. Concepts introduced in this step
- **Socket:** An endpoint for communication (an IP address + a Port).
- **Port:** A "mailbox number" on a computer (e.g., 8080).
- **IP Address:** The "street address" of the computer.
- **TCP (Transmission Control Protocol):** A reliable way to send data over a network that ensures everything arrives in order.
- **Listen/Accept:** The state where a server waits for a "knock" on the door.

## 3. Why these concepts exist (WHY-focused)
A computer runs many programs (Browser, Spotify, Discord). When a message arrives at the computer's IP address, how does the computer know which program it's for? 
The **Port** solves this. Your API listens on Port `9000`, so any message marked for `9000` goes to your code. 
**TCP** exists because the internet is messy. Packets get lost or arrive out of order. TCP handles the "bookkeeping" so your code just sees a clean stream of text, exactly like the pipe from Step 2.

## 4. Common confusions & doubts (explicit Q&A)
**Q: Is a socket the same as an API?**  
A: No. A socket is the "telephone hardware." The API is the "language" you speak over the phone.

**Q: What is `127.0.0.1`?**  
A: That is the "loopback" address. It means "this computer." It's used for testing servers locally.

**Q: Can two programs use the same port?**  
A: No. If your API is on Port 8080, no other program can use 8080. You will get an "Address already in use" error.

## 5. ASCII diagrams
```text
NETWORK TOPOLOGY:

[Client] ----(Request over TCP)----> [Router/Internet] ----> [Server Computer]
                                                                    |
                                                               [Port 9000]
                                                                    |
                                                               [Your Script]
```

## 6. Full working Python code
*We will now use the Python `socket` library. This is the "raw" way to build a server.*

**File: `tcp_server.py`**
```python
import socket

# 1. Create a socket (IPv4, TCP)
server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. Bind to an address and port
server_sock.bind(('127.0.0.1', 9000))

# 3. Start listening
server_sock.listen(1)
print("Server is listening on 127.0.0.1:9000...")

while True:
    # 4. Wait for a connection (This 'blocks' until someone connects)
    client_conn, client_addr = server_sock.accept()
    print(f"New connection from {client_addr}")
    
    # 5. Receive the data (up to 1024 bytes)
    data = client_conn.recv(1024).decode('utf-8')
    print(f"Received: {data.strip()}")
    
    # 6. Apply our Protocol Logic
    if data.startswith("ADD"):
        try:
            _, a, b = data.split()
            result = int(a) + int(b)
            response = f"OK {result}\n"
        except:
            response = "ERR INVALID\n"
    else:
        response = "ERR UNKNOWN\n"
        
    # 7. Send the response back
    client_conn.sendall(response.encode('utf-8'))
    
    # 8. Close this specific connection
    client_conn.close()
```

**How to test:**
1. Run `python3 tcp_server.py`.
2. In another terminal, use a tool like `nc` (netcat) or `telnet`:
   `echo "ADD 5 10" | nc 127.0.0.1 9000`
3. You will see `OK 15`.

## 7. How this connects to the next step
We now have a real network server! But our protocol (`ADD 5 10`) is something we made up. The rest of the world uses a standard protocol called **HTTP**. In **Step 4**, we will change our server to understand "Raw HTTP" instead of our custom "CALC-PROTOCOL."
