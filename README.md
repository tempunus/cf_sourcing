# Aplicação Django - Relatório de Projetos China Fácil

## 📋 Visão Geral

Aplicação Django completa para gerenciamento de projetos de sourcing, baseada na estrutura de uma planilha Google Sheets. Inclui cadastro de usuários, projetos, pesquisa avançada e registro de acessos.

## 🎨 Design

- **Paleta de Cores**: Vermelho China Fácil (#C8102E), Carvão (#2C2C2C), Ouro (#D4AF37)
- **Tipografia**: Roboto para corpo, Oswald para títulos
- **Responsividade**: Totalmente adaptada para desktop e mobile

## 🚀 Instalação e Configuração

### Pré-requisitos
- Python 3.11+
- pip
- virtualenv

### Passos de Instalação

1. **Criar e ativar ambiente virtual:**
```bash
python3.11 -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

2. **Instalar dependências:**
```bash
pip install -r requirements.txt
```

3. **Executar migrações:**
```bash
python manage.py makemigrations
python manage.py migrate
```

4. **Criar superusuário (admin):**
```bash
python manage.py createsuperuser
```

5. **Iniciar servidor de desenvolvimento:**
```bash
python manage.py runserver
```

Acesse em: `http://localhost:8000`

## 📁 Estrutura do Projeto

```
relatorio_projetos/
├── config/                 # Configurações do Django
│   ├── settings.py        # Configurações principais
│   ├── urls.py            # URLs principais
│   └── wsgi.py            # WSGI para produção
├── projetos/              # App de projetos
│   ├── models.py          # Modelos de dados
│   ├── views.py           # Views e lógica
│   ├── forms.py           # Formulários
│   ├── admin.py           # Admin do Django
│   └── templates/         # Templates HTML
├── usuarios/              # App de usuários
│   ├── models.py          # Modelos de usuários
│   ├── views.py           # Views de autenticação
│   ├── forms.py           # Formulários de registro
│   └── templates/         # Templates de login/registro
├── templates/             # Templates base
│   └── base.html          # Template base com navbar
├── static/                # Arquivos estáticos (CSS, JS)
├── media/                 # Arquivos de mídia
├── manage.py              # Script de gerenciamento
└── requirements.txt       # Dependências do projeto
```

## 🗄️ Modelos de Dados

### Projeto
- `cf_codigo`: Código do CF (Cotar os Itens)
- `cliente`: Nome do cliente
- `plataforma`: Plataforma de sourcing (Alibaba, Global Sources, etc)
- `fornecedor`: Nome do fornecedor
- `descricao`: Descrição detalhada
- `status`: Status do projeto (Em Análise, Em Cotação, etc)
- `inicio_sourcing`: Data de início
- `data_atualizacao`: Data da última atualização
- `operador`: Usuário responsável

### RegistroAcesso
- `usuario`: Usuário que fez login
- `data_login`: Data/hora do login
- `data_logout`: Data/hora do logout
- `ip_address`: IP do acesso
- `localizacao`: Localização geográfica
- `sessao_ativa`: Status da sessão

### PerfilUsuario
- `usuario`: Usuário do Django
- `telefone`: Telefone de contato
- `cargo`: Cargo do usuário
- `departamento`: Departamento

## 🔐 Credenciais Padrão

**Admin:**
- Usuário: `admin`
- Senha: `admin123`

⚠️ **IMPORTANTE**: Altere a senha em produção!

## 📊 Funcionalidades

### ✅ Implementadas

1. **Autenticação**
   - Login/Logout
   - Registro de novos usuários
   - Perfil de usuário

2. **Gerenciamento de Projetos**
   - Criar novo projeto
   - Listar todos os projetos
   - Visualizar detalhes
   - Editar projeto
   - Deletar projeto

3. **Pesquisa Avançada**
   - Buscar por CF
   - Buscar por Cliente
   - Filtrar por data de atualização
   - Filtrar por status

4. **Registro de Acessos**
   - Registrar login/logout automático
   - Visualizar histórico de acessos pessoais
   - Admin pode ver acessos de todos os usuários
   - Informações: IP, localização, duração da sessão

5. **Dashboard**
   - Visão geral de projetos
   - Estatísticas rápidas
   - Projetos recentes

## 🎯 URLs Principais

| URL | Descrição |
|-----|-----------|
| `/` | Login |
| `/dashboard/` | Dashboard principal |
| `/projetos/` | Lista de projetos |
| `/projetos/novo/` | Criar novo projeto |
| `/projetos/<id>/` | Detalhes do projeto |
| `/projetos/<id>/editar/` | Editar projeto |
| `/projetos/pesquisa/` | Pesquisa avançada |
| `/acessos/meus/` | Meus acessos |
| `/acessos/todos/` | Todos os acessos (admin) |
| `/admin/` | Painel administrativo |

## 🛠️ Customizações Comuns

### Adicionar novo campo ao Projeto

1. Edite `projetos/models.py`:
```python
class Projeto(models.Model):
    # ... campos existentes ...
    novo_campo = models.CharField(max_length=100, blank=True)
```

2. Crie migração:
```bash
python manage.py makemigrations
python manage.py migrate
```

3. Atualize `projetos/forms.py` para incluir o novo campo

4. Atualize os templates para exibir o novo campo

### Alterar cores do tema

Edite `templates/base.html` na seção `:root`:
```css
--primary-red: #C8102E;  /* Cor primária */
--dark-red: #8B0000;     /* Cor escura */
```

## 📱 Responsividade Mobile

- Menu lateral colapsável em telas pequenas
- Tabelas com scroll horizontal
- Botões redimensionáveis
- Espaçamento otimizado para toque

## 🔒 Segurança

- CSRF protection ativado
- Senhas com hash seguro
- Validação de formulários
- Autenticação obrigatória

### Para Produção:

1. Altere `DEBUG = False` em `settings.py`
2. Configure `ALLOWED_HOSTS`
3. Use variáveis de ambiente para `SECRET_KEY`
4. Configure HTTPS
5. Use banco de dados robusto (PostgreSQL recomendado)

## 📦 Dependências

```
Django==5.2.9
Pillow==10.0.0
django-crispy-forms==2.0
crispy-bootstrap5==0.7
```

## 🐛 Troubleshooting

### Erro de migração
```bash
python manage.py migrate --fake-initial
```

### Limpar cache
```bash
python manage.py clear_cache
```

### Resetar banco de dados
```bash
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

## 📝 Notas de Desenvolvimento

- Sempre use `python manage.py makemigrations` após alterar models
- Teste em mobile com `python manage.py runserver 0.0.0.0:8000`
- Use o admin Django para gerenciar dados rapidamente
- Implemente testes com `python manage.py test`

## 📞 Suporte

Para dúvidas sobre a aplicação, consulte:
- Documentação Django: https://docs.djangoproject.com/
- Bootstrap 5: https://getbootstrap.com/docs/5.0/
- Font Awesome: https://fontawesome.com/

---

**Versão**: 1.0.0  
**Última Atualização**: Dezembro 2025
