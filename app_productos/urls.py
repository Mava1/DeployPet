from django.contrib import admin
from django.urls import path , include


from .views import      ProductoListView   
            

app_name = "productos"

urlpatterns = [
    path("", ProductoListView.as_view(), name="all")
    

]