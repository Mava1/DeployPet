from django.contrib import admin
from .models import Producto
from django.contrib.admin import ModelAdmin

# Register your models here.
@admin.register(Producto)
class ProductosAdmin(ModelAdmin):
    ...