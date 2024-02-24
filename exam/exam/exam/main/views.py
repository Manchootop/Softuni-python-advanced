from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from exam.cars.models import Car
from exam.shared.get_profile import get_profile


def index(request):
    context = {}

    return render(request, "main/index.html", context)



