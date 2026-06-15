# Blog Application

A simple yet powerful blog application built using **Django** framework. This application allows users to create, read, and manage blog posts with a user-friendly interface.

## 🌐 Live Demo

Check out the live application here: [https://blog-application-3-yeh7.onrender.com](https://blog-application-3-yeh7.onrender.com)

## ✨ Features

- **User Authentication**: Secure user registration and login system
- **Create Posts**: Write and publish blog posts with rich text content
- **View Posts**: Browse all blog posts in a clean, organized interface
- **Author Information**: Each post displays the author and posting date
- **Admin Panel**: Django admin interface for managing posts and users
- **Responsive Design**: Works seamlessly on desktop and mobile devices
- **Database**: SQLite database for persistent data storage

## 🏗️ Project Structure

```
blog-Application/
├── django_blog/                 # Main project directory
│   ├── blog/                    # Blog application
│   │   ├── migrations/          # Database migrations
│   │   ├── templates/           # HTML templates
│   │   ├── static/              # CSS, JavaScript, Images
│   │   ├── models.py            # Database models
│   │   ├── views.py             # View logic
│   │   ├── urls.py              # URL routing
│   │   ├── admin.py             # Admin configuration
│   │   └── apps.py              # App configuration
│   ├── django_blog/             # Project configuration
│   │   ├── settings.py          # Project settings
│   │   ├── urls.py              # Main URL router
│   │   ├── wsgi.py              # WSGI configuration
│   │   └── asgi.py              # ASGI configuration
│   ├── manage.py                # Django management script
│   ├── db.sqlite3               # SQLite database
│   └── staticfiles/             # Compiled static files
├── venv/                        # Virtual environment (Python packages)
├── requirements.txt             # Project dependencies
└── README.md                    # This file
```

## 📦 Technologies Used

- **Backend**: Django 6.0.3
- **Database**: SQLite3
- **Server**: Gunicorn
- **Frontend**: HTML, CSS, JavaScript
- **Python Version**: 3.x
- **Deployment**: Render

### Dependencies

- Django 6.0.3
- gunicorn 25.3.0
- asgiref 3.11.1
- sqlparse 0.5.5
- tzdata 2025.3
- packaging 26.0

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/ranjeetkanojya39/blog-Application.git
   cd blog-Application
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**

   **On Windows:**
   ```bash
   venv\Scripts\activate
   ```

   **On macOS/Linux:**
   ```bash
   source venv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Navigate to the Django project**
   ```bash
   cd django_blog
   ```

6. **Run migrations** (if needed)
   ```bash
   python manage.py migrate
   ```

7. **Create a superuser** (admin account)
   ```bash
   python manage.py createsuperuser
   ```

8. **Start the development server**
   ```bash
   python manage.py runserver
   ```

9. **Access the application**
   - Main site: [http://localhost:8000](http://localhost:8000)
   - Admin panel: [http://localhost:8000/admin](http://localhost:8000/admin)

## 📊 Database Models

### Posts Model

The main model for storing blog post data:

```python
class Posts(models.Model):
    title = models.CharField(max_length=100)        # Post title
    content = models.TextField()                    # Post content
    date_posted = models.DateTimeField()            # Posting timestamp
    author = models.ForeignKey(User)                # Author reference
```

## 🔐 Security Considerations

- The project currently runs in DEBUG mode. For production, set `DEBUG = False` in settings
- Use environment variables for sensitive data like `SECRET_KEY`
- Configure `ALLOWED_HOSTS` appropriately for production
- Use HTTPS in production

## 📝 Usage

1. **Create a Blog Post**
   - Log in to the admin panel at `/admin`
   - Navigate to Posts
   - Click "Add Post"
   - Fill in the title, content, and author
   - Click "Save"

2. **View Blog Posts**
   - Visit the main page to see all published posts
   - Click on any post to view its full content

3. **Manage Posts**
   - Use the admin panel to edit, delete, or manage posts
   - Filter posts by author or date

## 🛠️ Common Commands

```bash
# Run development server
python manage.py runserver

# Create superuser
python manage.py createsuperuser

# Apply migrations
python manage.py migrate

# Create new migrations
python manage.py makemigrations

# Collect static files (for production)
python manage.py collectstatic

# Django shell
python manage.py shell

# Run tests (if any)
python manage.py test
```

## 📂 Directory Descriptions

| Directory | Purpose |
|-----------|---------|
| `django_blog/blog/` | Main blog application |
| `django_blog/django_blog/` | Project configuration and settings |
| `django_blog/static/` | Static assets (CSS, JS, images) |
| `django_blog/staticfiles/` | Collected static files for production |
| `venv/` | Python virtual environment |

## 🌍 Environment Setup

Create a `.env` file for production environment variables:

```
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=your-domain.com
DATABASE_URL=your-database-url
```

## 📞 Support & Contributing

- For issues and feature requests, please open an [issue](https://github.com/ranjeetkanojya39/blog-Application/issues)
- Feel free to fork the repository and submit pull requests

## 📄 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

**Ranjeet Kanojya**
- GitHub: [@ranjeetkanojya39](https://github.com/ranjeetkanojya39)

## 🎓 Learning Resources

- [Django Official Documentation](https://docs.djangoproject.com/)
- [Django for Beginners](https://djangoforbeginners.com/)
- [Python Official Documentation](https://docs.python.org/)

---

**Last Updated**: June 2026

**Status**: Active Development

Feel free to ⭐ this repository if you find it helpful!
