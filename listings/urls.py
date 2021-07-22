from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListingsListView.as_view(), name="listing-list"),
    path('detail/<int:pk>/', views.ListingsDetail.as_view(), name="listing-detail"),
    path('new/', views.ListingsCreateView.as_view(), name="listing-create"),
]