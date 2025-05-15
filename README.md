# 🔐 FastAPI Firebase Auth API

A live authentication API that allows users to **sign up** and **sign in** via a simple REST interface.

📍 **Base URL**:  
https://signup-signin-fastapi-with-firebase.onrender.com

📄 **Interactive API Docs (Swagger UI)**:  
https://signup-signin-fastapi-with-firebase.onrender.com/docs

---

## 📝 Features

- 🔐 **User Sign-Up** with password confirmation
- 🔓 **User Sign-In** with password validation
- 📡 Publicly hosted — ready to use, no setup required

---

## 🚀 Usage

Use the API right away via:

- [Swagger UI](https://signup-signin-fastapi-with-firebase.onrender.com/docs)
- Postman or any HTTP client
- `curl` commands (examples below)

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
  "confirm_password": "<your_password_again>",
  "age": <your_age>,
  "professional_title": "<your_title>"
}
````

#### Responses

* `200 OK`: User created successfully
* `400 Bad Request`: Username already exists OR password mismatch

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

* `200 OK`: `"Success"`
* `200 OK`: `"Wrong Password"`
* `400 Bad Request`: `"User Does Not Exist"`

---

## 🧪 Try It Live

### ➡️ Swagger UI

Test all endpoints interactively:
👉 [https://signup-signin-fastapi-with-firebase.onrender.com/docs](https://signup-signin-fastapi-with-firebase.onrender.com/docs)

---

## 💻 Example with curl

> Replace all placeholder values (`<...>`) with your own data.

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

* No authentication key needed — the API is open to test.
* Choose a unique username to avoid collisions with other users.
* Passwords are stored in plaintext (for demo purposes only). Avoid using real or sensitive credentials.

---

Enjoy testing the API! 🚀