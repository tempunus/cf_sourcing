from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Projeto(models.Model):
    """
    Model para representar um projeto de sourcing
    Baseado na estrutura da planilha Google Sheets
    """
    
    STATUS_CHOICES = [
        ('INICIAR_SOURCING', 'Iniciar Sourcing'),
        ('EM_ANDAMENTO', 'Em Andamento'),
        ('AGUARDANDO_FORNECEDOR', 'Aguardando Fornecedor'),
        ('CONCLUIDO', 'Concluído'),
        ('CANCELADO', 'Cancelado'),
    ]
    
    PLATAFORMA_CHOICES = [
        ('CHINA_FACIL', 'China Fácil'),
        ('ALIBABA', 'Alibaba'),
        ('1688', '1688'),
        ('TAOBAO', 'Taobao'),
        ('OUTROS', 'Outros'),
    ]
    
    # Campos principais
    cf_codigo = models.CharField(
        max_length=50, 
        verbose_name='CF - Código',
        unique=True,
        help_text='Código único do projeto'
    )
    
    cliente = models.CharField(
        max_length=200,
        verbose_name='Cliente',
        help_text='Nome do cliente'
    )
    
    plataforma = models.CharField(
        max_length=50,
        choices=PLATAFORMA_CHOICES,
        default='CHINA_FACIL',
        verbose_name='Plataforma'
    )
    
    inicio_sourcing = models.DateField(
        verbose_name='Início do Sourcing',
        default=timezone.now
    )
    
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='INICIAR_SOURCING',
        verbose_name='Status'
    )
    
    fornecedor = models.CharField(
        max_length=200,
        verbose_name='Fornecedor',
        blank=True,
        null=True,
        help_text='Nome do fornecedor'
    )
    
    descricao = models.TextField(
        verbose_name='Descrição',
        help_text='Descrição detalhada do projeto'
    )
    
    data_atualizacao = models.DateTimeField(
        auto_now=True,
        verbose_name='Data da Atualização'
    )
    
    operador = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='projetos',
        verbose_name='Operador'
    )
    
    # Campos de auditoria
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'
        ordering = ['-data_atualizacao']
        indexes = [
            models.Index(fields=['cf_codigo']),
            models.Index(fields=['cliente']),
            models.Index(fields=['data_atualizacao']),
        ]
    
    def __str__(self):
        return f"{self.cf_codigo} - {self.cliente}"
    
    def get_status_display_class(self):
        """Retorna a classe CSS apropriada para o status"""
        status_classes = {
            'INICIAR_SOURCING': 'success',
            'EM_ANDAMENTO': 'primary',
            'AGUARDANDO_FORNECEDOR': 'warning',
            'CONCLUIDO': 'info',
            'CANCELADO': 'danger',
        }
        return status_classes.get(self.status, 'secondary')
