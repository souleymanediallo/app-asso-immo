from django.test import Client, TestCase
from django.urls import reverse


class TestView(TestCase):
    def setUp(self):
        self.client = Client()
        self.response = self.client.get(reverse('listing-list'))

    def test_listing_page(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, "listings/listing_list.html")



