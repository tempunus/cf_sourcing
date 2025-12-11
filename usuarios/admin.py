from django.contrib import admin
from .models import RegistroAcesso, PerfilUsuario


@admin.register(RegistroAcesso)
class RegistroAcessoAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'data_login', 'data_logout', 'ip_address', 'sessao_ativa']
    list_filter = ['sessao_ativa', 'data_login']
    search_fields = ['usuario__username', 'ip_address']
    date_hierarchy = 'data_login'
    ordering = ['-data_login']


@admin.register(PerfilUsuario)
class PerfilUsuarioAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'telefone', 'cargo', 'departamento']
    search_fields = ['usuario__username', 'cargo', 'departamento']
