---
title: "Step 8: Client Discipline"
date: 2026-01-31
---

## 1. What problem this step solves
Until now, we've focused on the Server. But what happens if the network goes down for 2 seconds? Or if the Server is slow? A poorly written Client will hang, crash, or spam the server with thousands of requests, potentially causing a "Self-Denial of Service" (Self-DoS).

## 2. Concepts introduced in this step
- **Timeout:** How long to wait before giving up on a request.
- **Retry Logic:** Attempting the request again if it fails (with caution).
- **Exponential Backoff:** Waiting longer and longer between retries (e.g., wait 1s, then 2s, then 4s...).
- **User Agent:** Identifying who the client is.

## 3. Why these concepts exist (WHY-focused)
The network is **unreliable**. 
- **Timeouts** prevent your program from "freezing" forever if a server doesn't respond.
- **Backoff** is "politeness." If a server is crashing because it's overloaded, and 1,000 clients all retry immediately at the same time, the server will never recover. 
- **User Agents** help server owners. If your client has a bug, the server owner can look at their logs, see "Client: ShahidApp-v1.0", and contact you to fix it.

## 4. Common confusions & doubts (explicit Q&A)
**Q: Should I retry every error?**  
A: No! Only retry "Transient" errors (like a `503 Service Unavailable` or a network timeout). Never retry a `400 Bad Request`—the data is wrong, and retrying won't change that.

**Q: What is a good timeout value?**  
A: It depends. For a fast UI, 2-5 seconds. For a heavy data report, maybe 30 seconds. Never leave it at "Infinite."

**Q: Why not just use a `while True` loop for retries?**  
A: Without a limit, your program will loop forever and eat your CPU if the server is permanently down. Always set a `max_retries` limit (usually 3 or 5).

## 5. ASCII diagrams
```text
RETRY WITH EXPONENTIAL BACKOFF:

Request 1 (Fail) -> Wait 1s
Request 2 (Fail) -> Wait 2s
Request 3 (Fail) -> Wait 4s
Request 4 (Fail) -> Wait 8s
Request 5 (Fail) -> GIVE UP & LOG ERROR
```

## 6. Full working Python code
*We will use the popular `requests` library style (simulated) to show disciplined API consumption.*

```python
import time
import random

def mock_server_api(request_count):
    """Simulates a flaky server that fails 50% of the time."""
    if random.random() < 0.5:
        return {"status": 500, "body": "Internal Server Error"}
    return {"status": 200, "body": {"result": "Success!"}}

def disciplined_client_call():
    max_retries = 3
    base_delay = 1 # second
    
    for attempt in range(max_retries):
        print(f"Attempt {attempt + 1}...")
        
        response = mock_server_api(attempt)
        
        if response["status"] == 200:
            return response["body"]
        
        if response["status"] >= 500:
            # Server error, wait and try again
            delay = base_delay * (2 ** attempt) # Exponential: 1, 2, 4...
            print(f"Server failed. Retrying in {delay}s...")
            time.sleep(delay)
        else:
            # Client error (400s), don't retry
            print(f"Client error {response['status']}. Aborting.")
            break
            
    return "All attempts failed."

# Run the client
result = disciplined_client_call()
print(f"Final Result: {result}")
```

## 7. How this connects to the next step
Now that we have a professional Client and Server, we need to think about the "Real World." The internet is full of bad actors and limited resources. In **Step 9**, we will discuss **Security, Rate Limiting, and Authentication**.
