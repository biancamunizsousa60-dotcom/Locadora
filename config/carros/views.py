from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .models import Carro
class CarroListView(ListView):
    model = Carro
    template_name = 'carros/lista.html'
    context_object_name = 'carros'
class CarroCreateView(CreateView):
    model = Carro
    fields = ['marca', 'modelo', 'ano', 'placa', 'valor_diaria']
    template_name = 'form.html'
    success_url = reverse_lazy('carros:lista')