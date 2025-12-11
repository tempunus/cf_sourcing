from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegistroUsuarioForm, LoginForm
from .models import RegistroAcesso
from django.utils import timezone


def get_client_ip(request):
    """Obtém o IP do cliente"""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def registro(request):
    """
    View para registro de novos usuários
    """
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Conta criada com sucesso! Faça login para continuar.')
            return redirect('login')
    else:
        form = RegistroUsuarioForm()
    
    return render(request, 'registration/registro.html', {'form': form})


def login_view(request):
    """
    View customizada para login com registro de acesso
    """
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            
            # Registrar acesso
            ip_address = get_client_ip(request)
            user_agent = request.META.get('HTTP_USER_AGENT', '')
            
            RegistroAcesso.objects.create(
                usuario=user,
                ip_address=ip_address,
                user_agent=user_agent,
                sessao_ativa=True
            )
            
            messages.success(request, f'Bem-vindo, {user.first_name}!')
            return redirect('dashboard')
    else:
        form = LoginForm()
    
    return render(request, 'registration/login.html', {'form': form})


@login_required
def logout_view(request):
    """
    View customizada para logout com registro de saída
    """
    # Atualizar último registro de acesso
    ultimo_acesso = RegistroAcesso.objects.filter(
        usuario=request.user,
        sessao_ativa=True
    ).order_by('-data_login').first()
    
    if ultimo_acesso:
        ultimo_acesso.data_logout = timezone.now()
        ultimo_acesso.sessao_ativa = False
        ultimo_acesso.save()
    
    logout(request)
    messages.info(request, 'Você saiu do sistema.')
    return redirect('login')


@login_required
def meus_acessos(request):
    """
    View para exibir histórico de acessos do usuário
    """
    acessos = RegistroAcesso.objects.filter(usuario=request.user)
    return render(request, 'usuarios/meus_acessos.html', {'acessos': acessos})


@login_required
def todos_acessos(request):
    """
    View para administradores verem todos os acessos
    """
    if not request.user.is_staff:
        messages.error(request, 'Você não tem permissão para acessar esta página.')
        return redirect('dashboard')
    
    acessos = RegistroAcesso.objects.all()
    return render(request, 'usuarios/todos_acessos.html', {'acessos': acessos})
