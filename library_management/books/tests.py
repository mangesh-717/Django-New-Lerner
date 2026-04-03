from django.test import TestCase
from django.contrib.auth.models import User, Group
from django.urls import reverse
from .models import Book, Category


class BookTests(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name="Test Category")

        self.book = Book.objects.create(
            title="Test Book",
            category=self.category,
            price=10.99,
            description="Test description"
        )

        # Create normal user
        self.user = User.objects.create_user(
            username='user',
            password='user123'
        )

        user_group = Group.objects.get(name='User')
        self.user.groups.add(user_group)

        # Create admin user
        self.admin_user = User.objects.create_user(
            username='admin',
            password='admin123'
        )

        admin_group = Group.objects.get(name='Admin')
        self.admin_user.groups.add(admin_group)

        # Create superuser
        self.superuser = User.objects.create_superuser(
            username='super',
            password='super123'
        )

    def test_user_can_view_books(self):
        self.client.login(username='user', password='user123')

        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Book")

    def test_admin_can_add_book(self):
        self.client.login(username='admin', password='admin123')

        response = self.client.post(reverse('add_book'), {
            'title': 'New Book',
            'category': self.category.id,
            'price': 20.00,
            'description': 'New description'
        })

        self.assertEqual(response.status_code, 302)
        self.assertTrue(Book.objects.filter(title="New Book").exists())

    def test_superuser_can_delete_book(self):
        self.client.login(username='super', password='super123')

        response = self.client.post(
            reverse('delete_book', args=[self.book.id])
        )

        self.assertEqual(response.status_code, 302)
        self.assertFalse(Book.objects.filter(id=self.book.id).exists())