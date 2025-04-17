# 📚 Library Management System

A Django-based web application that allows admins and users to manage and view books efficiently. This system supports user registration, login functionalities, book CRUD operations, and role-based access.

---

## 🚀 Features

### 👤 Admin:
- Login / Signup
- Add new books
- View all books
- Edit and delete books

### 👥 User:
- Login / Signup
- View all books (read-only)

---

## 🛠️ Tech Stack

- **Frontend:** HTML, CSS, Bootstrap
- **Backend:** Python, Django
- **Database:** SQLite
- **Version Control:** Git & GitHub

---

## 📸 Screenshots

### 🔐 Admin Login
![Screenshot Admin_login](https://github.com/user-attachments/assets/31034caf-58c0-4705-9060-6fe46a92535c)


### 📖 View All Books
(![Screenshot view_all_books](https://github.com/user-attachments/assets/f0a851f8-49af-41f8-9204-e4dd71c21b2c)


> Add your own screenshots inside a `/screenshots/` folder.

---

## 🧑‍💻 How to Run Locally

```bash
# Clone the repository
git clone https://github.com/your-username/library-management-django.git
cd library-management-django

# Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Start the server
python manage.py runserver
