from django.contrib import admin
from .models import Locacao

@admin.register(Locacao)
class LocacaoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'carro', 'data_retirada', 'data_devolucao', 'valor_total', 'ativa')
    list_filter = ('ativa', 'data_retirada')
    search_fields = ('cliente__nome', 'carro__modelo', 'carro__placa')