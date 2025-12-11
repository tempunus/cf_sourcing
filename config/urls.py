"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from usuarios import views as usuarios_views
from projetos import views as projetos_views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Autenticação
    path('', usuarios_views.login_view, name='login'),
    path('login/', usuarios_views.login_view, name='login'),
    path('logout/', usuarios_views.logout_view, name='logout'),
    path('registro/', usuarios_views.registro, name='registro'),
    
    # Dashboard
    path('dashboard/', projetos_views.dashboard, name='dashboard'),
    
    # Projetos
    path('projetos/', projetos_views.projeto_lista, name='projeto_lista'),
    path('projetos/novo/', projetos_views.projeto_criar, name='projeto_criar'),
    path('projetos/<int:pk>/', projetos_views.projeto_detalhe, name='projeto_detalhe'),
    path('projetos/<int:pk>/editar/', projetos_views.projeto_editar, name='projeto_editar'),
    path('projetos/<int:pk>/deletar/', projetos_views.projeto_deletar, name='projeto_deletar'),
    path('projetos/pesquisa/', projetos_views.projeto_pesquisa, name='projeto_pesquisa'),
    
    # Acessos
    path('acessos/meus/', usuarios_views.meus_acessos, name='meus_acessos'),
    path('acessos/todos/', usuarios_views.todos_acessos, name='todos_acessos'),
]

# Servir arquivos de mídia em desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
