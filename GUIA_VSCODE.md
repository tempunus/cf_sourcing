# Guia de Edição no VSCode

## Estrutura dos Projetos

Você recebeu dois projetos:

### 1. Aplicação Django (Backend)
**Pasta**: `relatorio_projetos/`

Gerenciamento de projetos, usuários e acessos com interface web.

### 2. Dashboard Interativo (Frontend)
**Pasta**: `dashboard_interativo/`

Dashboard web estático com gráficos e visualizações de dados.

---

## Configuração do VSCode

### Extensões Recomendadas

Para melhor experiência, instale estas extensões:

**Django:**
- Python (Microsoft)
- Django (Baptiste Darthenay)
- Pylance (Microsoft)

**React/TypeScript:**
- ES7+ React/Redux/React-Native snippets (dsznajder.es7-react-js-snippets)
- Tailwind CSS IntelliSense (bradlc.vscode-tailwindcss)
- TypeScript Vue Plugin (Vue)
- Prettier - Code formatter (esbenp.prettier-vscode)

**Geral:**
- GitLens (eamodio.gitlens)
- Thunder Client (rangav.vscode-thunder-client)

### Configurar Python

1. Abra a pasta `relatorio_projetos/`
2. Pressione `Ctrl+Shift+P` (ou `Cmd+Shift+P` no Mac)
3. Digite: "Python: Select Interpreter"
4. Escolha: `./venv/bin/python`

### Configurar Node.js

1. Abra a pasta `dashboard_interativo/`
2. O VSCode detectará automaticamente Node.js

---

## Projeto Django - Edição

### Estrutura de Arquivos

```
relatorio_projetos/
├── config/
│   ├── settings.py        ← Configurações do projeto
│   ├── urls.py            ← Rotas principais
│   └── wsgi.py
├── projetos/
│   ├── models.py          ← Modelos de dados (Projeto)
│   ├── views.py           ← Lógica das páginas
│   ├── forms.py           ← Formulários
│   ├── admin.py           ← Admin do Django
│   └── templates/
│       ├── dashboard.html
│       ├── projeto_lista.html
│       ├── projeto_form.html
│       └── projeto_pesquisa.html
├── usuarios/
│   ├── models.py          ← Modelos de usuários
│   ├── views.py           ← Autenticação
│   ├── forms.py           ← Formulários de registro
│   └── templates/
│       ├── login.html
│       ├── registro.html
│       └── meus_acessos.html
├── templates/
│   └── base.html          ← Template base (navbar, estilos)
├── manage.py
└── requirements.txt       ← Dependências
```

### Fluxo de Desenvolvimento

1. **Editar Models** (`projetos/models.py`, `usuarios/models.py`)
   - Adicione novos campos
   - Execute: `python manage.py makemigrations`
   - Execute: `python manage.py migrate`

2. **Editar Views** (`projetos/views.py`, `usuarios/views.py`)
   - Modifique a lógica das páginas
   - Salve e o servidor recarrega automaticamente

3. **Editar Templates** (arquivos `.html`)
   - Modifique o HTML e CSS
   - Salve e recarregue a página no navegador

4. **Editar Formulários** (`projetos/forms.py`, `usuarios/forms.py`)
   - Adicione/remova campos
   - Sincronize com models e templates

### Iniciar Servidor Django

No terminal do VSCode:

```bash
cd relatorio_projetos
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows

python manage.py runserver
```

Acesse: http://localhost:8000

### Credenciais Padrão

- Usuário: `admin`
- Senha: `admin123`

### Comandos Úteis

```bash
# Criar novo app
python manage.py startapp nome_app

# Criar superusuário
python manage.py createsuperuser

# Resetar banco de dados
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser

# Acessar shell do Django
python manage.py shell

# Coletar arquivos estáticos
python manage.py collectstatic
```

---

## Projeto React - Edição

### Estrutura de Arquivos

```
dashboard_interativo/
├── client/
│   ├── public/
│   │   └── images/        ← Imagens do projeto
│   └── src/
│       ├── pages/
│       │   └── Home.tsx   ← Dashboard principal
│       ├── components/
│       │   ├── DashboardLayout.tsx  ← Layout principal
│       │   └── ui/        ← Componentes shadcn/ui
│       ├── contexts/      ← React contexts
│       ├── hooks/         ← Custom hooks
│       ├── lib/           ← Utilitários
│       ├── App.tsx        ← Roteamento
│       ├── main.tsx       ← Entry point
│       └── index.css      ← Estilos globais
├── server/                ← Servidor Express (produção)
├── package.json
└── README.md
```

### Fluxo de Desenvolvimento

1. **Editar Estilos** (`client/src/index.css`)
   - Modifique cores, fontes, temas
   - Salve e veja mudanças em tempo real

2. **Editar Componentes** (`client/src/components/`)
   - Modifique layout, funcionalidade
   - Hot reload automático

3. **Editar Páginas** (`client/src/pages/`)
   - Adicione novas páginas
   - Registre rotas em `App.tsx`

4. **Adicionar Componentes UI**
   - Use `shadcn/ui` quando possível
   - Customize com Tailwind CSS

### Iniciar Servidor React

No terminal do VSCode:

```bash
cd dashboard_interativo
pnpm install  # Primeira vez
pnpm dev
```

Acesse: http://localhost:3000

### Comandos Úteis

```bash
# Instalar dependência
pnpm add nome-pacote

# Remover dependência
pnpm remove nome-pacote

# Build para produção
pnpm build

# Preview do build
pnpm preview

# Verificar tipos TypeScript
pnpm check

# Formatar código
pnpm format
```

### Paleta de Cores (Tailwind)

Edite `client/src/index.css` para alterar cores:

```css
:root {
  --primary: #C8102E;           /* Vermelho China Fácil */
  --chart-1: #C8102E;           /* Gráfico 1 */
  --chart-2: #D4AF37;           /* Gráfico 2 (Ouro) */
  --chart-3: #2C2C2C;           /* Gráfico 3 (Carvão) */
}
```

---

## Dicas de Produtividade

### VSCode Shortcuts

| Atalho | Ação |
|--------|------|
| `Ctrl+P` | Buscar arquivo |
| `Ctrl+Shift+P` | Paleta de comandos |
| `Ctrl+/` | Comentar linha |
| `Alt+Up/Down` | Mover linha |
| `Ctrl+D` | Selecionar palavra |
| `F12` | Ir para definição |
| `Ctrl+Shift+F` | Buscar em arquivos |

### Debugging Django

1. Instale a extensão "Python" da Microsoft
2. Crie `.vscode/launch.json`:

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Django",
      "type": "python",
      "request": "launch",
      "program": "${workspaceFolder}/relatorio_projetos/manage.py",
      "args": ["runserver"],
      "django": true
    }
  ]
}
```

3. Pressione `F5` para iniciar debug

### Debugging React

1. Use React Developer Tools (extensão do Chrome)
2. Abra DevTools: `F12`
3. Vá para aba "Components" ou "Profiler"

---

## Estrutura de Pastas Recomendada

```
Seu Projeto/
├── relatorio_projetos/      (Django)
├── dashboard_interativo/    (React)
├── GUIA_VSCODE.md          (Este arquivo)
└── .gitignore
```

---

## Próximos Passos

1. **Abra os projetos no VSCode**
   - Arquivo → Abrir Pasta

2. **Instale extensões recomendadas**
   - Vá para Extensions (Ctrl+Shift+X)

3. **Configure interpretadores**
   - Python: Selecione venv
   - Node.js: Detectado automaticamente

4. **Inicie os servidores**
   - Django: `python manage.py runserver`
   - React: `pnpm dev`

5. **Comece a editar!**
   - Django: Edite templates, views, models
   - React: Edite componentes, estilos, páginas

---

## Suporte Rápido

### Erro: "Python interpreter not found"
- Instale Python 3.11+
- Configure em VSCode: Ctrl+Shift+P → Python: Select Interpreter

### Erro: "pnpm not found"
- Instale Node.js 22+
- Instale pnpm: `npm install -g pnpm`

### Erro: "Port already in use"
- Django: `python manage.py runserver 8001`
- React: `pnpm dev -- --port 3001`

### Servidor não recarrega
- Django: Reinicie com `Ctrl+C` e `python manage.py runserver`
- React: Salve o arquivo novamente

---

**Versão**: 1.0.0
**Data**: Dezembro 2025

Boa edição! 🚀
