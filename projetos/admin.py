from django.contrib import admin
from .models import Projeto


@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ['cf_codigo', 'cliente', 'plataforma', 'status', 'data_atualizacao', 'operador']
    list_filter = ['status', 'plataforma', 'data_atualizacao']
    search_fields = ['cf_codigo', 'cliente', 'fornecedor']
    date_hierarchy = 'data_atualizacao'
    ordering = ['-data_atualizacao']
