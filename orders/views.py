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
from orders.models import Regularpizza, Sicilianpizza, Topping, Salad, Pasta
from orders.models import Sub, Dinnerplatter, Order, User, Rating
import os, datetime
from datetime import date, datetime
import json
import requests
import itertools
from django.template import Context, Template, loader
from django.views.decorators.csrf import csrf_exempt # from https://stackoverflow.com/questions/16458166/how-to-disable-djangos-csrf-validation
from decimal import Decimal

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def index(request):
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    foodnames = {"regularpizzas":"regularpizza","sicilianpizzas":"sicilianpizza",
    "toppings":"topping","pastas":"pasta","salads":"salad","subs":"subs"}
    regularpizzaDICT = {
    'QuerySet': Regularpizza.objects.all(),
    'menutype': 'regularpizza',
    'menuheader': 'Regular Pizza',
    'menuheader_no_blanks': 'Regular_Pizza', # for use in css class
    'menuformat': 3,
    'foodname': 'regularpizza',
    'toppings': 'topping'
    }
    sicilianpizzaDICT = {
    'QuerySet': Sicilianpizza.objects.all(),
    'menutype': 'sicilianpizza',
    'menuheader': 'Sicilian Pizza',
    'menuheader_no_blanks': 'Regular_Pizza', # for use in css class
    'menuformat': 3,
    'foodname': 'sicilianpizza',
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
    subDICT = {
    'QuerySet': Sub.objects.all(),
    'menutype': 'Sub',
    'menuheader': 'Subs',
    'menuheader_no_blanks': 'Subs',
    'menuformat': 3,
    'foodname': 'sub',
    }
    dinnerplatterDICT = {
    'QuerySet': Dinnerplatter.objects.all(),
    'menutype': 'Dinnerplatter',
    'menuheader': 'Dinner Platters',
    'menuheader_no_blanks': 'Dinnerplatters',
    'menuformat': 3,
    'foodname': 'dinnerplatter',
    }
    foodtypes = [regularpizzaDICT,sicilianpizzaDICT,toppingDICT, pastaDICT, saladDICT, subDICT, dinnerplatterDICT]
    manager = "manager"
    context = {
        'regularpizzas_all': Regularpizza.objects.all(),
        'sicilianpizzas_all': Sicilianpizza.objects.all(),
        'toppings_all': Topping.objects.all(),
        'pastas_all': Pasta.objects.all(),
        'salads_all': Salad.objects.all(),
        'subs_all': Sub.objects.all(),
        'num_visits': num_visits,
        'foodtypes': foodtypes,
        'foodnames': foodnames,
        'manager': manager,
    }
    return render(request, 'menu.html/',context=context)


def menu_nav(request, menuheader_displayedJSON):
    # print("94 index menu_nav: ",request)
    menuheader_display=["Pizzas","Pastas","Salads","Subs"]
    menuheaders_displayedJSON = json.loads(menuheader_display)
    return menuheaders_displayed;


def add_toppings(request, foodnameID):
    special_pizzaDICT = { # 0 corresponds to Sunday
    # SOMEDAY - put in model for easy editing
        0:"Shrimp Scampi",
        1:"Venison",
        2:"Duck Bacon",
        3:"Goat Cheese and Beets",
        4:"Asparagus, Artichoke Hearts and Spinach",
        5:"Herring",
        6:"Avocado and Habanero",
    }
    foodname = ''
    print("127 foodnameID", foodnameID)
    if int(foodnameID)<1000:
        get1 = Regularpizza.objects.get(id=foodnameID)
        numtoppings = get1.numtoppings
        smallprice = get1.smallprice
        largeprice = get1.largeprice
        foodtype = get1.foodtype
        pizzatypeDICT = {
        4:0,  # 0 signifies Regular Pizza, 4 no toppings
        8:0,  # 1 topping
        9:0,  # 2 toppings
        7:0,  # 3 toppings
        12:2, # Special Regular pizza
        }
        pizzatype  = pizzatypeDICT[foodnameID]
        print("141 pizzatype: ",pizzatype)
        if pizzatype==2:
            numtoppings = 0
            foodname = special_pizzaDICT[timezone.now().weekday()]
        context = {
            'foodnameID': foodnameID,
            'reqularpizzas_all': Regularpizza.objects.all(),
            'toppings_all': Topping.objects.all(),
            'numtoppings': numtoppings,
            'pizzatype': pizzatype,
            'smallprice': smallprice,
            'largeprice': largeprice,
            'foodname':foodname,
            # 'foodtype': foodtype,
            }
    if int(foodnameID)>1000 and int(foodnameID)<2000:
        foodnameID=foodnameID - 1000
        get1 = Sicilianpizza.objects.get(id=foodnameID)
        numtoppings = get1.numtoppings
        smallprice = get1.smallprice
        largeprice = get1.largeprice
        foodtype = get1.foodtype
        pizzatypeDICT = {
        1:1,  # 1 signifies Sicilian Pizza, 1 no toppings
        2:1,  # # 1 signifies Sicilian Pizza, 2 one topping
        3:1,  # 2 toppings
        4:1,  # 3 toppings
        5:3,  # Special Sicilian Pizza  # Should we use this tag instead of -1 for toppings?
        }
        pizzatype  = pizzatypeDICT[foodnameID]
        if pizzatype==3:
            numtoppings = 0
            foodname = special_pizzaDICT[timezone.now().weekday()]
        context = {
            'foodnameID': foodnameID,
            'reqularpizzas_all': Sicilianpizza.objects.all(),
            'toppings_all': Topping.objects.all(),
            'numtoppings': numtoppings,
            'pizzatype': pizzatype,
            'smallprice': smallprice,
            'largeprice': largeprice,
            'foodname':foodname,
            # 'foodtype': foodtype,
            }
    if int(foodnameID)>2000 and int(foodnameID)<3000:
        foodnameID=foodnameID - 2000
        get1 = Sub.objects.get(id=foodnameID)
        numtoppings = 0
        smallprice = get1.smallprice
        largeprice = get1.largeprice
        foodname = get1.name
        foodtype = 'sub'
        display_order = get1.display_order
        pizzatype = int("6")
        if display_order%1 != 0:
            parent_display_order = display_order-display_order%1
            print("203 parent_display_order: ", parent_display_order)
            parent = Sub.objects.get(display_order=parent_display_order)
            print("205: ",parent.smallprice, smallprice)
            smallprice = smallprice + parent.smallprice
            largeprice = largeprice + parent.largeprice
            foodname = parent.name + " " + foodname
        context = {
            'foodnameID': foodnameID,
            'reqularpizzas_all': Sub.objects.all(),
            'toppings_all': Topping.objects.all(),
            'numtoppings': numtoppings,
            'pizzatype': pizzatype,
            'smallprice': smallprice,
            'largeprice': largeprice,
            'foodname': foodname,
            'foodtype': foodtype,
            'display_order':display_order,
            }

    if int(foodnameID)>3000:
        foodnameID=foodnameID - 3000
        get1 = Dinnerplatter.objects.get(id=foodnameID)
        numtoppings = 0
        smallprice = get1.smallprice
        largeprice = get1.largeprice
        foodname = get1.name
        print("238, parent.name, foodname", foodname)
        foodtype = 'dinnerplatter'
        display_order = get1.display_order
        pizzatype = int("4")
        context = {
                'foodnameID': foodnameID,
                'reqularpizzas_all': Dinnerplatter.objects.all(),
                'toppings_all': Topping.objects.all(),
                'numtoppings': numtoppings,
                'pizzatype': pizzatype,
                'smallprice': smallprice,
                'largeprice': largeprice,
                'foodname': foodname,
                'foodtype': foodtype,
                'display_order':display_order,
                }
    return render(request, 'orders/add_toppings.html/', context=context)


def add_to_orderARRAY (request, foodnameID):
    """ This routine is only for subs as subs have add-ons"""
    get1 = Sub.objects.get(id=foodnameID)
    numtoppings = 0
    smallprice = get1.smallprice
    largeprice = get1.largeprice
    foodname = get1.name
    foodtype = 'sub'
    display_order = get1.display_order
    pizzatype = int("6")
    context = {
        'foodnameID': foodnameID,
        'reqularpizzas_all': Sub.objects.all(),
        'toppings_all': Topping.objects.all(),
        'numtoppings': numtoppings,
        'pizzatype': pizzatype,
        'smallprice': smallprice,
        'largeprice': largeprice,
        'foodname': foodname,
        'foodtype': foodtype,
        'display_order':display_order,
        }
    return render(request, 'orders/add_to_orderARRAY.html/', context=context)


def review_order(request):
    """Allows the customer to review and edit the order"""
    context = {
    'user_is_authenticated':request.user.is_authenticated,
    }
    return render(request, 'orders/review_order.html', context=context)


def place_order(request):
    context = { #TODO Delete if not needed
    'user_is_authenticated':request.user.is_authenticated,
    'next': '/orders/review_order.html' #Needed because of how we pass json
    }
    if not request.user.is_authenticated:
        return render(request, 'orders/place_order.html', context=context)
    return redirect('get_orderJS')


def get_orderJS(request):
    orderdataJSON = request.POST['orderdataJSON']
    orderdataJSON = json.loads(orderdataJSON)
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
    orderdataJSON_length = len(orderdataJSON)
    orderdataJSON_count = 0
    for order_item in orderdataJSON:
        print("302: order_item",order_item)
        if order_item["foodtype"]=="special":
            add_to_Order_model(customer_id,customer_name, ordertime, order_item)
        if order_item["foodtype"]=="regularpizza":
            order_item_model =  Regularpizza.objects.all()
            for item in order_item_model:
                try:
                    numtoppings = len(order_item["toppings"])
                except:
                    numtoppings = 0
                print("310 item.numtoppings, numtoppings",item.numtoppings, numtoppings)
                if item.numtoppings == numtoppings:
                    add_to_Order_model(customer_id,customer_name, ordertime, order_item)

        if order_item["foodtype"]=="sicilianpizza":
            order_item_model =  Sicilianpizza.objects.all()
            for item in order_item_model:
                try:
                    numtoppings = len(order_item["toppings"])
                except:
                    numtoppings = 0
                if item.numtoppings == numtoppings:
                    add_to_Order_model(customer_id,customer_name, ordertime, order_item)

        if order_item["foodtype"]=="pasta":
            order_item_data = Pasta.objects.filter(name=order_item["foodname"])
            for item in order_item_data:
                add_to_Order_model(customer_id,customer_name, ordertime, order_item)

        if order_item["foodtype"]=="salad":
            order_item_data = Salad.objects.filter(name=order_item["foodname"])
            for item in order_item_data:
                add_to_Order_model(customer_id,customer_name, ordertime, order_item)

        if order_item["foodtype"]=="sub":
            order_item_data = Sub.objects.filter(id=order_item["foodnameID"])
            for item in order_item_data:
                if item.display_order%1 != 0:
                    parent_display_order = item.display_order-item.display_order%1
                    parent = Sub.objects.get(display_order=parent_display_order)
                    item.smallprice = item.smallprice + parent.smallprice
                    item.largeprice = item.largeprice + parent.largeprice
                    item.name = parent.name + " " + item.name
                add_to_Order_model(customer_id,customer_name, ordertime, order_item)

        if order_item["foodtype"]=="dinnerplatter":
            order_item_data = Dinnerplatter.objects.filter(id=order_item["foodnameID"])
            for item in order_item_data:
                add_to_Order_model(customer_id,customer_name, ordertime, order_item)

    # Retrieve order data
    current_order =[]
    ordername = customer_name + "-" + ordertime.strftime("%m/%d/%Y, %H:%M:%S")
    current_order = Order.objects.filter(name=ordername)
    orderJSONSTR = order_history_to_JSON(current_order)
    order_price = Decimal(0.0)
    for item in current_order:
        order_price = order_price + Decimal(item.qty) * Decimal(item.foodprice)
    context = {
    'current_order': current_order,
    'order_price': order_price,
    'user_is_authenticated':request.user.is_authenticated,
    'place_order': True
    }
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
    # TODO add definition in triple quotes
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


def order_history(request):
    """Views order history and ratings"""
    print("414 order_history(request):", request)
    user_is_authenticated = False
    is_manager = False
    show_order_history = True
    my_ratingsLIST = []
    my_ratingsDICT ={}
    if request.user.is_authenticated:
        user_is_authenticated = True
        user_id = request.user.id
        user = User.objects.get(id=user_id)
        user_name = user.username
        if user_id == 2:
            is_manager = True
        current_order = Order.objects.all() #TODO Filter
        x1 = Order.objects.first().name
        current_order = Order.objects.filter(name=x1)
        my_orders = Order.objects.filter(customer_id=user.id)
        my_ratings = Rating.objects.filter(customer_id=user_id)
        if my_ratings.count()<1:
            print ("436 my_ratings.count()<1: do we need this if statement",my_ratings)
        #(user_id, order1.foodtype, order1.foodname, customer_rating)
        for rating in my_ratings:
            x = {
            "customer_id":rating.customer_id,
            "foodtype":rating.foodtype,
            "foodname":rating.foodname,
            "customer_rating":rating.customer_rating,
            }
            my_ratingsLIST.append(x)
        my_ratingsJSONSTR = json.dumps(my_ratingsLIST)
        my_ratingsJSONSTR = my_ratingsJSONSTR.replace("'",'"')


    if is_manager:
        current_order = Order.objects.all()
        orderJSONSTR = order_history_to_JSON(current_order) # TODOD Do we need this?
    try:
        x = current_order
    except:
        print ("464 no current order")
        current_order = []
    context = {
      'current_order': current_order,
      'is_manager': is_manager,
      'user_is_authenticated': user_is_authenticated,
      'my_orders': my_orders,
     # 'my_ratingsARRAY': my_ratingsLIST,
      'my_ratingsJSONSTR': my_ratingsJSONSTR,
      'show_order_history': show_order_history,
    # 'order_price': order_price,
    }
    return render(request, 'orders/order_list.html',context=context)


def ratings(request, orderid, foodrating):
    """Allows users to rate a past menu item. I do not allow ratings on
    the current order as the customer hasn't tried them yet"""
    user_id = request.user.id
    order1 = Order.objects.get(id=int(orderid))
    # If rating exists update
    rating1 = Rating.objects.filter(customer_id=user_id)
    if rating1.count()>0:
        if rating1.filter(foodtype=order1.foodtype).count()>0:
            if rating1.filter(foodtype=order1.foodtype).filter(foodname=order1.foodname).count()>0:
                if rating1.filter(foodtype=order1.foodtype).filter(foodname=order1.foodname).count()>1:
                    print("471: Why more than one rating?", rating1.filter(foodtype=order1.foodtype).filter(foodname=order1.foodname).count())
                    for rating_item in rating1.filter(foodtype=order1.foodtype).filter(foodname=order1.foodname):
                        print("473: ", rating_item.customer_id,rating_item.id, rating_item.foodname)
                rating1.filter(foodtype=order1.foodtype).filter(foodname=order1.foodname) \
                .update(customer_rating=foodrating)
                context = {

                }
                return redirect('order_history')
    # Else create a new rating
    context = {

    }
    create_new_rating(user_id, order1.foodtype, order1.foodname, foodrating)
    return redirect('order_history')


def create_new_rating(customer_id, foodtype, foodname, foodrating):
    print("507 create_new_rating:", customer_id, foodtype, foodname, foodrating)
    rating_item_model = Rating(
    customer_id = customer_id,
    foodtype = foodtype,
    foodname = foodname,
    customer_rating = foodrating
        )
    rating_item_model.save()
    return


def update_rating(rating_item_model, rating):
    print("515 update_rating:", customer_id, foodtype, foodname, foodrating)
    rating_item_model.update(rating=rating)
    rating_item_model.save()
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

class SicilianpizzaListView(generic.ListView):
    model = Sicilianpizza

class SicilianpizzaDetailView(generic.DetailView):
    model = Sicilianpizza
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(SicilianpizzaDetailView, self).get_context_data(**kwargs)
        context['Sicilianpizzas_all']=Sicilianpizza.objects.all()
        foodtypes = ["sicilianpizzas"]
        foodname = "sicilianpizza"
        context['foodtypes'] = foodtypes
        context['foodname'] = foodname
        return context

class SicilianpizzaCreate(CreateView):
    model = Sicilianpizza
    # fields = '__all__'
    fields = ['name', 'smallprice', 'largeprice', 'numtoppings']
    success_url = reverse_lazy('index')

class SicilianpizzaUpdate(UpdateView):
    model = Sicilianpizza
    # fields = '__all__'
    fields = ['name', 'smallprice', 'largeprice', 'numtoppings']
    success_url = reverse_lazy('index')

class SicilianpizzaDelete(DeleteView):
    model = Sicilianpizza
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


class SubListView(generic.ListView):
    model = Sub

class SubDetailView(generic.DetailView):
    model = Sub
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(SubDetailView, self).get_context_data(**kwargs)
        context['Subs_all']=Sub.objects.all()
        foodtypes = ["subs"]
        foodname = "sub"
        context['foodtypes'] = foodtypes
        context['foodname'] = foodname
        return context

class SubCreate(CreateView):
    model = Sub
    fields = '__all__'
    success_url = reverse_lazy('index')

class SubUpdate(UpdateView):
    model = Sub
    fields = '__all__'
    success_url = reverse_lazy('index')

class SubDelete(DeleteView):
    model = Sub
    success_url = reverse_lazy('index')


class DinnerplatterListView(generic.ListView):
    model = Dinnerplatter

class DinnerplatterDetailView(generic.DetailView):
    model = Dinnerplatter
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(DinnerplatterDetailView, self).get_context_data(**kwargs)
        context['Dinnerplatters_all']=Dinnerplatter.objects.all()
        foodtypes = ["dinnerplatters"]
        foodname = "dinnerplatter test to see what happens - line 671"
        context['foodtypes'] = foodtypes
        context['foodname'] = foodname
        return context

class DinnerplatterCreate(CreateView):
    model = Dinnerplatter
    fields = '__all__'
    success_url = reverse_lazy('index')

class DinnerplatterUpdate(UpdateView):
    model = Dinnerplatter
    fields = '__all__'
    success_url = reverse_lazy('index')

class DinnerplatterDelete(DeleteView):
    model = Dinnerplatter
    success_url = reverse_lazy('index')

class OrderListView(generic.ListView):
    model = Order
    def get_context_data(self, **kwargs):
        # x1 = Order.objects.first().name # commented out 1/18/20
        # x2 = Order.objects.filter(name=x1) # commented out 1/18/20
        # Call the base implementation first to get the context
        context = super(OrderListView, self).get_context_data(**kwargs)
        # context['current_order'] = x2 # commented out 1/18/20
        # print("558 context: ",context)
        return context


class OrderDetailView(generic.DetailView):
    model = Order
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(OrderDetailView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
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
    print("740: in signup")
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            # return redirect('place_order(request)')
    else:
        form = UserCreationForm()
    return render(request, 'orders/signup.html', {'form': form})

# modified from https://pythonprogramming.net/user-login-logout-django-tutorial/
def logged_out(request):
    print("567 request: ", request)
    logout(request)
    return render(request, 'orders/logged_out.html')
