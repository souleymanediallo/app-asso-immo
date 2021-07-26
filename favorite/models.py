from django.db import models
from django.contrib.auth import get_user_model
from listings.models import Listing

User = get_user_model()


class Favorite(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Listing, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f" {self.username} "
