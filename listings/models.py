from django.db import models
from django.urls import reverse


# Create your models here.


class Realtor(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.TextField(blank=True)
    experience = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        permissions = [('group_realtor', 'Can eat add annonces')]

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name


class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    garage = models.IntegerField(default=0)
    size = models.IntegerField()
    conditioner = models.BooleanField(default=False)
    pool = models.BooleanField(default=False)
    fireplace = models.BooleanField(default=False)
    alarm = models.BooleanField(default=False)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    published = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('listing-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return f"{self.title} - {self.city}"