from django.urls import path

from workshop1.main.views import EmptyView, HomePage

urlpatterns = [
    path('', HomePage.as_view(), name=''),
    path('accounts/register/', EmptyView, name='1'),
    path('accounts/login/', EmptyView, name='2'),
    path('accounts/profile/<int:pk>/', EmptyView, name='3'),
    path('accounts/profile/<int:pk>/edit/', EmptyView, name='4'),
    path('accounts/profile/<int:pk>/delete/', EmptyView, name='5'),
    path('pets/add/', EmptyView, name='6'),
    path('pets/<str:username>/pet/<slug:pet_slug>/', EmptyView, name='7'),
    path('pets/<str:username>/pet/<slug:pet_slug>/edit/', EmptyView, name='8'),
    path('pets/<str:username>/pet/<slug:pet_slug>/delete/', EmptyView, name='9'),
    path('pets/<str:username>/pet/<slug:pet_slug>/delete/', EmptyView, name='10'),
    path('photos/add/', EmptyView, name='11'),
    path('photos/<int:pk>/', EmptyView, name='12'),
    path('photos/<int:pk>/edit/', EmptyView, name='13'),
]