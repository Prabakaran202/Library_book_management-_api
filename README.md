# 📚 Library Book Management API

A REST API built with FastAPI for managing library books.

## 🚀 Live Demo

- **Backend API:** [https://library-api.onrender.com](https://library-api.onrender.com)
- **Frontend:** [https://library-app.netlify.app](https://library-app.netlify.app)
- **API Docs:** [https://library-api.onrender.com/docs](https://library-api.onrender.com/docs)

---

## 🛠️ Tech Stack

| Technology | Usage |
|------------|-------|
| FastAPI | Backend API |
| Pydantic | Data Validation |
| HTML + JavaScript | Frontend |
| Render.com | Backend Hosting |
| Netlify | Frontend Hosting |

---

## 📋 Features

- ✅ View all books
- ✅ Add new book
- ✅ Find book by ID
- ✅ Update book details
- ✅ Delete book
- ✅ Data Validation
- ✅ Error Handling

---

## 📁 Project Structure

```
library-api/
│
├── main.py          # FastAPI backend
├── index.html       # Frontend
├── requirements.txt # Dependencies
└── README.md        # This file
```

---

## ⚙️ Installation & Setup

### 1. Clone the repo
```bash
git clone https://github.com/Prabakaran202/library-api.git
cd library-api
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the server
```bash
uvicorn main:app --reload
```

### 4. Open API docs
```
http://127.0.0.1:8000/docs
```

---

## 🔗 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /books | Get all books |
| POST | /books | Add new book |
| GET | /books/{id} | Get book by ID |
| PUT | /books/{id} | Update book |
| DELETE | /books/{id} | Delete book |

---

## 📝 Request Body (POST/PUT)

```json
{
  "id": 1,
  "title": "Python Basics",
  "author": "Robert",
  "price": 299.0,
  "available": true
}
```

---

## 📊 Response Example

```json
{
  "msg": "Book added!",
  "data": {
    "id": 1,
    "title": "Python Basics",
    "author": "Robert",
    "price": 299.0,
    "available": true
  }
}
```

---

## ❌ Error Responses

| Status Code | Meaning |
|-------------|---------|
| 200 | Success |
| 404 | Book not found |
| 422 | Validation Error |

---

## 👨‍💻 Developer

**Prabakaran** — Backend Developer

- GitHub: [@Prabakaran202](https://github.com/Prabakaran202)

---

## 📄 License

MIT License
