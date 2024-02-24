from django.forms import modelform_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from exam.cars.forms import CreateCarForm, DeleteCarForm
from exam.cars.models import Car
from exam.shared.get_profile import get_profile


class CatalogueView(views.ListView):
    queryset = Car.objects.all()
    template_name = 'cars/catalogue.html'
    context_object_name = 'cars'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['car_count'] = self.queryset.count()
        return context


class CreateCarView(views.CreateView):
    queryset = Car.objects.all()
    template_name = "cars/car-create.html"
    success_url = reverse_lazy("catalogue")
    form_class = CreateCarForm

    def form_valid(self, form):
        form.instance.owner_id = get_profile().pk
        return super().form_valid(form)


class DetailCarView(views.DetailView):
    queryset = Car.objects.all()
    template_name = "cars/car-details.html"
    context_object_name = 'car'


class EditCarView(views.UpdateView):
    model = Car
    template_name = "cars/car-edit.html"
    form_class = CreateCarForm
    success_url = reverse_lazy('catalogue')
    context_object_name = 'car'

    def get_queryset(self):
        return super().get_queryset().filter(owner=get_profile().pk)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

class ReadonlyViewMixin:
    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)

        for field in form.fields.values():
            field.widget.attrs["readonly"] = "readonly"

        return form


class DeleteCarView(views.DeleteView):
    model = Car
    template_name = 'cars/car-delete.html'
    success_url = reverse_lazy('catalogue')
    form_class = DeleteCarForm
    context_object_name = 'car'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = DeleteCarForm(instance=self.get_object())
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)


