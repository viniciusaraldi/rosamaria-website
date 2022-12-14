from django.shortcuts import render,redirect
from .models import *
from django.views.generic import ListView, DetailView
from django.contrib import messages
# Create your views here.

class IndexListView(ListView):
    model = Products
    template_name = 'paginas/index.html'

class ListaProductsListView(ListView):
    model = Products
    template_name = 'paginas/list_product.html'

    def get_queryset(self):
        produtos_ativos = Products.objects.filter(status='ativo')
        return produtos_ativos

class MaterialsListView(ListView):
    model = Materials
    context_object_name = 'material'
    template_name = 'paginas/catalogo.html'

    
class CategoriesProdutosListView(ListView):
    model = Products
    context_object_name = 'produtcs'
    template_name = 'paginas/product_details.html'
    


class ProdutosDetailView(DetailView):
    model = Products
    template_name = 'paginas/products.html'

