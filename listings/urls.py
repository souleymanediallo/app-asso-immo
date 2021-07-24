from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListingsListView.as_view(), name="listing-list"),
    path('detail/<int:pk>/', views.ListingsDetail.as_view(), name="listing-detail"),
    path('detail/<int:pk>/update/', views.ListingsUpdateView.as_view(), name='listing-update'),
    path('detail/<int:pk>/delete/', views.ListingsDeleteView.as_view(), name='listing-delete'),
    path('new/', views.ListingsCreateView.as_view(), name="listing-create"),
    path('my-listing/', views.my_listing, name="my-listing"),
]
