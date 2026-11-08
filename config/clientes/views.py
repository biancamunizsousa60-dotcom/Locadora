from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .models import Cliente

class ClienteListView(ListView):
    model = Cliente
    template_name = 'clientes/lista.html'
    context_object_name = 'clientes'

class ClienteCreateView(CreateView):
    model = Cliente
    fields = ['nome', 'cpf', 'telefone', 'email']
    template_name = 'form.html'
    success_url = reverse_lazy('clientes:lista')