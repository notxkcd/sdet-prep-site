---
title: "Step 6: JSON and Schemas"
date: 2026-01-31
---

## 1. What problem this step solves
Until now, our server replied with sentences like "The sum is 30." If a mobile app wants to display just the number "30" in a large font, it has to write complex code to "scrape" the number out of the sentence. If we change the sentence to "Result: 30", the app breaks. We need a way to send data that is structured and machine-readable.

## 2. Concepts introduced in this step
- **JSON (JavaScript Object Notation):** A text-based format for representing structured data (lists and dictionaries).
- **Serialization:** Converting a Python object into a JSON string.
- **Deserialization:** Converting a JSON string back into a Python object.
- **Schema:** A "blueprint" or "definition" of what the data should look like (e.g., "The 'age' field must be an integer").

## 3. Why these concepts exist (WHY-focused)
**JSON** is the industry standard because it is lightweight and easy for almost every programming language to read. 
**Schemas** exist because "Garbage In = Garbage Out." If your API expects a user's `email` and someone sends an image, your database might crash. A Schema allows you to validate the data *before* your logic touches it.

## 4. Common confusions & doubts (explicit Q&A)
**Q: Is JSON related to JavaScript?**  
A: It started that way, but now it's universal. You don't need to know any JavaScript to use JSON in Python.

**Q: Can I send images in JSON?**  
A: Not directly. JSON is text. You usually send a "URL" to the image, or you encode the image into a very long text string (Base64), though the former is preferred.

**Q: Why not use XML?**  
A: XML is much wordier and harder to read for humans. JSON has mostly replaced it for modern APIs.

## 5. ASCII diagrams
```text
TEXT VS JSON:

Plain Text:
"User John is 25 years old and lives in New York"

JSON:
{
  "name": "John",
  "age": 25,
  "city": "New York",
  "is_active": true
}
```

## 6. Full working Python code
*We will use Python's built-in `json` library to handle our API data.*

```python
import json

# 1. THE DATA (Python Dictionary)
book_data = {
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "year": 1925,
    "available": True
}

# 2. SERIALIZATION (Object -> String)
# This is what the SERVER sends over the network
json_string = json.dumps(book_data)
print(f"Network Payload: {json_string}")

# 3. DESERIALIZATION (String -> Object)
# This is what the CLIENT does when it receives the data
received_data = json.loads(json_string)
print(f"Client Accessing Data: {received_data['title']} by {received_data['author']}")

# 4. SCHEMA VALIDATION (Simple Version)
def validate_book(data):
    required_fields = ["title", "author", "year"]
    for field in required_fields:
        if field not in data:
            return False, f"Missing field: {field}"
    
    if not isinstance(data['year'], int):
        return False, "Year must be an integer"
        
    return True, "Valid"

# Testing validation
is_valid, msg = validate_book({"title": "A Book", "author": "Me"})
print(f"Validation Result: {is_valid} - {msg}")
```

## 7. How this connects to the next step
Now we have structured data (JSON) and a naming convention (REST). But what happens when things go wrong? Or when we need to change our API without breaking old apps? In **Step 7**, we will learn how to handle **Errors** professionally and how to **Version** our API.
