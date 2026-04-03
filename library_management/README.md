Book Library Management System

Tech Stack:
- Django
- SQLite
- BeautifulSoup

Features:
- Role Based Access Control (Admin, User)
- CRUD operations
- Pagination
- Category filtering
- Web scraping from books.toscrape.com
- Duplicate prevention

Setup Instructions:

1. Create virtual environment
2. Install requirements:
   pip install -r requirements.txt
3. Run migrations:
   python manage.py migrate
4. Create superuser:
   python manage.py createsuperuser
5. Run server:
   python manage.py runserver