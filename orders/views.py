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
from django.contrib.auth import login, authenticate # 9/28/ 19 from https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html
from django.contrib.auth.forms import UserCreationForm # 9/28/ 19 from https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html
from orders.models import Regularpizza,Topping, Salad, Pasta, Order, User
from orders.forms import PlaceOrderForm # TODO: see if we can delete Added 11/13/19 per Django documentation

import os, datetime
from datetime import date, datetime
import json
import requests
# TODO see if we can delete the next two lines
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder

from django.template import Context, Template, loader
from django.views.decorators.csrf import csrf_exempt # from https://stackoverflow.com/questions/16458166/how-to-disable-djangos-csrf-validation

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
    print("94 index menu_nav: ",request)
    menuheader_display=["Pizzas","Pastas","Salads"]
    menuheaders_displayedJSON = json.loads(menuheader_display)
    # TODO: Access this file with an
    return menuheaders_displayed;


def add_toppings(request, foodnameID):
    print("124 add_toppings request: ",request)
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
    return render(request, 'orders/add_toppings.html/', context=context)


def review_order(request):
    print("154 review_order request: ",request)
    """Allows the customer to review and edit the order"""
    context = {
    'user_is_authenticated':request.user.is_authenticated,
    }
    return render(request, 'orders/review_order.html', context=context)


def place_order(request):
    print("187 place_order request: ",request, request.user.is_authenticated)
    context = { #TODO Delete if not needed
    'user_is_authenticated':request.user.is_authenticated,
    }
    if request.user.is_authenticated:
        print("189: TODO - add next screen")
        return render(request, 'orders/get_orderJS')
    # this sent the html file,
    # but did not execute the javascript file
    return render(request, 'orders/place_order.html', context=context)
    # return render(request, 'orders/place_order.html', context=context)

def get_orderJS(request):
    print("201 place_order request: ",request, request.user.is_authenticated)
    context = {
    'user_is_authenticated':request.user.is_authenticated,
    }
    orderdataJSON = request.POST['orderdataJSON']
    orderdataJSON = json.loads(orderdataJSON)
    print("208: orderdataJSON: ", orderdataJSON)
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
        print("217: order_item",order_item,"\n")

        if order_item["foodtype"]=="regularpizza":
            print("219: need to resolve by name and number of toppings for pizza")

        if order_item["foodtype"]=="pasta":
            print("224: order_item",order_item)
            order_item_data = Pasta.objects.filter(name=order_item["foodname"])
            for item in order_item_data:
                print("227 item; ",item)
                add_to_Order_model(customer_id,customer_name, ordertime, order_item)

        if order_item["foodtype"]=="salad":
            order_item_data = Salad.objects.filter(name=order_item["foodname"])
            for item in order_item_data:
                add_to_Order_model(customer_id,customer_name, ordertime, order_item)
# Retrieve order data
    ordername = customer_name + "-" + ordertime.strftime("%m/%d/%Y, %H:%M:%S")
    current_order = Order.objects.filter(name=ordername)
    orderJSONSTR = order_history_to_JSON(current_order)
    for item in current_order: # for debugging 11/02/19
        print("241 item:",item.foodtype)
    context = {
    'orderJSONSTR': orderJSONSTR,
    'current_order': current_order,
    }

    return render(request, 'orders/order_list.html',context=context)


# TODO: Do we use this?
# def checkout(request):
#         print("163 checkout request: ",request)
#         ## Retrieve_order starts here:
#         order_list = {}
#         foodprice = 0.0
#         try:
#             #print("235 retrieve_order data: ",data)
#             print("213")
#         except:
#             print("237 not able to print checkout data\n")
#             print("238 request.method: ",request.method)
#         orderdata = request.GET.get("orderdata")
#         print("229: ", orderdata)
#         orderdataJSON = json.loads(orderdata)
#         # print("258: ",context)
#         if request.user.is_authenticated:
#             customer_id = request.user.id
#             user = User.objects.get(id=customer_id)
#             customer_name = user.username
#         else:
#             customer_id = 0
#             customer_name = "guest"
#             # Create time date stamp
#             #ordertime = datetime.now() #commented out 11/2/19
#         ordertime = timezone.now()
#         # ordername = customer_name + "-" + ordertime.strftime("%m/%d/%Y, %H:%M:%S") # TODO: comment out
#             # Loop through orderdata and create records in Order Model
#         for order_item in orderdataJSON:
#             print("245: order_item",order_item,"\n")
#             print("246: ",order_item["foodtype"],order_item["foodnameID"],"\n")
#             foodtype = order_item["foodtype"]
#             #TODO comment out assignments
#             # if order_item["foodtype"]=="regularpizza":
#             if foodtype=="regularpizza":
#                 #print("\n",order_item,"\n")
#                 order_item_data = Regularpizza.objects.get(id=int(order_item["foodnameID"]))
#                 #print("Retrieved: ",order_item_data)
#                 print("need to resolve by name and number of toppings for pizza")
#                 # retrieve query that matches foodnameID
#                 # set foodtype, foodname, foodnameID,toppings (if pizza),foodprice and qty in Orders Model
#                 #if order_item["foodtype"]=="pasta":
#             if foodtype=="pasta":
#                 print("order_item",order_item)
#                 order_item_data = Pasta.objects.get(name=order_item["foodname"])
#                 print("283 Retrieved: ",order_item_data)
#
#                 current_order = Order.objects.filter(name=ordername)
#                 print("284 current_order:",current_order)
#                 # for item in Pasta.objects.all():
#                 for item in order_item_data:
#                     foodprice = item.price
#                     print ("287: ",item,item.price, foodprice)
#                     # set foodtype, foodname, foodnameID,toppings (if pizza),foodprice and qty in Orders Model
#                     # try to make a function
#                     # foodtype = order_item["foodtype"]
#                     order_item_model = Order(
#                     name = ordername,
#                     customer_id = customer_id,
#                     orderdate = ordertime,
#                     foodtype = foodtype, #order_item["foodtype"],
#                     foodname = order_item["foodname"],
#                     foodnameID = order_item["foodnameID"],
#                     qty = order_item["foodnameID"],
#                     foodprice = item.price
#                     # add foodrating
#                     )
#                     order_item_model.save()
#
#
#             if foodtype=="salad":
#                 print("306: order_item",order_item)
#                 order_item_data = Salad.objects.get(name=order_item["foodname"])
#                 print("308:Retrieved: ",order_item_data)
#                 # print("309: Salad.objects.all()",Salad.objects.all())
#                 # foodname = order_item["foodname"]
#                 # print("311 foodname: ",foodname)
#                 # foodnameID = order_item["foodnameID"]
#                 # qty = order_item["qty"]
#                 current_order = Order.objects.filter(name=ordername)
#                 print("316 order_item_data: ", order_item_data)
#                 for item in current_order:
#                     # foodprice = item.price
#                     # print (item,item.price, foodprice)
#                     #TODO: Pass dictionary instead of individual items
#                     add_to_Order_model(ordername,customer_id,ordertime,order_item_data,foodtype,foodname,foodnameID,qty,foodprice)
#                 # Retrieve order from the model and convert to JSON string to pass to javascript
#
#                 #print("320 current_order",current_order)
#                 # for item in current_order: # for debugging 11/02/19
#                 #     print("321 item:",item.foodtype)
#                 orderJSONSTR = order_history_to_JSON(current_order)
#             #TODO change single quotes to double quotes
#             # User orderJSON for debugging        orderJSON = order_history_to_JSON(current_order)
#             print("328: orderJSONSTR: ",orderJSONSTR)
#             #context['orderJSONSTR']=orderJSONSTR
#             #TODO put in hidden field in html file and then have js put in sessionStorage
#             #confirmed_orderdata = json.dumps(orderdataJSON)
#             print("334 context:",order_list,type(order_list['orderJSONSTR']))
#
#             # TODO: Repeat for other menu items
#
#             # Go to Order Placed
#             # Order placed:
#             #   Retrieve records with last time stamp and customer_id
#             #   Display order with total
#             #   Add buttons for order history and review
#             # Or:
#             #   Display message that the order has been placed
#             #   Clear sessionStorage
#             #   Logout and return to menu
#
#             # print("254: request",request) # problem:request <WSGIRequest: GET '/orders/orders/retrieve_order/?
#             # return HttpResponse("255 retrieve_order") #Not Found: /orders/orders/checkout/ qed response object wrohg
#             # print("263 request: ",request,"\n",dir(HttpRequest),"\n",HttpRequest,"\n")
#             print("354 path_info:\n",request.path_info)
#             # request_confirm = request.GET.copy()
#             # request_confirm = copy.deepcopy(request TypeError: cannot serialize '_io.BufferedReader' object
#             #  = request.GET.get('orders/confirm_order.html').copy()
#             # print("266: ",request_confirm,"\n",request.GET,"\n",dir(request.GET))
#             #return HttpResponse("checkout not found")
#             # print("267: ", request.getlist) 'WSGIRequest' object has no attribute 'getlist'
#             # return HttpResponse(template.render(context, request))
#             # redirect has a copy of retrieve order
#             # return redirect('/orders/confirm_order.html', context=context) # .html needed, executes confirm_order in views but not .html file
#             # Request is a repeat of retrieve order data
#             # return render(request, 'orders/order_list.html',context=context)
#             ## Retrieve_order ends here:
#             return render(request, 'orders/checkout.html')

# TODO: can we delete this?
def retrieve_order(request,data):
    print("417 retrieve_order request",request)
    order_list = {}
    foodprice = 0.0
    try:
        print("420 retrieve_order data: ",data)
    except:
        print("422 not able to print retrieve_order data\n")
        print("423 request.method: ",request.method)
    orderdata = request.GET.get("orderdata")
    orderdataJSON = json.loads(orderdata)
    if request.user.is_authenticated:
        customer_id = request.user.id
        user = User.objects.get(id=customer_id)
        customer_name = user.username
    else:
        customer_id = 0
        customer_name = "guest"
    # Create time date stamp
    ordertime = timezone.now()
    ordername = customer_name + "-" + ordertime.strftime("%m/%d/%Y, %H:%M:%S") #TODO Comment out
    # Loop through orderdata and create records in Order Model
    for order_item in orderdataJSON:
        print("452: order_item",order_item,"\n")
        if order_item["foodtype"]=="regularpizza":
            order_item_data = Regularpizza.objects.get(id=int(order_item["foodnameID"]))
            #print("Retrieved: ",order_item_data)
            print("need to resolve by name and number of toppings for pizza")
        if order_item["foodtype"]=="pasta":
                print("464: order_item",order_item)
                order_item_data = Pasta.objects.filter(name=order_item["foodname"])
                print("466 Retrieved: ",order_item_data)
                for item in order_item_data:
                    if True:
                        foodprice = item.price
                        print ("287: ",item,item.price, foodprice)
                        order_item_model = Order(
                        name = ordername,
                        customer_id = customer_id,
                        orderdate = ordertime,
                        foodtype = order_item["foodtype"],
                        foodname = order_item["foodname"],
                        foodnameID = order_item["foodnameID"],
                        qty = order_item["qty"],
                        foodprice = item.price
                        # TODO add foodrating
                        )
                        order_item_model.save()

        if order_item["foodtype"]=="salad":
            print("484: order_item",order_item)
            order_item_data = Salad.objects.filter(name=order_item["foodname"])
            for item in order_item_data:
                print("486 item; ",item)
                # foodname = order_item["foodname"]
                # foodnameID = order_item["foodnameID"]
                # qty = order_item["qty]
                # foodprice = order_item_data.price
                print("491 order_item price: ",order_item,foodprice)
                add_to_Order_model(customer_id,customer_name, ordertime, order_item)
            # orderJSONSTR = order_history_to_JSON(current_order) commented out 11/16/19
            # print("444: orderJSONSTR: ",orderJSONSTR)
            # for item in Salad.objects.all():
            #     foodprice = item.price
            #     print (item,item.price, foodprice)
            #     #TODO: Pass dictionary instead of individual items
            #     add_to_Order_model(ordername,customer_id,ordertime,order_item_data,foodtype,foodname,foodnameID,qty,foodprice)
            #
            #     orderJSONSTR = order_history_to_JSON(current_order)
            #     print("490: orderJSONSTR: ",orderJSONSTR)

            # TODO: Repeat for other menu items

    print("496 path_info: ",request.path_info)
    # request_confirm = request.GET.copy()
    # request_confirm = copy.deepcopy(request TypeError: cannot serialize '_io.BufferedReader' object
    #  = request.GET.get('orders/confirm_order.html').copy()
    # print("266: ",request_confirm,"\n",request.GET,"\n",dir(request.GET))
    #return HttpResponse("checkout not found")
    # print("267: ", request.getlist) 'WSGIRequest' object has no attribute 'getlist'
    # return HttpResponse(template.render(context, request))
    # redirect has a copy of retrieve order
    # return redirect('/orders/confirm_order.html', context=context) # .html needed, executes confirm_order in views but not .html file
    # Request is a repeat of retrieve order data
    current_order = Order.objects.filter(name=ordername)
    orderJSONSTR = order_history_to_JSON(current_order)
    print("469 current_order",current_order)
    for item in current_order: # for debugging 11/02/19
        print("711 item:",item.foodtype)
    context = {
    'orderJSONSTR':orderJSONSTR,
    }
    print("474 context",context)
    # return redirect('/',context=context)
    # render ' ' and '/' do not work
    # return HttpResponse("477 Still Trying")
    # return render(request, 'order_list',context=context)
    # return redirect('orders/order_list.html',context=context) #Not Found: /orders/orders/retrieve_order/orders/order_list.html
    return render(request, 'orders/order_list.html',context=context) # url does not update

def order_history_to_JSON(order_query):
    """
    Input is a queary set; output isa JSON string suitable for passing to javascript.
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


# pre 11/22/19 version def add_to_Order_model(ordername,customer_id,ordertime, order_item,foodtype,foodname,foodnameID,qty,foodprice):
def add_to_Order_model(customer_id,customer_name, ordertime, order_item):
    print("775 add_to Order_model: ",order_item)
    order_item_model = Order(
    customer_id = customer_id,
    # ordername = customer_name + "-" + ordertime.strftime("%m/%d/%Y, %H:%M:%S"),
    name = customer_name + "-" + ordertime.strftime("%m/%d/%Y, %H:%M:%S"),
    orderdate = ordertime,
    foodtype = order_item["foodtype"],
    foodname = order_item["foodname"],
    foodnameID = order_item["foodnameID"],
    qty = order_item["qty"],
    foodprice = order_item["foodprice"],
        # add foodrating
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
