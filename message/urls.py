from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name="contact-message"),
    path('message-dashboard/', views.message_contact, name="message-dashboard"),
]