from django.test import Client, TestCase, RequestFactory
from django.urls import reverse


class TestRegisterView(TestCase):
    def setUp(self):
        self.client = Client()
        self.response = self.client.get(reverse('register'))

    def test_display_register_page(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, "accounts/register.html")
        self.assertContains(self.response, "email")
        self.assertContains(self.response, "username")
        self.assertContains(self.response, "password1")
        self.assertContains(self.response, "password2")

    def test_display_password_reset_complete_page_ok(self):
        response = self.client.get(reverse("password_reset_complete"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/password_reset_complete.html")


class TestLoginView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_display_logout_page(self):
        response = self.client.get(reverse("login"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/login.html")
        self.assertContains(response, "username")
        self.assertContains(response, "password")


class TestPasswordRestView(TestCase):
    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()

    def test_display_password_reset_page(self):
        response = self.client.get(reverse("password_reset"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/password_reset.html")
        self.assertContains(response, "email")

    def test_display_password_reset_done_page_ok(self):
        response = self.client.get(reverse("password_reset_done"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/password_reset_done.html")
