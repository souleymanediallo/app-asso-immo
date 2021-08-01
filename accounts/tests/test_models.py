from django.test import TestCase

from accounts.models import CustomUser


class CustomUserModelTests(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            email="malick@mail.com",
            username="Malick",
            password="Django1234",
        )

    def test_simple_user_not_admin_str(self):
        self.assertIs(self.user.is_admin, False)

    def test_superuser_is_admin_str(self):
        superuser = CustomUser.objects.create_superuser(
            email="pape@mail.com",
            username="admin10",
            password="Django1234",
        )
        self.assertIs(superuser.is_admin, True)