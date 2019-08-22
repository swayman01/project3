from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.index, name="index"), # This works
    path('index/', views.index, name='index'), # This works
    path('menu/<str:menusNAME>', views.menu, name='menu'),
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
    path('salad/<int:pk>/', views.SaladDetailView.as_view(), name='salad_detail'),
    path('salad/create/', views.SaladCreate.as_view(), name='salad_form'),
    path('salad/<int:pk>/update/', views.SaladUpdate.as_view(), name='salad_form'),
    path('salad/<int:pk>/delete/', views.SaladDelete.as_view(), name='salad_form'),
    path('toppings/', views.ToppingListView, name='toppings'), # This works except for context
    path('topping/<int:pk>/', views.ToppingDetailView.as_view(), name='topping_detail'),
    path('topping/create/', views.ToppingCreate.as_view(), name='topping_form'),
    path('topping/<int:pk>/update/', views.ToppingUpdate.as_view(), name='topping_form'),
    path('topping/<int:pk>/delete/', views.ToppingDelete.as_view(), name='topping_form'),
    path('<int:foodnameID>/orders/add_toppings.html', views.add_toppings, name="add_toppings"), # missiong positional argument
    path('add_toppings_experiment.html', views.add_toppings_experiment, name="add_toppings_experiment"),
    path('orders/review_order.html', views.review_order, name="review_order"),
]
print("33 urlpatterns\n:",urlpatterns[-1],"/n", urlpatterns[-2])
