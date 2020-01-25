from django.urls import path, include
from . import views
from django.conf import settings

urlpatterns = [
    path("", views.index, name="index"), # This works
    path('index/', views.index, name='index'), # This works
    path('regularpizzas/', views.RegularpizzaListView, name='regularpizzas'), # This works except for context is this needed? 12/26/19
    path('regularpizza/<int:pk>/', views.RegularpizzaDetailView.as_view(), name='regularpizza_detail'),
    path('regularpizza/create/', views.RegularpizzaCreate.as_view(), name='regularpizza_form'),
    path('regularpizza/<int:pk>/update/', views.RegularpizzaUpdate.as_view(), name='regularpizza_form'),
    path('regularpizza/<int:pk>/delete/', views.RegularpizzaDelete.as_view(), name='regularpizza_form'),
    path('sicilianpizza/<int:pk>/', views.SicilianpizzaDetailView.as_view(), name='sicilianpizza_detail'),
    path('sicilianpizza/create/', views.SicilianpizzaCreate.as_view(), name='sicilianpizza_form'),
    path('sicilianpizza/<int:pk>/update/', views.SicilianpizzaUpdate.as_view(), name='sicilianpizza_form'),
    path('sicilianpizza/<int:pk>/delete/', views.SicilianpizzaDelete.as_view(), name='regularpizza_form'),
    path('pastas/', views.PastaListView, name='pastas'), # This works except for context
    path('pasta/<int:pk>/', views.PastaDetailView.as_view(), name='pasta_detail'),
    path('pasta/create/', views.PastaCreate.as_view(), name='pasta_form'),
    path('pasta/<int:pk>/update/', views.PastaUpdate.as_view(), name='pasta_form'),
    path('pasta/<int:pk>/delete/', views.PastaDelete.as_view(), name='pasta_form'),
    # path('salads/', views.salads, name='salads'), # Commented out 1/20/2020 This works except for context, should we make this like pastas?
    path('salad/<int:pk>/', views.SaladDetailView.as_view(), name='salad_detail'),
    path('salad/create/', views.SaladCreate.as_view(), name='salad_form'),
    path('salad/<int:pk>/update/', views.SaladUpdate.as_view(), name='salad_form'),
    path('salad/<int:pk>/delete/', views.SaladDelete.as_view(), name='salad_form'),
    path('subs/', views.SubListView, name='subs'),
    path('sub/<int:pk>/', views.SubDetailView.as_view(), name='sub_detail'),
    path('sub/create/', views.SubCreate.as_view(), name='sub_form'),
    path('sub/<int:pk>/update/', views.SubUpdate.as_view(), name='sub_form'),
    path('sub/<int:pk>/delete/', views.SubDelete.as_view(), name='sub_form'),
    path('dinnerplatters/', views.DinnerplatterListView, name='dinnerplatters'),
    path('dinnerplatter/<int:pk>/', views.DinnerplatterDetailView.as_view(), name='dinnerplatter_detail'),
    path('dinnerplatter/create/', views.DinnerplatterCreate.as_view(), name='dinnerplatter_form'),
    path('dinnerplatter/<int:pk>/update/', views.DinnerplatterUpdate.as_view(), name='dinnerplatter_form'),
    path('dinnerplatter/<int:pk>/delete/', views.DinnerplatterDelete.as_view(), name='dinnerplatter_form'),
    path('topping/<int:pk>/', views.ToppingDetailView.as_view(), name='topping_detail'),
    path('topping/create/', views.ToppingCreate.as_view(), name='topping_form'),
    path('topping/<int:pk>/update/', views.ToppingUpdate.as_view(), name='topping_form'),
    path('topping/<int:pk>/delete/', views.ToppingDelete.as_view(), name='topping_form'),
    path('orders/', views.OrderListView.as_view(), name='order_list'),
    path('orders/<int:pk>', views.OrderDetailView.as_view(), name='order_detail'),
    path('orders/logged_out/',views.logged_out, name="logged_out"),
    path('<int:foodnameID>/orders/add_toppings.html', views.add_toppings, name="add_toppings"),
    path('add_toppings.html', views.add_toppings, name="add_toppings"),
    path('add_to_orderARRAY.html', views.add_to_orderARRAY, name="add_to_orderARRAY"), # This may not be needed
    path('orders/review_order.html', views.review_order, name="review_order"),
    path('orders/place_order.html', views.place_order, name="place_order"),
    path('orders/get_orderJS', views.get_orderJS, name="get_orderJS"),
    path('orders/order_history', views.order_history, name="order_history"),
    #path('orders/ratings.html/<foodrating>/', views.ratings, name="ratings"), Commented out 2/22/2020
    path('orders/ratings.html/<orderid>,<foodrating>/', views.ratings, name="ratings"),
    path('orders/signup.html', views.signup, name="signup"),
]
#TODO Cleanup
    # path('<data>/orders/retrieve_order/', views.retrieve_order, name="retrieve_order"), #Commented out 12/13/19


# print("52 urlpatterns\n:",urlpatterns[-8:],"\n")
