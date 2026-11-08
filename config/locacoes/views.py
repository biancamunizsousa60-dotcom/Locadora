from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .models import Locacao

class LocacaoListView(ListView):
    model = Locacao
    template_name = 'locacoes/lista.html'
    context_object_name = 'locacoes'

class LocacaoCreateView(CreateView):
    model = Locacao
    fields = ['cliente', 'carro', 'data_retirada', 'data_devolucao']
    template_name = 'form.html'
    success_url = reverse_lazy('locacoes:lista')