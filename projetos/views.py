from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Projeto
from .forms import ProjetoForm, ProjetoPesquisaForm


@login_required
def dashboard(request):
    """
    Dashboard principal com estatísticas e projetos recentes
    """
    projetos_recentes = Projeto.objects.all()[:5]
    total_projetos = Projeto.objects.count()
    projetos_ativos = Projeto.objects.filter(
        status__in=['INICIAR_SOURCING', 'EM_ANDAMENTO', 'AGUARDANDO_FORNECEDOR']
    ).count()
    projetos_concluidos = Projeto.objects.filter(status='CONCLUIDO').count()
    
    context = {
        'projetos_recentes': projetos_recentes,
        'total_projetos': total_projetos,
        'projetos_ativos': projetos_ativos,
        'projetos_concluidos': projetos_concluidos,
    }
    return render(request, 'projetos/dashboard.html', context)


@login_required
def projeto_criar(request):
    """
    View para criar novo projeto
    """
    if request.method == 'POST':
        form = ProjetoForm(request.POST)
        if form.is_valid():
            projeto = form.save(commit=False)
            projeto.operador = request.user
            projeto.save()
            messages.success(request, 'Projeto criado com sucesso!')
            return redirect('projeto_detalhe', pk=projeto.pk)
    else:
        form = ProjetoForm()
    
    return render(request, 'projetos/projeto_form.html', {'form': form, 'titulo': 'Novo Projeto'})


@login_required
def projeto_editar(request, pk):
    """
    View para editar projeto existente
    """
    projeto = get_object_or_404(Projeto, pk=pk)
    
    if request.method == 'POST':
        form = ProjetoForm(request.POST, instance=projeto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Projeto atualizado com sucesso!')
            return redirect('projeto_detalhe', pk=projeto.pk)
    else:
        form = ProjetoForm(instance=projeto)
    
    return render(request, 'projetos/projeto_form.html', {'form': form, 'titulo': 'Editar Projeto', 'projeto': projeto})


@login_required
def projeto_detalhe(request, pk):
    """
    View para exibir detalhes do projeto
    """
    projeto = get_object_or_404(Projeto, pk=pk)
    return render(request, 'projetos/projeto_detalhe.html', {'projeto': projeto})


@login_required
def projeto_lista(request):
    """
    View para listar todos os projetos
    """
    projetos = Projeto.objects.all()
    return render(request, 'projetos/projeto_lista.html', {'projetos': projetos})


@login_required
def projeto_pesquisa(request):
    """
    View para pesquisar projetos com filtros
    """
    form = ProjetoPesquisaForm(request.GET or None)
    projetos = Projeto.objects.all()
    
    if form.is_valid():
        cf_codigo = form.cleaned_data.get('cf_codigo')
        cliente = form.cleaned_data.get('cliente')
        data_inicio = form.cleaned_data.get('data_inicio')
        data_fim = form.cleaned_data.get('data_fim')
        status = form.cleaned_data.get('status')
        
        if cf_codigo:
            projetos = projetos.filter(cf_codigo__icontains=cf_codigo)
        
        if cliente:
            projetos = projetos.filter(cliente__icontains=cliente)
        
        if data_inicio:
            projetos = projetos.filter(data_atualizacao__gte=data_inicio)
        
        if data_fim:
            projetos = projetos.filter(data_atualizacao__lte=data_fim)
        
        if status:
            projetos = projetos.filter(status=status)
    
    context = {
        'form': form,
        'projetos': projetos,
        'total_resultados': projetos.count()
    }
    
    return render(request, 'projetos/projeto_pesquisa.html', context)


@login_required
def projeto_deletar(request, pk):
    """
    View para deletar projeto
    """
    projeto = get_object_or_404(Projeto, pk=pk)
    
    if request.method == 'POST':
        projeto.delete()
        messages.success(request, 'Projeto deletado com sucesso!')
        return redirect('projeto_lista')
    
    return render(request, 'projetos/projeto_confirmar_delete.html', {'projeto': projeto})
