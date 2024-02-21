from django.shortcuts import render
from django.template.context_processors import request
from django.views import View
from django.views.generic import TemplateView


def EmptyView(request):
    return render(request, 'common/home-page.html')


class HomePage(TemplateView):
    template_name = 'common/home-page.html'

def RegisterUser(request):
    pass
