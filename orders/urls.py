from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"), # This works
    path('index/', views.index, name='index'), # This works
    path('menu/<str:menusNAME>', views.menu, name='menu'),
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
]
