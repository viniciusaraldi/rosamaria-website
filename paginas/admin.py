from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('name','slug','user','imagem')

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name','slug','status','category','create','user','destaque')
    list_filter = ('status','create','user')
    search_fields = ('name','description','category__name')

@admin.register(Materials)
class MaterialsAdmin(admin.ModelAdmin):
    list_display = ('name','imagem','user','cover')