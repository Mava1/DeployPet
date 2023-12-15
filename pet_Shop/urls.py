from django.contrib import admin
from django.urls import path
from django.urls import include
from .views import IndexPage , Contacto, Tienda

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", IndexPage.as_view(), name = "index"),
    path("contacto/", Contacto.as_view(), name="contacto"),

    path("tienda/" , Tienda.as_view(), name= "tienda"),
    path('productos/', include('app_productos.urls'))

]

'''    path("perros/" , Perros.as_view(), name= "perros"),
    path("gatos/" , Gatos.as_view(), name= "gatos") '''
    
