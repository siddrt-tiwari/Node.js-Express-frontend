# 🚀 Node.js + Express Frontend with Flask Backend (Dockerized)

This project demonstrates a **multi-service application** using:

* 🖥️ **Frontend**: Node.js + Express (EJS templates)
* 🧠 **Backend**: Flask (Python)
* 🗄️ **Database**: MongoDB
* 🐳 **Containerization**: Docker & Docker Compose

---

## 📂 Project Structure

```
project-root/
│
├── frontend/
│   ├── app.js
│   ├── package.json
│   ├── views/
│   │   ├── form.ejs
│   │   ├── todo.ejs
│   │   └── success.ejs
│   ├── Dockerfile
│
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   ├── Dockerfile
│
├── docker-compose.yml
├── .gitignore
└── README.md
```

---

## ⚙️ Features

* Submit user details (Name & Email)
* Add Todo items
* Backend validation and MongoDB storage
* Service-to-service communication via Docker network
* Fully containerized setup

---

## 🐳 Docker Setup

### 1️⃣ Build and Run Containers

```bash
docker-compose up --build
```

---

### 2️⃣ Access the Application

* 🌐 Frontend: http://localhost:3000
* 🔧 Backend: http://localhost:5001 (mapped from container 5000)

---

## 🔗 Service Communication

* Frontend communicates with backend using:

```
http://backend:5000
```

* Docker Compose automatically creates a shared network.

---

## 📦 Docker Images

Available on Docker Hub:

* Frontend: siddrttiwari/frontend
* Backend: siddrttiwari/backend

---

## 🚀 Push Images to Docker Hub

```bash
# Build
docker build -t siddrttiwari/frontend ./frontend
docker build -t siddrttiwari/backend ./backend

# Push
docker push siddrttiwari/frontend
docker push siddrttiwari/backend
```

---

## 🧪 API Endpoints (Flask Backend)

### Submit User

```
POST /submit
```

### Submit Todo

```
POST /submittodoitem
```

---

## 🔐 Environment Variables

Create a `.env` file in backend:

```
MONGO_URI=your_mongodb_connection_string
```

---

## 🚫 .gitignore

```
node_modules/
.env
.vscode/
__pycache__/
*.pyc
```

---

## ⚠️ Notes

* Port **5000** may be reserved on macOS → using **5001**
* Do NOT use `localhost` inside containers — use service name (`backend`)
* Ensure Docker Desktop is running before starting

---

## 🧠 Future Improvements

* Add MongoDB as a Docker service
* Use Nginx as reverse proxy
* Implement CI/CD with GitHub Actions
* Add authentication system

---

## 👨‍💻 Author

Siddharth Tiwari

---

## 📜 License

This project is for educational purposes.
