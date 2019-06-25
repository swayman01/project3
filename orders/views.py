from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.utils import timezone
# from django.views.generic.list import ListView, DetailView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from orders.models import Salad, Pasta

# TODO: Add login requirements
def index(request):
    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    foodnames = {"pastas":"pasta","salads":"salad"}
    pastaDICT = {
    'QuerySet': Pasta.objects.all(),
    'menutype': 'Pasta',
    'foodname': 'pasta',
    }
    saladDICT = {
    'QuerySet': Salad.objects.all(),
    'menutype': 'Salad',
    'foodname': 'salad',
    }
    foodtypes = [pastaDICT, saladDICT]
    context = {
        'pastas_all': Pasta.objects.all(),
        'salads_all': Salad.objects.all(),
        'num_visits': num_visits,
        'foodtypes': foodtypes,
        'foodnames': foodnames,
    }
    return render(request, 'menu.html/',context=context)

def menu(request):
    print("line 45 is def menu used?")
    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    #all = 'all'
    context = {
        'pastas_all': Pasta.objects.all(),
        'salads_all': Salad.objects.all(),
        'num_visits': num_visits,
    }
    return render(request, 'menu.html', context=context)

class PastaListView(generic.ListView):
    model = Pasta

class PastaDetailView(generic.DetailView):
    model = Pasta
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(PastaDetailView, self).get_context_data(**kwargs)
        context['Pastas_all']=Pasta.objects.all()
        foodtypes = ["pastas"]
        foodname = "pasta"
        context['foodtypes'] = foodtypes
        context['foodname'] = foodname
        return context

class PastaCreate(CreateView):
    model = Pasta
    #SOMEDAY: Find a way to pass the model as an argument,
    # See https://stackoverflow.com/questions/6724052/django-pass-model-name-as-parameter-to-decorator
    fields = '__all__'
    success_url = reverse_lazy('index')

class PastaUpdate(UpdateView):
    model = Pasta
    fields = '__all__'
    success_url = reverse_lazy('index')

class PastaDelete(DeleteView):
    model = Pasta
    success_url = reverse_lazy('index')

def salads(request):
    # TODO: do we need this?
    print("90: do we need this? ")
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['salads_all'] = list(Salad.objects.all()),
        context['saladsall'] = Salad.objects.all(),
        context['num_visits'] = num_visits,
        return context
    context = {
        'salads_all': list(Salad.objects.all()),
        'num_visits': num_visits,
        'saladsall': Salad.objects.all(),
    }

    print("36 context:",context)
    print("37 list(Salad.objects.all()):",list(Salad.objects.all()))
    print("38 context['salads__all']:",context['salads_all'][0])
    print("39 context['saladsall']:",context['saladsall'])
    return render(request, 'orders/salads.html', context=context)

class SaladListView(generic.ListView):
    model = Salad

class SaladDetailView(generic.DetailView):
    model = Salad
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(SaladDetailView, self).get_context_data(**kwargs)
        context['Salads_all']=Salad.objects.all()
        foodtypes = ["salads"]
        foodname = "salad"
        context['foodtypes'] = foodtypes
        context['foodname'] = foodname
        return context

class SaladCreate(CreateView):
    model = Salad
    fields = '__all__'
    success_url = reverse_lazy('index')

class SaladUpdate(UpdateView):
    model = Salad
    fields = '__all__'
    success_url = reverse_lazy('index')

class SaladDelete(DeleteView):
    model = Salad
    success_url = reverse_lazy('index')
