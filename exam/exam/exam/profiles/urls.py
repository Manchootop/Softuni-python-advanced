from django.urls import path

from exam.profiles.views import create_profile, DetailProfileView, DeleteProfileView, EditProfileView

urlpatterns = (
    path("details/", DetailProfileView.as_view(), name="details profile"),
    path("delete/", DeleteProfileView.as_view(), name="delete profile"),
    path("create-profile/", create_profile, name="create profile"),
    path("edit/", EditProfileView.as_view(), name="edit profile"),

)