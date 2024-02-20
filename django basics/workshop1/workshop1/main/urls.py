from django.urls import path

from workshop1.main.views import EmptyView

urlpatterns = [
    path('', EmptyView.as_view(), name = ''),
    path('/accounts/register/', EmptyView, name='').
    path('/accounts/login/', EmptyView, name=''),
    path('/accounts/profile/<int:pk>/', EmptyView, name=''),
    path('/accounts/profile/<int:pk>/edit/', EmptyView, name=''),
    path('/accounts/profile/<int:pk>/delete/', EmptyView, name=''),
    path('/pets/add/', EmptyView, name=''),
    path('/pets/<str:username>/pet/<slug:pet_slug>/', EmptyView, name=''),
    path('/pets/<str:username>/pet/<slug:pet_slug>/edit/', EmptyView, name=''),
    path('/pets/<str:username>/pet/<slug:pet_slug>/delete/', EmptyView, name=''),
    path('/pets/<str:username>/pet/<slug:pet_slug>/delete/', EmptyView, name=''),
    path('/photos/add/', EmptyView, name=''),
    path('/photos/<int:pk>/', EmptyView, name=''),
    path('/photos/<int:pk>/edit/', EmptyView, name=''),
]