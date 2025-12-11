from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class RegistroAcesso(models.Model):
    """
    Model para registrar acessos dos usuários ao sistema
    Registra login, logout, IP e localização
    """
    
    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='acessos',
        verbose_name='Usuário'
    )
    
    data_login = models.DateTimeField(
        default=timezone.now,
        verbose_name='Data/Hora de Login'
    )
    
    data_logout = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name='Data/Hora de Logout'
    )
    
    ip_address = models.GenericIPAddressField(
        verbose_name='Endereço IP',
        null=True,
        blank=True
    )
    
    user_agent = models.TextField(
        verbose_name='User Agent',
        blank=True,
        help_text='Informações do navegador'
    )
    
    localizacao = models.CharField(
        max_length=200,
        verbose_name='Localização',
        blank=True,
        help_text='Cidade/Estado/País'
    )
    
    sessao_ativa = models.BooleanField(
        default=True,
        verbose_name='Sessão Ativa'
    )
    
    class Meta:
        verbose_name = 'Registro de Acesso'
        verbose_name_plural = 'Registros de Acesso'
        ordering = ['-data_login']
        indexes = [
            models.Index(fields=['usuario', '-data_login']),
            models.Index(fields=['sessao_ativa']),
        ]
    
    def __str__(self):
        return f"{self.usuario.username} - {self.data_login.strftime('%d/%m/%Y %H:%M:%S')}"
    
    def duracao_sessao(self):
        """Calcula a duração da sessão"""
        if self.data_logout:
            delta = self.data_logout - self.data_login
            horas = delta.seconds // 3600
            minutos = (delta.seconds % 3600) // 60
            return f"{horas}h {minutos}min"
        return "Em andamento"


class PerfilUsuario(models.Model):
    """
    Extensão do modelo User padrão do Django
    Para armazenar informações adicionais
    """
    
    usuario = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='perfil',
        verbose_name='Usuário'
    )
    
    telefone = models.CharField(
        max_length=20,
        verbose_name='Telefone',
        blank=True
    )
    
    cargo = models.CharField(
        max_length=100,
        verbose_name='Cargo',
        blank=True
    )
    
    departamento = models.CharField(
        max_length=100,
        verbose_name='Departamento',
        blank=True
    )
    
    foto = models.ImageField(
        upload_to='perfis/',
        verbose_name='Foto de Perfil',
        blank=True,
        null=True
    )
    
    data_criacao = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Data de Criação'
    )
    
    class Meta:
        verbose_name = 'Perfil de Usuário'
        verbose_name_plural = 'Perfis de Usuários'
    
    def __str__(self):
        return f"Perfil de {self.usuario.username}"
