---
title: "Step 7: Versioning and Errors"
date: 2026-01-31
---

## 1. What problem this step solves
Imagine you have an API used by 1,000 people. You decide to change the field `user_name` to `full_name`. Suddenly, all 1,000 apps break because they are looking for `user_name`. Also, when a user enters the wrong password, simply sending "Error" isn't helpful. We need to handle change and failure gracefully.

## 2. Concepts introduced in this step
- **API Versioning:** Including the version in the URL (e.g., `/v1/users`).
- **Breaking Change:** A change that stops old clients from working.
- **HTTP Status Codes (Advanced):**
  - `401 Unauthorized` (You need to log in)
  - `403 Forbidden` (You aren't allowed to do this)
  - `422 Unprocessable Entity` (The data is formatted correctly but is logically wrong)
  - `500 Internal Server Error` (The server crashed)

## 3. Why these concepts exist (WHY-focused)
**Versioning** allows you to evolve. You keep the old code at `/v1` for existing users and put the new code at `/v2`. This gives people time to migrate.
**Detailed Errors** exist because the Client programmer is a human. If they get a `400` error with a JSON body saying `{"error": "field_too_short", "field": "password", "min": 8}`, they can fix their code instantly. If they just get "Error", they will be frustrated and call you.

## 4. Common confusions & doubts (explicit Q&A)
**Q: Should I use `/v1/` or a header for versioning?**  
A: Both exist, but putting it in the URL (`/v1/`) is much more common and easier to test in a browser.

**Q: Why use `401` vs `403`?**  
A: `401` means "Who are you? (Please log in)". `403` means "I know who you are, but you aren't allowed to touch this."

**Q: Should I always return JSON for errors?**  
A: YES. If your API usually returns JSON, its errors should also be JSON. This allows the client program to parse the error and show a nice message to the user.

## 5. ASCII diagrams
```text
THE VERSIONING PATH:

[Client v1] ----> [API Gateway] ----> [Old Logic (/v1/)]
[Client v2] ----> [API Gateway] ----> [New Logic (/v2/)]

THE ANATOMY OF A GOOD ERROR:
{
  "status": 400,
  "error_code": "INVALID_EMAIL",
  "message": "The email provided is not a valid format.",
  "help_url": "https://api.docs.com/errors/invalid_email"
}
```

## 6. Full working Python code
*We will build a professional Error Handler and a Version Router.*

```python
def api_v1_get_user(user_id):
    # Old way: returns 'name'
    return {"id": user_id, "name": "Alice"}

def api_v2_get_user(user_id):
    # New way: returns 'first_name' and 'last_name'
    return {"id": user_id, "first_name": "Alice", "last_name": "Smith"}

def router(path):
    if path.startswith("/v1/"):
        return 200, api_v1_get_user(1)
    elif path.startswith("/v2/"):
        return 200, api_v2_get_user(1)
    else:
        # Standardized Error Response
        error_body = {
            "error": "NOT_FOUND",
            "message": f"The path {path} does not exist.",
            "available_versions": ["/v1/", "/v2/"]
        }
        return 404, error_body

# Test routing
print(f"Calling v1: {router('/v1/user')}")
print(f"Calling v2: {router('/v2/user')}")
print(f"Calling unknown: {router('/v3/user')}")
```

## 7. How this connects to the next step
We've spent a lot of time on the Server. But an API is a two-way street. A "lazy" or "messy" Client can cause just as many problems as a bad Server. In **Step 8**, we will learn **Client Discipline**: how to write code that consumes APIs reliably.
