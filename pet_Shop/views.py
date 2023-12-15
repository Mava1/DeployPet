from django.views.generic import TemplateView

class IndexPage (TemplateView):
    template_name = "index.html"

class Contacto (TemplateView):
    template_name = "contacto.html"    


class Tienda (TemplateView):
    template_name = "tienda.html"   


# views.py
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render

@staff_member_required
def vista_que_requiere_login(request):
    # Tu lógica de vista aquí
    return render(request, 'adim:index')
