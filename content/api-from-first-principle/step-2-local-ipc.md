---
title: "Step 2: Local IPC (stdin/stdout)"
date: 2026-01-31
---

## 1. What problem this step solves
Until now, our "Client" and "Server" were just two functions in the same script. In the real world, they are separate programs. Before we deal with the complexity of networks (IP addresses, ports, firewalls), we need to see how two separate processes can talk to each other on the same machine.

## 2. Concepts introduced in this step
- **Process:** A running instance of a program.
- **IPC (Inter-Process Communication):** The general term for programs talking to each other.
- **Standard Streams:** `stdin` (input) and `stdout` (output).
- **Pipes:** A way to connect the `stdout` of one program to the `stdin` of another.

## 3. Why these concepts exist (WHY-focused)
Programs are isolated by the operating system for security. Program A cannot reach into the memory of Program B. 
To communicate, they must use a "medium" provided by the OS. The simplest medium is the "Pipe." Imagine a literal pipe where Program A drops a note into one end, and Program B picks it up from the other.

## 4. Common confusions & doubts (explicit Q&A)
**Q: I thought APIs were about URLs and the Internet?**  
A: The Internet is just a very long pipe. The logic of "sending a string and waiting for a string" is exactly the same whether it's a pipe on your laptop or a cable under the Atlantic Ocean.

**Q: Why use `stdin`/`stdout`?**  
A: Every program has them by default. It's the "universal interface" of Unix-like systems. If you can talk to a pipe, you can eventually talk to a network.

## 5. ASCII diagrams
```text
THE PIPE MODEL:

[Client Process]                 [Server Process]
       |                                |
   (stdout) -------- PIPE ----------> (stdin)
       |                                |
   (stdin)  <------- PIPE ---------- (stdout)
```

## 6. Full working Python code
*We will create two separate files. One will be the 'Server' and the other the 'Client'.*

**File 1: `server.py`**
```python
import sys

# The Server runs forever, waiting for lines of input
for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    
    # Logic from Step 1
    parts = line.split(" ")
    if parts[0] == "ADD":
        res = int(parts[1]) + int(parts[2])
        print(f"OK {res}")
    elif parts[0] == "QUIT":
        break
    else:
        print("ERR UNKNOWN")
    
    # Crucial: flush tells the OS to send the data NOW
    sys.stdout.flush()
```

**File 2: `client.py`**
*In a real scenario, you'd run these together. For this step, we'll simulate the client-side interaction manually in the terminal.*

**How to run this:**
1. Open a terminal.
2. Run `python3 server.py`.
3. Type `ADD 5 10` and hit Enter.
4. You will see `OK 15`.

## 7. How this connects to the next step
Using pipes is great, but it has a massive limitation: the programs must be started together and are physically "linked" on one machine. In **Step 3**, we will replace the local pipe with a **Network Socket (TCP)**, allowing the server to sit and wait for *anyone* on the network to connect.
