from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexListView.as_view(), name='home'),
    path('catalogo/', MaterialsListView.as_view(), name='catalogo'),
    path('categoria/produtos', ListaProductsListView.as_view(), name='lista-de-produtos'),
    path('categoria/<category>/<slug:slug>', ProdutosDetailView.as_view(), name='produtos-detail'),
]