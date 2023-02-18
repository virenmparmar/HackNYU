from django.test import TestCase
from django.urls import reverse
from .models import ItemListings, User


# Create your tests here.

from django.test import TestCase

class TestUserRegistration(TestCase):
    def setUp(self) -> None:
        self.register_url = reverse("findR:register")
        self.login_url = reverse("findR:login")
        self.add_listing_url = reverse("findR:add_listing")
        return super().setUp()
    
    def test_register(self):
        response = self.client.post(self.register_url, {
            "username": "testuser",
            "password": "testpassword",
            "email": "testemail@gmail.com",
            "first_name": "test",
            "last_name": "user",
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "login.html")
        self.assertEquals(User.objects.get(username="testuser").first_name, "test")
