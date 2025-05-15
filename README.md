# 🔐 FastAPI Firebase Auth API

A live authentication API that allows users to **sign up** and **sign in** using a simple REST interface.

📍 **Base URL**:  
https://signup-signin-fastapi-with-firebase.onrender.com

📄 **Interactive API Docs (Swagger UI)**:  
https://signup-signin-fastapi-with-firebase.onrender.com/docs

---

## 📝 Features

- 🔐 Sign up with password confirmation and unique username check
- 🔓 Sign in with password validation
- ⚠️ Returns proper HTTP status codes (e.g., `401 Unauthorized` for wrong passwords)
- 📡 Publicly hosted — ready to use instantly

---

## 🚀 Usage

You can use the API right away via:

- [Swagger UI](https://signup-signin-fastapi-with-firebase.onrender.com/docs)
- Postman or any HTTP client
- `curl` (examples below)

---

## 📬 API Endpoints

### 📝 POST `/signup`

Register a new user.

#### Body (JSON)

```json
{
  "first_name": "<your_first_name>",
  "middle_name": "<your_middle_name>",
  "last_name": "<your_last_name>",
  "username": "<unique_username>",
  "password": "<your_password>",
  "confirm_password": "<your_password>",
  "age": <your_age>,
  "professional_title": "<your_title>"
}
````

#### Responses

* `200 OK`: User created successfully
* `400 Bad Request`: Username already exists or password mismatch

---

### 🔐 POST `/signin`

Authenticate a user.

#### Body (JSON)

```json
{
  "username": "<your_username>",
  "password": "<your_password>"
}
```

#### Responses

* `200 OK`: `{"message": "Success"}`
* `401 Unauthorized`: `{"detail": "Wrong password"}`
* `400 Bad Request`: `{"detail": "User does not exist"}`

---

## 🧪 Try It Live

### ➡️ Swagger UI

Test all endpoints directly in your browser:
👉 [https://signup-signin-fastapi-with-firebase.onrender.com/docs](https://signup-signin-fastapi-with-firebase.onrender.com/docs)

---

## 💻 Example with curl

> Replace all `<...>` placeholders with your own data.

### ✅ Sign Up

```bash
curl -X POST "https://signup-signin-fastapi-with-firebase.onrender.com/signup" \
-H "Content-Type: application/json" \
-d '{
  "first_name": "<your_first_name>",
  "middle_name": "<your_middle_name>",
  "last_name": "<your_last_name>",
  "username": "<unique_username>",
  "password": "<your_password>",
  "confirm_password": "<your_password>",
  "age": <your_age>,
  "professional_title": "<your_title>"
}'
```

### 🔓 Sign In

```bash
curl -X POST "https://signup-signin-fastapi-with-firebase.onrender.com/signin" \
-H "Content-Type: application/json" \
-d '{
  "username": "<your_username>",
  "password": "<your_password>"
}'
```

---

## ✅ Notes

* No API key or token required — test freely.
* Use a **unique username** to avoid conflicts.
* Passwords are currently stored in plaintext (demo purposes). Avoid using real credentials.

---

Enjoy exploring the API! 🚀