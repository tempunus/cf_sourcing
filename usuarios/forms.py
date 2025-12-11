from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import PerfilUsuario
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit, HTML


class RegistroUsuarioForm(UserCreationForm):
    """
    Formulário para registro de novos usuários
    """
    
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'seu@email.com'
        })
    )
    
    first_name = forms.CharField(
        required=True,
        label='Nome',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Seu nome'
        })
    )
    
    last_name = forms.CharField(
        required=True,
        label='Sobrenome',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Seu sobrenome'
        })
    )
    
    telefone = forms.CharField(
        required=False,
        label='Telefone',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '(00) 00000-0000'
        })
    )
    
    cargo = forms.CharField(
        required=False,
        label='Cargo',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Seu cargo'
        })
    )
    
    departamento = forms.CharField(
        required=False,
        label='Departamento',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Seu departamento'
        })
    )
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nome de usuário'
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})
        
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('username', css_class='form-group col-md-6 mb-3'),
                Column('email', css_class='form-group col-md-6 mb-3'),
                css_class='row'
            ),
            Row(
                Column('first_name', css_class='form-group col-md-6 mb-3'),
                Column('last_name', css_class='form-group col-md-6 mb-3'),
                css_class='row'
            ),
            Row(
                Column('telefone', css_class='form-group col-md-4 mb-3'),
                Column('cargo', css_class='form-group col-md-4 mb-3'),
                Column('departamento', css_class='form-group col-md-4 mb-3'),
                css_class='row'
            ),
            Row(
                Column('password1', css_class='form-group col-md-6 mb-3'),
                Column('password2', css_class='form-group col-md-6 mb-3'),
                css_class='row'
            ),
            HTML('<button type="submit" class="btn btn-primary btn-lg">Cadastrar</button>'),
        )
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        
        if commit:
            user.save()
            # Criar perfil do usuário
            PerfilUsuario.objects.create(
                usuario=user,
                telefone=self.cleaned_data.get('telefone', ''),
                cargo=self.cleaned_data.get('cargo', ''),
                departamento=self.cleaned_data.get('departamento', '')
            )
        
        return user


class LoginForm(AuthenticationForm):
    """
    Formulário customizado para login
    """
    
    username = forms.CharField(
        label='Usuário',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nome de usuário'
        })
    )
    
    password = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Sua senha'
        })
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            'username',
            'password',
            HTML('<button type="submit" class="btn btn-danger btn-lg btn-block mt-3">Entrar</button>'),
        )
