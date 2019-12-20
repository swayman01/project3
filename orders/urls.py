from django.urls import path, include
from . import views
from django.conf import settings

#from django.contrib.auth.views import logout

urlpatterns = [
    path("", views.index, name="index"), # This works
    path('index/', views.index, name='index'), # This works
    path('regularpizzas/', views.RegularpizzaListView, name='regularpizzas'), # This works except for context
    path('regularpizza/<int:pk>/', views.RegularpizzaDetailView.as_view(), name='regularpizza_detail'),
    path('regularpizza/create/', views.RegularpizzaCreate.as_view(), name='regularpizza_form'),
    path('regularpizza/<int:pk>/update/', views.RegularpizzaUpdate.as_view(), name='regularpizza_form'),
    path('regularpizza/<int:pk>/delete/', views.RegularpizzaDelete.as_view(), name='regularpizza_form'),
    path('pastas/', views.PastaListView, name='pastas'), # This works except for context
    path('pasta/<int:pk>/', views.PastaDetailView.as_view(), name='pasta_detail'),
    path('pasta/create/', views.PastaCreate.as_view(), name='pasta_form'),
    path('pasta/<int:pk>/update/', views.PastaUpdate.as_view(), name='pasta_form'),
    path('pasta/<int:pk>/delete/', views.PastaDelete.as_view(), name='pasta_form'),
    path('salads/', views.salads, name='salads'), # This works except for context
    path('salad/<int:pk>/', views.SaladDetailView.as_view(), name='salad_detail'), # needed 11/4/19
    path('salad/create/', views.SaladCreate.as_view(), name='salad_form'),
    path('salad/<int:pk>/update/', views.SaladUpdate.as_view(), name='salad_form'),
    path('salad/<int:pk>/delete/', views.SaladDelete.as_view(), name='salad_form'),
    path('topping/<int:pk>/', views.ToppingDetailView.as_view(), name='topping_detail'), # Needed 9/19/19
    path('topping/create/', views.ToppingCreate.as_view(), name='topping_form'),
    path('topping/<int:pk>/update/', views.ToppingUpdate.as_view(), name='topping_form'),
    path('topping/<int:pk>/delete/', views.ToppingDelete.as_view(), name='topping_form'),
    path('orders/', views.OrderListView.as_view(), name='order_list'), # This worked 11/1/19
    path('orders/<int:pk>', views.OrderDetailView.as_view(), name='order_detail'),
    path('orders/logged_out/',views.logged_out, name="logged_out"),
    path('<int:foodnameID>/orders/add_toppings.html', views.add_toppings, name="add_toppings"), # needed 9/19/19
    path('add_toppings.html', views.add_toppings, name="add_toppings"),
    path('orders/review_order.html', views.review_order, name="review_order"),
    path('orders/place_order.html', views.place_order, name="place_order"), #needed 10/25/19
    path('orders/get_orderJS', views.get_orderJS, name="get_orderJS"),
    path('orders/signup.html', views.signup, name="signup"),
]
#TODO Cleanup
    # path('<data>/orders/retrieve_order/', views.retrieve_order, name="retrieve_order"), #Commented out 12/13/19


# print("56 urlpatterns\n:",urlpatterns[-8:],"\n")
