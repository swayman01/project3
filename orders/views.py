from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.utils import timezone
# from django.views.generic.list import ListView, DetailView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy, path
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from orders.models import Regularpizza,Topping, Salad, Pasta, Order

import os
import json
from django.core.serializers.json import DjangoJSONEncoder

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# TODO: Add login requirements
# TODOs:
# If logged in:
#  retrieve history and bold previously ordered items
#    add ability to thumbs up of thumbs down
# Shopping Cart
#   Modify
#   option to login to save history

def index(request):
    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    foodnames = {"regularpizzas":"regularpizza","toppings":"topping","pastas":"pasta","salads":"salad"}
    regularpizzaDICT = {
    'QuerySet': Regularpizza.objects.all(),
    'menutype': 'regularpizza',
    'menuheader': 'Regular Pizza',
    'menuformat': 3,
    'foodname': 'regularpizza',
    'toppings': 'topping'
    }
    toppingDICT = {
    'QuerySet': Topping.objects.all(),
    'menutype': 'Topping',
    'menuheader': 'Toppings',
    'menuformat': 0,
    'foodname': 'topping',
    }
    pastaDICT = {
    'QuerySet': Pasta.objects.all(),
    'menutype': 'Pasta',
    'menuheader': 'Pastas',
    'menuformat': 1,
    'foodname': 'pasta',
    }
    saladDICT = {
    'QuerySet': Salad.objects.all(),
    'menutype': 'Salad',
    'menuheader': 'Salads',
    'menuformat': 1,
    'foodname': 'salad',
    }
    foodtypes = [regularpizzaDICT,toppingDICT, pastaDICT, saladDICT]
    manager = "manager"
# experimental code
    # reqularpizzadbLIST = []
    # reqularpizzadbDICT = {}
    # for e in Regularpizza.objects.all():
    #     print(e.id,e.smallprice,e.largeprice,e.name,e.numtoppings)
    #     f= {str(e.id): {'regularpizzaID': e.id,
    #     'smallprice':str(e.smallprice),
    #     'largeprice':str(e.largeprice),
    #     'name':e.name,
    #     'numtoppings':e.numtoppings,
    #     }}
    #     reqularpizzadbDICT.update(f)
    #     #print("125 f:",f)
    #     reqularpizzadbLIST.append(json.dumps(f))
    #     #regularpizzadbSTR = json.dumps(f)
    #     #print("regularpizzadbSTR ",regularpizzadbSTR,type(regularpizzadbSTR))
    # #reqularpizzadbLIST = list(Regularpizza.objects.all())
    # print("81 reqularpizzadbDICT:",reqularpizzadbDICT,type(reqularpizzadbDICT))
    # print("***")
    # regularpizzadbSTR = json.dumps(reqularpizzadbDICT, cls=DjangoJSONEncoder)

    menuheader_display=["Pizzas","Pastas","Salads"]
    menuheaders_displayedJSON = json.dumps(menuheader_display)


    context = {
        'regularpizzas_all': Regularpizza.objects.all(),
        'toppings_all': Topping.objects.all(),
        'pastas_all': Pasta.objects.all(),
        'salads_all': Salad.objects.all(),
        'num_visits': num_visits,
        'foodtypes': foodtypes,
        'foodnames': foodnames,
        'manager': manager,
        'menuheaders_displayedJSON': menuheaders_displayedJSON,
    }
    return render(request, 'menu.html/',context=context)

# def menu(request): # Commented out 9/19/19, works as long as url.py line is commented out
#     print("line 74 is def menu used?")
#     # Number of visits to this view, as counted in the session variable.
#     num_visits = request.session.get('num_visits', 0)
#     request.session['num_visits'] = num_visits + 1
#     context = {
#         'reqularpizzas_all': Regularpizza.objects.all(),
#         'toppings_all': Topping.objects.all(),
#         'pastas_all': Pasta.objects.all(),
#         'salads_all': Salad.objects.all(),
#         'num_visits': num_visits,
#     }
#     return render(request, 'menu.html', context=context)


def menu_nav(request, menuheader_displayedJSON):
    menuheader_display=["Pizzas","Pastas","Salads"]
    menuheaders_displayedJSON = json.loads(menuheader_display)
    # TODO: Access this file with an
    return menuheaders_displayed;


def add_toppings(request, foodnameID):
    pizzatypeDICT = {
    4:0,  # 0 signifies Regular Pizza
    8:0,
    9:0,
    7:0,
    12:2, # 1 signifies Regular Pizza Special
    }
    get1 = Regularpizza.objects.get(id=foodnameID)
    # print("136 get1:", get1)
    numtoppings = get1.numtoppings
    smallprice = get1.smallprice
    largeprice = get1.largeprice
    foodtype = get1.foodtype
    # print("136 foodtype:",foodtype,", foodnameID:",foodnameID, "numtoppings:",numtoppings)
    # print("140 numtoppings, smallprice, largeprice:",numtoppings, smallprice, largeprice)
    pizzatype  = pizzatypeDICT[foodnameID]
    context = {
        'foodnameID': foodnameID,
        'reqularpizzas_all': Regularpizza.objects.all(),
        'toppings_all': Topping.objects.all(),
        'numtoppings': numtoppings,
        'pizzatype': pizzatype,
        'smallprice': smallprice,
        'largeprice': largeprice,
        # 'foodtype': foodtype,
        }
    return render(request, 'orders/add_toppings_experiment.html/', context=context)


def add_toppings_experiment(request):
    print("add_toppings_experiment: no argument")
    #TODO remove this here and from urls
    numtoppingsDICT = {
        4:0,
        8:1,
        9:2,
        7:3,
        12:'special',
    }
    numtoppings = "placholder, fix when passing ID"
    foodnameID = "stub"

    context = {
        'foodnameID': foodnameID,
        'reqularpizzas_all': Regularpizza.objects.all(),
        'toppings_all': Topping.objects.all(),
        'numtoppings': numtoppings,
    }
    print("139request:",request)

    #return render(request, 'menu.html/',context=context)
    return render(request, 'orders/add_toppings_experiment.html/', context=context)

def review_order(request): # Commented out 8/26/19 and failed
    """Allows the customer to review and edit the order"""
    # Read the object
    # TODO: decide on checks
    # Pass it to review_order.html

    context = {

    }
    return render(request, 'orders/review_order.html', context=context)

class RegularpizzaListView(generic.ListView):
    model = Regularpizza

class RegularpizzaDetailView(generic.DetailView):
    model = Regularpizza
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(RegularpizzaDetailView, self).get_context_data(**kwargs)
        context['Regularpizzas_all']=Regularpizza.objects.all()
        foodtypes = ["regularpizzas"]
        foodname = "regularpizza"
        context['foodtypes'] = foodtypes
        context['foodname'] = foodname
        return context

class RegularpizzaCreate(CreateView):
    model = Regularpizza
    # fields = '__all__'
    fields = ['name', 'smallprice', 'largeprice', 'numtoppings']
    success_url = reverse_lazy('index')

class RegularpizzaUpdate(UpdateView):
    model = Regularpizza
    # fields = '__all__'
    fields = ['name', 'smallprice', 'largeprice', 'numtoppings']
    success_url = reverse_lazy('index')

class RegularpizzaDelete(DeleteView):
    model = Regularpizza
    success_url = reverse_lazy('index')

class ToppingListView(generic.ListView):
    model = Topping

class ToppingDetailView(generic.DetailView):
    model = Topping
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(ToppingDetailView, self).get_context_data(**kwargs)
        context['Toppings_all']=Topping.objects.all()
        foodtypes = ["toppings"]
        foodname = "topping"
        context['foodtypes'] = foodtypes
        context['foodname'] = foodname
        return context

class ToppingCreate(CreateView):
    model = Topping
    #SOMEDAY: Find a way to pass the model as an argument,
    # See https://stackoverflow.com/questions/6724052/django-pass-model-name-as-parameter-to-decorator
    fields = '__all__'
    success_url = reverse_lazy('index')

class ToppingUpdate(UpdateView):
    model = Topping
    fields = '__all__'
    success_url = reverse_lazy('index')

class ToppingDelete(DeleteView):
    model = Topping
    success_url = reverse_lazy('index')

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
