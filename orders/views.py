from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.utils import timezone
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy, path
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth import login, logout, authenticate # 9/28/ 19 from django documentation and https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html
from django.contrib.auth.forms import UserCreationForm # 9/28/ 19 from https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html
from orders.models import Regularpizza,Topping, Salad, Pasta, Order, User
from orders.forms import PlaceOrderForm # TODO: see if we can delete Added 11/13/19 per Django documentation

import os, datetime
from datetime import date, datetime
import json
import requests
# TODO see if we can delete the next two lines - commented out 12/12/19
# from django.http import JsonResponse
# from django.core.serializers.json import DjangoJSONEncoder

from django.template import Context, Template, loader
from django.views.decorators.csrf import csrf_exempt # from https://stackoverflow.com/questions/16458166/how-to-disable-djangos-csrf-validation
from decimal import Decimal

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def index(request):
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    foodnames = {"regularpizzas":"regularpizza","toppings":"topping","pastas":"pasta","salads":"salad"}
    regularpizzaDICT = {
    'QuerySet': Regularpizza.objects.all(),
    'menutype': 'regularpizza',
    'menuheader': 'Regular Pizza',
    'menuheader_no_blanks': 'Regular_Pizza', # for use in css class
    'menuformat': 3,
    'foodname': 'regularpizza',
    'toppings': 'topping'
    }
    toppingDICT = {
    'QuerySet': Topping.objects.all(),
    'menutype': 'Topping',
    'menuheader': 'Toppings',
    'menuheader_no_blanks': 'Toppings',
    'menuformat': 0,
    'foodname': 'topping',
    }
    pastaDICT = {
    'QuerySet': Pasta.objects.all(),
    'menutype': 'Pasta',
    'menuheader': 'Pastas',
    'menuheader_no_blanks': 'Pastas',
    'menuformat': 1,
    'foodname': 'pasta',
    }
    saladDICT = {
    'QuerySet': Salad.objects.all(),
    'menutype': 'Salad',
    'menuheader': 'Salads',
    'menuheader_no_blanks': 'Salads',
    'menuformat': 1,
    'foodname': 'salad',
    }
    foodtypes = [regularpizzaDICT,toppingDICT, pastaDICT, saladDICT]
    manager = "manager"
    context = {
        'regularpizzas_all': Regularpizza.objects.all(),
        'toppings_all': Topping.objects.all(),
        'pastas_all': Pasta.objects.all(),
        'salads_all': Salad.objects.all(),
        'num_visits': num_visits,
        'foodtypes': foodtypes,
        'foodnames': foodnames,
        'manager': manager,
    }
    return render(request, 'menu.html/',context=context)


def menu_nav(request, menuheader_displayedJSON):
    # print("94 index menu_nav: ",request)
    menuheader_display=["Pizzas","Pastas","Salads"]
    menuheaders_displayedJSON = json.loads(menuheader_display)
    return menuheaders_displayed;


def add_toppings(request, foodnameID):
    print("124 add_toppings request: ",request)
    pizzatypeDICT = {
    4:0,  # 0 signifies Regular Pizza, 4 no toppings
    8:0,  # 1 topping
    9:0,  # 2 toppings
    7:0,  # 3 toppings
    12:2, # Regular Pizza Special
    }
    get1 = Regularpizza.objects.get(id=foodnameID)
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
    return render(request, 'orders/add_toppings.html/', context=context)


def review_order(request):
    """Allows the customer to review and edit the order"""
    print("123 review_order request: ",request, request.path)
    next = request.path
    context = {
    'user_is_authenticated':request.user.is_authenticated,
    'next':next
    }
    print ("129 review_order context:", context)
    return render(request, 'orders/review_order.html', context=context)


def place_order(request):
    print("131 place_order request: ",request, request.user.is_authenticated)
    context = { #TODO Delete if not needed
    'user_is_authenticated':request.user.is_authenticated,
    'next': '/orders/review_order.html' #Needed because of how we pass json
    }
    print ("139 place_order context:", context)
    if request.user.is_authenticated:
        print("136 request: ",request)
        return redirect('get_orderJS')
        #return render(request, 'orders/get_orderJS')
        #return render(request, 'orders/place_order.html', context=context) - commented out 12/16/19
    # this sent the html file,
    # but did not execute the javascript file
    return render(request, 'orders/place_order.html', context=context)


def get_orderJS(request):
    print("144 place_order request, user_id.is_authenticated: ",request, request.user.is_authenticated)
    context = {
    'user_is_authenticated':request.user.is_authenticated,
    }
    orderdataJSON = request.POST['orderdataJSON']
    orderdataJSON = json.loads(orderdataJSON)
    print("152: orderdataJSON: ", orderdataJSON)
    if request.user.is_authenticated:
        customer_id = request.user.id
        user = User.objects.get(id=customer_id)
        customer_name = user.username
    else:
        customer_id = 0
        customer_name = "guest"
    # Create time date stamp
    ordertime = timezone.now()
# Loop through orderdata and create records in Order Model
    for order_item in orderdataJSON:
        print("162: order_item",order_item)
# Need If to filter
        if order_item["foodtype"]=="regularpizza":
            #print("165: order_item",order_item)
            # order_item_data =  Regularpizza.objects.filter(foodname=order_item["foodname"])
            order_item_model =  Regularpizza.objects.all()
            for item in order_item_model:
                print("167: ",customer_id,customer_name, ordertime, order_item)
                print("170 item: ",item)
                # if order_item["foodnameID"] == 8 and item.numtoppings == 1:
                try:
                    numtoppings = len(order_item["toppings"])
                except:
                    numtoppings = 0
                if item.numtoppings == numtoppings:
                #if order_item["foodnameID"] == item.foodnameID: # and item["numtoppings"] == numtoppings:
                    print("171 item: !", item.numtoppings, numtoppings)
                # if size, numtoppings equal then add to model
                    add_to_Order_model(customer_id,customer_name, ordertime, order_item)

        if order_item["foodtype"]=="pasta":
            print("224: order_item",order_item)
            order_item_data = Pasta.objects.filter(name=order_item["foodname"])
            for item in order_item_data:
                print("188 item; ",item)
                add_to_Order_model(customer_id,customer_name, ordertime, order_item)

        if order_item["foodtype"]=="salad":
            order_item_data = Salad.objects.filter(name=order_item["foodname"])
            for item in order_item_data:
                print("193 item; ",item)
                add_to_Order_model(customer_id,customer_name, ordertime, order_item)
# Retrieve order data
    ordername = customer_name + "-" + ordertime.strftime("%m/%d/%Y, %H:%M:%S")
    current_order = Order.objects.filter(name=ordername)
    orderJSONSTR = order_history_to_JSON(current_order)
    order_price = Decimal(0.0)
    for item in current_order:
        order_price = order_price + Decimal(item.qty) * Decimal(item.foodprice)
    context = {
    # 'orderJSONSTR': orderJSONSTR, # Commented out 12/11/19
    'current_order': current_order,
    'order_price': order_price,
    }
    print("207 request: ",request)
    # return redirect('order_list') # 12/17/19: This does not return order_price
    return render(request, 'orders/order_list.html',context=context)


def order_history_to_JSON(order_query):
    """
    Input is a queary set; output is a JSON string suitable for passing to javascript.
    """
    orderJSON = []
    for item in order_query:
        x = {"foodtype":item.foodtype,
        "foodnameID":item.foodnameID,
        "foodname":item.foodname,
        "foodprice":str(item.foodprice),
        "qty":item.qty
        }
        orderJSON.append(x)
    orderJSONSTR = json.dumps(orderJSON)
    orderJSONSTR = orderJSONSTR.replace("'",'"')
    # orderJSONSTR = json.dumps(orderJSONSTR) commented out for debugging 11/4/19
    return orderJSONSTR


def add_to_Order_model(customer_id,customer_name, ordertime, order_item):
    print("336 add_to Order_model: ",order_item)
    foodnameID = order_item["foodnameID"]
    foodname = str(order_item["foodname"])
    if foodname == "regularpizza":
        print("340: TODO update for toppings")
        if foodnameID != 8:
            foodname == "Reqular Pizza with " + "Topping names"
    order_item_model = Order(
    customer_id = customer_id,
    name = customer_name + "-" + ordertime.strftime("%m/%d/%Y, %H:%M:%S"),
    orderdate = ordertime,
    foodtype = order_item["foodtype"],
    foodname = foodname,
    foodnameID = foodnameID,
    qty = order_item["qty"],
    foodprice = order_item["foodprice"],
        # TODO add foodrating
        )
    order_item_model.save()
    return

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

    print("572 context:",context)
    print("573 list(Salad.objects.all()):",list(Salad.objects.all()))
    print("574 context['salads__all']:",context['salads_all'][0])
    print("575 context['saladsall']:",context['saladsall'])
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

class OrderListView(generic.ListView):
    model = Order
    def get_context_data(self, **kwargs):
        x1 = Order.objects.first().name
        x2 = Order.objects.filter(name=x1)
        # print("557: ",x1, x2)
        # Call the base implementation first to get the context
        context = super(OrderListView, self).get_context_data(**kwargs)
        context['current_order'] = x2
        # print("558 context: ",context)
        return context

class OrderDetailView(generic.DetailView):
    model = Order
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(OrderDetailView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        #context['authors_all']=Author.objects.all()
        # try filter on last order - hardcode first, then pass variable later
        context['current_order'] = Order.objects.filter('filter')
        return context

class OrderCreate(CreateView):
    model = Order
    fields = '__all__'
    success_url = reverse_lazy('index')

# no reason to allow manager to update view, but keep in for debugging
class OrderUpdate(UpdateView):
    model = Order
    fields = '__all__'
    success_url = reverse_lazy('index')


def signup(request):
    print("319: in signup")
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('place_order')
    else:
        form = UserCreationForm()
    return render(request, 'orders/signup.html', {'form': form})

# modified from https://pythonprogramming.net/user-login-logout-django-tutorial/
def logged_out(request):
    print("567 request: ", request)
    logout(request)
    return render(request, 'orders/logged_out.html')
