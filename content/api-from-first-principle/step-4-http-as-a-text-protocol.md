---
title: "Step 4: HTTP as a Text Protocol"
date: 2026-01-31
---

## 1. What problem this step solves
Until now, we used a custom protocol (`ADD 5 10`). This works, but it means only *our* clients can talk to *our* servers. To make a program that can talk to web browsers, mobile apps, and other services, we must use a universal standard. That standard is **HTTP** (HyperText Transfer Protocol).

## 2. Concepts introduced in this step
- **HTTP Method (Verb):** What you want to do (`GET`, `POST`).
- **Path:** Where the resource is (`/add`, `/users`).
- **HTTP Version:** Usually `HTTP/1.1`.
- **Headers:** Key-value pairs providing metadata (`Content-Type: text/plain`).
- **Body:** The actual content (optional).
- **Status Codes:** Standardized results (`200 OK`, `404 Not Found`).

## 3. Why these concepts exist (WHY-focused)
Our custom protocol was too simple. HTTP is richer. 
- The **Method** (GET/POST) tells the server the "intent" immediately.
- The **Path** allows one server to handle many different features (e.g., one port for both `calc` and `user-profile`).
- **Headers** allow the client and server to negotiate details (like "I only speak Spanish" or "This data is an image").
- **Status Codes** mean the client doesn't have to "guess" if things worked; `200` always means success, `400+` always means client error.

## 4. Common confusions & doubts (explicit Q&A)
**Q: Is HTTP "binary" data?**  
A: No! HTTP/1.1 is strictly **plain text**. You can literally type an HTTP request by hand.

**Q: What is the difference between GET and POST?**  
A: Conventionally, `GET` is for asking for data (no side effects), and `POST` is for sending data to be processed or saved.

**Q: Why the blank line in an HTTP request?**  
A: The blank line is the "delimiter" that tells the server: "The headers are finished, the next part is the body."

## 5. ASCII diagrams
```text
A RAW HTTP REQUEST:
GET /add?a=5&b=10 HTTP/1.1
Host: localhost:9000
User-Agent: MyTestClient
[BLANK LINE]

A RAW HTTP RESPONSE:
HTTP/1.1 200 OK
Content-Type: text/plain
Content-Length: 5
[BLANK LINE]
OK 15
```

## 6. Full working Python code
*We will modify our TCP server to manually parse a basic HTTP request.*

**File: `http_server.py`**
```python
import socket

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_sock.bind(('127.0.0.1', 9000))
server_sock.listen(1)

print("Standard HTTP Server running on http://127.0.0.1:9000")

while True:
    client_conn, _ = server_sock.accept()
    request_data = client_conn.recv(1024).decode('utf-8')
    
    # --- CRUDE HTTP PARSING ---
    lines = request_data.split("\r\n")
    if not lines: continue
    
    # First line looks like: "GET /add?a=5&b=10 HTTP/1.1"
    first_line = lines[0]
    print(f"Request: {first_line}")
    
    # Logic to extract path
    try:
        method, path, protocol = first_line.split(" ")
        
        if path.startswith("/add"):
            # Very simple query string parsing
            # Expecting /add?a=5&b=10
            params = path.split("?")[1]
            pairs = params.split("&")
            d = {p.split("=")[0]: p.split("=")[1] for p in pairs}
            result = int(d['a']) + int(d['b'])
            
            body = f"The sum is {result}"
            status = "200 OK"
        else:
            body = "Not Found"
            status = "404 Not Found"
    except Exception as e:
        body = f"Error: {str(e)}"
        status = "400 Bad Request"

    # --- CONSTRUCTING HTTP RESPONSE ---
    response = (
        f"HTTP/1.1 {status}\r\n"
        f"Content-Type: text/plain\r\n"
        f"Content-Length: {len(body)}\r\n"
        f"Connection: close\r\n"
        f"\r\n"
        f"{body}"
    )
    
    client_conn.sendall(response.encode('utf-8'))
    client_conn.close()
```

**How to test:**
1. Run `python3 http_server.py`.
2. Open your web browser and go to: `http://127.0.0.1:9000/add?a=10&b=20`.
3. You will see "The sum is 30" in the browser!

## 7. How this connects to the next step
You just built a web server! But sending data in the URL (`?a=5&b=10`) is messy for complex data. Also, how do we organize our "Paths" so they make sense? In **Step 5**, we will learn about **REST**, which is a set of conventions for making your HTTP paths logical and professional.
