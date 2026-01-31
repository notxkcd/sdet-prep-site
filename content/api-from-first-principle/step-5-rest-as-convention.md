---
title: "Step 5: REST as Convention"
date: 2026-01-31
---

## 1. What problem this step solves
In Step 4, we used a path like `/add?a=5&b=10`. While this works, as an API grows to hundreds of features (users, posts, comments, settings), it becomes a chaotic mess. If one developer uses `/getUser`, another uses `/fetch_person`, and another uses `/person/1`, the API becomes impossible to learn. **REST** (REpresentational State Transfer) is a set of "best practice" rules to keep things organized.

## 2. Concepts introduced in this step
- **Resources:** The "nouns" of your system (Users, Books, Orders).
- **Verbs (CRUD):** 
  - `GET` = Read
  - `POST` = Create
  - `PUT/PATCH` = Update
  - `DELETE` = Delete
- **Statelessness:** The server doesn't "remember" previous requests. Every request must contain all the information needed to fulfill it.

## 3. Why these concepts exist (WHY-focused)
REST makes APIs predictable. If you know an API follows REST, you can guess the URLs without looking at the documentation. 
- You want to see user 5? It's probably `GET /users/5`.
- You want to delete user 5? It's probably `DELETE /users/5`.

**Statelessness** exists for scale. If a server has to "remember" that you are logged in using its internal memory, and that server crashes, you are kicked out. If the request itself contains the "proof" of who you are (like a token), any server in a cluster can handle your request.

## 4. Common confusions & doubts (explicit Q&A)
**Q: Is REST a library I download?**  
A: No. REST is an architectural style. It's just a set of "rules for humans" on how to name their URLs and use HTTP methods.

**Q: Do I *have* to use REST?**  
A: No. You can name your URLs whatever you want. But if you don't follow conventions, other developers will find your API very difficult to use.

**Q: What is a "Resource"?**  
A: Think of it as an object. A "User" is a resource. A "Product" is a resource. You perform actions on these resources using HTTP verbs.

## 5. ASCII diagrams
```text
THE RESTFUL NAMING CONVENTION:

Action          HTTP Verb   Path            Description
------          ---------   ----            -----------
List All        GET         /books          Get a list of all books
Get One         GET         /books/12       Get details for book #12
Create          POST        /books          Add a new book
Update          PUT         /books/12       Replace book #12
Delete          DELETE      /books/12       Remove book #12
```

## 6. Full working Python code
*We will update our server logic to handle "Restful" paths.*

```python
# Logic-only snippet (Assume this is inside our TCP/HTTP loop)

def handle_rest_request(method, path):
    parts = path.strip("/").split("/")
    resource = parts[0] # e.g., "books"
    
    if resource == "books":
        if method == "GET":
            if len(parts) == 1:
                return "200 OK", "Listing all books..."
            else:
                book_id = parts[1]
                return "200 OK", f"Showing details for book {book_id}"
        
        if method == "POST":
            return "201 Created", "Book created successfully"
            
        if method == "DELETE":
            book_id = parts[1]
            return "200 OK", f"Book {book_id} deleted"

    return "404 Not Found", "Resource not found"

# Example usage:
print(handle_rest_request("GET", "/books/42"))
print(handle_rest_request("DELETE", "/books/101"))
```

## 7. How this connects to the next step
We have a great naming system (REST), but we are still sending plain text like "The sum is 30" or "Book created." Programs struggle to parse sentences. They prefer structured data. In **Step 6**, we will introduce **JSON**, the "language of data" for modern APIs.
