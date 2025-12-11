# Estrutura Consolidada - China Fácil

## Visão Geral

Projeto integrado com Django (Backend) e React (Frontend) para gerenciamento completo de projetos de sourcing.

## Estrutura de Pastas

```
china_facil_completo/
│
├── Backend (Django)
│   ├── config/                    # Configurações do Django
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   │
│   ├── projetos/                  # App de Projetos
│   │   ├── models.py              # Modelo Projeto
│   │   ├── views.py               # Views de projetos
│   │   ├── forms.py               # Formulários
│   │   ├── admin.py
│   │   ├── urls.py
│   │   └── templates/
│   │       ├── dashboard.html
│   │       ├── projeto_lista.html
│   │       ├── projeto_form.html
│   │       ├── projeto_pesquisa.html
│   │       ├── projeto_detalhe.html
│   │       └── projeto_confirmar_delete.html
│   │
│   ├── usuarios/                  # App de Usuários
│   │   ├── models.py              # Modelos (RegistroAcesso, PerfilUsuario)
│   │   ├── views.py               # Views de autenticação
│   │   ├── forms.py               # Formulários de registro
│   │   ├── admin.py
│   │   ├── urls.py
│   │   └── templates/
│   │       ├── login.html
│   │       ├── registro.html
│   │       ├── meus_acessos.html
│   │       └── todos_acessos.html
│   │
│   ├── templates/                 # Templates base
│   │   └── base.html              # Template base com navbar
│   │
│   ├── static/                    # Arquivos estáticos
│   │   ├── css/
│   │   ├── js/
│   │   └── images/
│   │
│   ├── media/                     # Uploads de usuários
│   │
│   ├── manage.py
│   ├── requirements.txt
│   └── db.sqlite3                 # Banco de dados
│
├── Frontend (React)
│   ├── client/
│   │   ├── public/
│   │   │   ├── images/            # Imagens do dashboard
│   │   │   │   ├── hero-bg.jpg
│   │   │   │   ├── avatar-placeholder.jpg
│   │   │   │   └── chart-placeholder.jpg
│   │   │   └── index.html
│   │   │
│   │   └── src/
│   │       ├── pages/
│   │       │   ├── Home.tsx       # Dashboard principal
│   │       │   └── NotFound.tsx
│   │       │
│   │       ├── components/
│   │       │   ├── DashboardLayout.tsx  # Layout com sidebar
│   │       │   ├── ErrorBoundary.tsx
│   │       │   └── ui/            # Componentes shadcn/ui
│   │       │       ├── button.tsx
│   │       │       ├── card.tsx
│   │       │       ├── progress.tsx
│   │       │       ├── separator.tsx
│   │       │       ├── sonner.tsx
│   │       │       └── tooltip.tsx
│   │       │
│   │       ├── contexts/
│   │       │   └── ThemeContext.tsx
│   │       │
│   │       ├── hooks/
│   │       │   └── useTheme.ts
│   │       │
│   │       ├── lib/
│   │       │   └── utils.ts
│   │       │
│   │       ├── App.tsx            # Roteamento principal
│   │       ├── main.tsx           # Entry point
│   │       └── index.css          # Estilos globais
│   │
│   ├── server/
│   │   └── index.ts               # Servidor Express (produção)
│   │
│   ├── package.json
│   ├── tsconfig.json
│   ├── vite.config.ts
│   └── README.md
│
├── README.md                      # Documentação geral
├── GUIA_VSCODE.md                # Guia de edição
├── ESTRUTURA_COMPLETA.md         # Este arquivo
└── requirements.txt              # Dependências Python
```

## Formulários Implementados

### Django - Formulários de Projetos

#### 1. **ProjetoForm** (`projetos/forms.py`)
Formulário para criar/editar projetos com campos:
- CF Código
- Cliente
- Plataforma (Alibaba, Global Sources, etc)
- Fornecedor
- Descrição
- Status (Em Análise, Em Cotação, Aguardando, Concluído)
- Data de Início
- Operador (usuário responsável)

#### 2. **PesquisaProjetoForm** (`projetos/forms.py`)
Formulário para pesquisa avançada:
- Buscar por CF
- Buscar por Cliente
- Filtrar por Status
- Filtrar por Data de Atualização (de/até)

### Django - Formulários de Usuários

#### 3. **RegistroForm** (`usuarios/forms.py`)
Formulário de registro de novo usuário:
- Username
- Email
- Senha
- Confirmar Senha
- Primeiro Nome
- Último Nome

#### 4. **LoginForm** (`usuarios/forms.py`)
Formulário de login:
- Username
- Senha
- Lembrar-me

#### 5. **PerfilForm** (`usuarios/forms.py`)
Formulário para editar perfil:
- Primeiro Nome
- Último Nome
- Email
- Telefone
- Cargo
- Departamento

### React - Formulários/Componentes

#### 6. **Busca de Projetos** (Home.tsx)
Campo de busca com:
- Busca por texto
- Filtro por status
- Filtro por data

#### 7. **Filtros Avançados** (Home.tsx)
Componentes de filtro:
- Data de atualização (range)
- Status (multi-select)
- Cliente (busca)

## Funcionalidades Completas

### Backend Django

✅ **Autenticação**
- Login/Logout
- Registro de novos usuários
- Perfil de usuário
- Recuperação de senha

✅ **Gerenciamento de Projetos**
- CRUD completo (Create, Read, Update, Delete)
- Listagem paginada
- Pesquisa avançada
- Filtros múltiplos
- Exportação de dados

✅ **Registro de Acessos**
- Login/Logout automático
- IP do acesso
- Localização geográfica
- Duração da sessão
- Histórico completo

✅ **Admin Django**
- Gerenciamento de projetos
- Gerenciamento de usuários
- Visualização de acessos

### Frontend React

✅ **Dashboard Interativo**
- KPIs em tempo real
- Gráficos de evolução
- Gráficos de status
- Tabelas responsivas
- Busca e filtros

✅ **Responsividade**
- Desktop (1920px+)
- Tablet (768px-1024px)
- Mobile (320px-767px)

✅ **Design**
- Paleta China Fácil
- Tipografia profissional
- Animações suaves
- Modo claro/escuro (preparado)

## Como Usar

### 1. Instalar Dependências

**Backend:**
```bash
cd /path/to/china_facil_completo
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
```

**Frontend:**
```bash
cd frontend
pnpm install
```

### 2. Iniciar Servidores

**Terminal 1 - Backend:**
```bash
python manage.py runserver
# Acesso: http://localhost:8000
```

**Terminal 2 - Frontend:**
```bash
cd frontend
pnpm dev
# Acesso: http://localhost:3000
```

### 3. Acessar Admin Django

```
http://localhost:8000/admin/
Usuário: admin
Senha: admin123
```

## Fluxo de Dados

```
Frontend (React)
    ↓
Busca/Filtro de Projetos
    ↓
Backend (Django API)
    ↓
Database (SQLite)
    ↓
Retorna dados
    ↓
Frontend renderiza gráficos/tabelas
```

## Customizações Comuns

### Adicionar novo campo ao Projeto

1. Edite `projetos/models.py`:
```python
class Projeto(models.Model):
    novo_campo = models.CharField(max_length=100, blank=True)
```

2. Crie migração:
```bash
python manage.py makemigrations
python manage.py migrate
```

3. Atualize `projetos/forms.py`:
```python
class ProjetoForm(forms.ModelForm):
    class Meta:
        fields = [..., 'novo_campo']
```

4. Atualize templates Django
5. Atualize componentes React se necessário

### Alterar cores do tema

**Django** - Edite `templates/base.html`:
```css
--primary-red: #C8102E;
```

**React** - Edite `frontend/client/src/index.css`:
```css
:root {
  --primary: #C8102E;
  --chart-1: #C8102E;
}
```

## Segurança

- ✅ CSRF protection (Django)
- ✅ Senhas com hash (Django)
- ✅ Validação de formulários
- ✅ Autenticação obrigatória
- ✅ Proteção contra XSS (React)

### Para Produção

1. Altere `DEBUG = False` em `config/settings.py`
2. Configure `ALLOWED_HOSTS`
3. Use variáveis de ambiente para `SECRET_KEY`
4. Configure HTTPS
5. Use PostgreSQL em vez de SQLite
6. Configure CORS adequadamente

## Troubleshooting

### Erro: "Module not found"
```bash
# Backend
pip install -r requirements.txt

# Frontend
cd frontend && pnpm install
```

### Erro: "Port already in use"
```bash
# Backend
python manage.py runserver 8001

# Frontend
cd frontend && pnpm dev -- --port 3001
```

### Erro: "Database locked"
```bash
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

### Erro: "Node modules corrupted"
```bash
cd frontend
rm -rf node_modules pnpm-lock.yaml
pnpm install
```

## Próximos Passos

1. Customize os formulários conforme necessário
2. Adicione mais campos aos modelos
3. Implemente autenticação com terceiros (Google, GitHub)
4. Configure email para recuperação de senha
5. Implemente testes automatizados
6. Configure CI/CD para deploy automático

## Suporte

- Django: https://docs.djangoproject.com/
- React: https://react.dev/
- Tailwind: https://tailwindcss.com/
- Recharts: https://recharts.org/

---

**Versão**: 1.0.0  
**Data**: Dezembro 2025
