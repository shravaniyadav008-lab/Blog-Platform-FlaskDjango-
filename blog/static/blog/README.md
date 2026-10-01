# 📝 Blog Platform

A full-stack blog platform developed using **Python and Django**.

## 🚀 Features

- User Registration
- User Login and Logout
- Create Blog
- View Blog
- Edit Blog
- Delete Blog
- My Blogs
- Search Blogs
- Category Filtering
- Comments
- Django Admin Panel
- Responsive UI
- SQLite Database

## 🛠️ Technology Stack

### Frontend
- HTML5
- CSS3

### Backend
- Python
- Django

### Database
- SQLite

### Authentication
- Django Authentication System

## 📂 Project Structure

```text
Blog Platform
│
├── blog
│   ├── migrations
│   ├── static
│   │   └── blog
│   │       └── style.css
│   │
│   ├── templates
│   │   └── blog
│   │       ├── base.html
│   │       ├── home.html
│   │       ├── register.html
│   │       ├── login.html
│   │       ├── create_blog.html
│   │       ├── edit_blog.html
│   │       ├── blog_detail.html
│   │       └── my_blogs.html
│   │
│   ├── admin.py
│   ├── models.py
│   └── views.py
│
├── blogproject
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md