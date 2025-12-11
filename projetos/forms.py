from django import forms
from .models import Projeto
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit, HTML


class ProjetoForm(forms.ModelForm):
    """
    Formulário para cadastro e edição de projetos
    """
    
    class Meta:
        model = Projeto
        fields = [
            'cf_codigo',
            'cliente',
            'plataforma',
            'inicio_sourcing',
            'status',
            'fornecedor',
            'descricao',
        ]
        widgets = {
            'cf_codigo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: CF-001'
            }),
            'cliente': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nome do cliente'
            }),
            'plataforma': forms.Select(attrs={
                'class': 'form-control'
            }),
            'inicio_sourcing': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'status': forms.Select(attrs={
                'class': 'form-control'
            }),
            'fornecedor': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nome do fornecedor'
            }),
            'descricao': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Descrição detalhada do projeto'
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('cf_codigo', css_class='form-group col-md-6 mb-3'),
                Column('cliente', css_class='form-group col-md-6 mb-3'),
                css_class='row'
            ),
            Row(
                Column('plataforma', css_class='form-group col-md-4 mb-3'),
                Column('inicio_sourcing', css_class='form-group col-md-4 mb-3'),
                Column('status', css_class='form-group col-md-4 mb-3'),
                css_class='row'
            ),
            Row(
                Column('fornecedor', css_class='form-group col-md-12 mb-3'),
                css_class='row'
            ),
            Row(
                Column('descricao', css_class='form-group col-md-12 mb-3'),
                css_class='row'
            ),
            HTML('<button type="submit" class="btn btn-primary btn-lg">Salvar Projeto</button>'),
        )


class ProjetoPesquisaForm(forms.Form):
    """
    Formulário para pesquisa de projetos
    """
    
    cf_codigo = forms.CharField(
        required=False,
        label='CF - Código',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Buscar por código CF'
        })
    )
    
    cliente = forms.CharField(
        required=False,
        label='Cliente',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Buscar por cliente'
        })
    )
    
    data_inicio = forms.DateField(
        required=False,
        label='Data Inicial',
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date'
        })
    )
    
    data_fim = forms.DateField(
        required=False,
        label='Data Final',
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date'
        })
    )
    
    status = forms.ChoiceField(
        required=False,
        label='Status',
        choices=[('', 'Todos')] + Projeto.STATUS_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'get'
        self.helper.layout = Layout(
            Row(
                Column('cf_codigo', css_class='form-group col-md-3 mb-3'),
                Column('cliente', css_class='form-group col-md-3 mb-3'),
                Column('data_inicio', css_class='form-group col-md-2 mb-3'),
                Column('data_fim', css_class='form-group col-md-2 mb-3'),
                Column('status', css_class='form-group col-md-2 mb-3'),
                css_class='row'
            ),
            HTML('<button type="submit" class="btn btn-danger">Pesquisar</button>'),
        )
