from django.db.models import Sum
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from exam.cars.models import Car
from exam.profiles.forms import ProfileForm, CreateProfileForm
from exam.profiles.models import Profile
from exam.shared.get_profile import get_profile


class DetailProfileView(views.DetailView):
    template_name = "profiles/profile-details.html"
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        return get_profile()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total_price = Car.objects.filter(owner=get_profile().pk).aggregate(Sum('price'))['price__sum'] or 0
        context['total_price'] = total_price
        print(total_price)
        return context


class DeleteProfileView(views.DeleteView):
    template_name = "profiles/profile-delete.html"
    context_object_name = 'profile'
    success_url = reverse_lazy("index")

    def get_object(self, queryset=None):
        return get_profile()


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')  # Redirect to a success page
    else:
        form = ProfileForm()
    return render(request, 'profiles/profile-create.html', {'form': form})


class EditProfileView(views.UpdateView):
    template_name = "profiles/profile-edit.html"
    form_class = ProfileForm
    success_url = reverse_lazy('details profile')
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        return get_profile()
