from django.urls import path

from exam.main.views import index

urlpatterns = [
    path('', index, name='index'),

]