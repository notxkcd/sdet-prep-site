---
title: "Step 1: Protocol Design (On Paper)"
date: 2026-01-31
---

## 1. What problem this step solves
In Step 0, we saw that a Client and Server need a contract. But if the contract isn't precisely defined, programs will crash. If I expect a number and you send a string, the system fails. "Protocol Design" is the act of deciding exactly what characters and formats will be used before we write a single line of networking code.

## 2. Concepts introduced in this step
- **Protocol:** A set of rules governing the exchange of data.
- **Payload:** The actual data being sent (the "meat" of the message).
- **Header/Metadata:** Information *about* the message (e.g., "how long is this message?").
- **Delimiters:** Markers that tell the program where one piece of data ends and another begins (like a newline `\n`).

## 3. Why these concepts exist (WHY-focused)
Computers don't "guess." If you send a stream of bytes over a wire, the receiving computer just sees `101010...`.
A protocol exists so the receiver knows:
1. "When should I start listening?"
2. "Which part of this is the command?"
3. "Which part is the data?"
4. "When is the message finished?"

Without a protocol, the receiver might keep waiting forever for data that never comes, or it might try to process a half-finished message.

## 4. Common confusions & doubts (explicit Q&A)
**Q: Why not just use English? ("Hey server, add 5 and 2")**  
A: Parsing natural language is hard and ambiguous. Computers need predictable patterns. It is much easier to parse `ADD 5 2` than "Could you please add five and two?".

**Q: What happens if the Client breaks the protocol?**  
A: The Server should identify the error and inform the Client, rather than crashing. This is called "Error Handling" and is a core part of the protocol.

**Q: Is HTTP the only protocol?**  
A: No! There are thousands (SSH, FTP, SMTP, DNS). HTTP is just the most popular one for the web. Today, we are designing our *own* simple protocol to understand the mechanics.

## 5. ASCII diagrams
```text
OUR CUSTOM "CALC-PROTOCOL" SPECIFICATION:

Request Format:
[COMMAND][SPACE][ARG1][SPACE][ARG2][NEWLINE]

Example Request:
"ADD 10 20\n"

Response Format:
[STATUS][SPACE][RESULT_OR_ERROR][NEWLINE]

Example Success:
"OK 30\n"

Example Error:
"ERR UNKNOWN_COMMAND\n"
```

## 6. Full working Python code
*We will implement a "Parser" that enforces our paper protocol. This is the heart of what an API framework does for you later.*

```python
def parse_request(raw_string):
    """Enforces the 'CALC-PROTOCOL' request rules."""
    parts = raw_string.strip().split(" ")
    if len(parts) != 3:
        return "ERR INVALID_FORMAT\n"
    
    command, arg1, arg2 = parts
    
    try:
        val1 = int(arg1)
        val2 = int(arg2)
    except ValueError:
        return "ERR NOT_INTEGERS\n"
    
    if command == "ADD":
        return f"OK {val1 + val2}\n"
    elif command == "MUL":
        return f"OK {val1 * val2}\n"
    else:
        return "ERR UNKNOWN_COMMAND\n"

# Test the protocol enforcement
print(f"Valid:   {parse_request('ADD 5 10')}")
print(f"Invalid: {parse_request('SUB 5 10')}")
print(f"Broken:  {parse_request('ADD FIVE TEN')}")
```

## 7. How this connects to the next step
We have a protocol (the logic), but we are still inside one Python file. The programs aren't truly "separate." In **Step 2**, we will separate the Client and the Server into two different processes and make them talk using the simplest possible method: **Standard Input and Output**.

```