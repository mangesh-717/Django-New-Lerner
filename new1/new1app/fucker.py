import os
import django
from faker import Faker
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')
application = get_wsgi_application()
django.setup()

from new1app.models import student
from django.contrib.auth.models import User

fake = Faker()

# Create fake users
for _ in range(5):
    fake_name = fake.name()
    fake_email = fake.email()
    user = User.objects.create(username=fake_name, email=fake_email, password=fake.password())

    # Create fake students
    student.objects.create(
        name=fake_name,
        about=fake.text(),
        email=fake_email,
        Users=user,
        photo=fake.image_url(),
    )
