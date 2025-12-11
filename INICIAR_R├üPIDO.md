# Guia de Inicialização Rápida

## ⚡ Em 5 Minutos

### Pré-requisitos
- Python 3.11+
- Node.js 22+
- pnpm

### Passo 1: Backend (Django)

```bash
# Ativar ambiente virtual
python3.11 -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows

# Instalar dependências
pip install -r requirements.txt

# Executar migrações
python manage.py migrate

# Criar admin
python manage.py createsuperuser
# Username: admin
# Password: admin123

# Iniciar servidor
python manage.py runserver
```

**Acesso**: http://localhost:8000

---

### Passo 2: Frontend (React)

Em outro terminal:

```bash
# Navegar para frontend
cd frontend

# Instalar dependências
pnpm install

# Iniciar servidor
pnpm dev
```

**Acesso**: http://localhost:3000

---

## 📋 Checklist de Configuração

- [ ] Python 3.11+ instalado
- [ ] Node.js 22+ instalado
- [ ] pnpm instalado
- [ ] Ambiente virtual criado
- [ ] Dependências instaladas (pip)
- [ ] Migrações executadas
- [ ] Superusuário criado
- [ ] Servidor Django rodando
- [ ] Dependências frontend instaladas (pnpm)
- [ ] Servidor React rodando

---

## 🔑 Credenciais Padrão

**Admin Django**:
- Username: `admin`
- Password: `admin123`

**Acesso Admin**: http://localhost:8000/admin/

---

## 📱 Testar no Celular

### Descobrir IP local
```bash
# Linux/Mac
ifconfig | grep "inet "

# Windows
ipconfig
```

### Acessar do celular
```
http://SEU_IP:8000  (Django)
http://SEU_IP:3000  (React)
```

---

## 🚀 Comandos Úteis

### Django

```bash
# Criar novo app
python manage.py startapp nome_app

# Fazer migrações
python manage.py makemigrations

# Aplicar migrações
python manage.py migrate

# Shell interativo
python manage.py shell

# Resetar banco
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser

# Coletar estáticos
python manage.py collectstatic

# Rodar em IP específico
python manage.py runserver 0.0.0.0:8000
```

### React

```bash
# Instalar pacote
pnpm add nome-pacote

# Remover pacote
pnpm remove nome-pacote

# Build para produção
pnpm build

# Preview do build
pnpm preview

# Verificar tipos
pnpm check

# Formatar código
pnpm format
```

---

## 🐛 Troubleshooting Rápido

### Erro: "Port 8000 already in use"
```bash
python manage.py runserver 8001
```

### Erro: "Port 3000 already in use"
```bash
cd frontend
pnpm dev -- --port 3001
```

### Erro: "Module not found"
```bash
# Backend
pip install -r requirements.txt

# Frontend
cd frontend
pnpm install
```

### Erro: "Database locked"
```bash
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

### Erro: "Python not found"
- Instale Python 3.11+ de https://www.python.org/
- Adicione ao PATH

### Erro: "pnpm not found"
```bash
npm install -g pnpm
```

---

## 📂 Estrutura Rápida

```
china_facil_completo/
├── Backend Django (raiz)
│   ├── config/
│   ├── projetos/
│   ├── usuarios/
│   ├── templates/
│   ├── manage.py
│   └── requirements.txt
│
└── frontend/
    ├── client/
    │   ├── public/
    │   └── src/
    ├── server/
    ├── package.json
    └── vite.config.ts
```

---

## 🌐 URLs Principais

### Backend
- Dashboard: http://localhost:8000/dashboard/
- Projetos: http://localhost:8000/projetos/
- Novo Projeto: http://localhost:8000/projetos/novo/
- Pesquisa: http://localhost:8000/projetos/pesquisa/
- Admin: http://localhost:8000/admin/

### Frontend
- Dashboard: http://localhost:3000/

---

## 📊 Dados de Teste

Após criar o superusuário, adicione dados via admin:

1. Acesse http://localhost:8000/admin/
2. Clique em "Projetos"
3. Clique em "Adicionar Projeto"
4. Preencha os dados
5. Salve

Ou use o formulário em http://localhost:8000/projetos/novo/

---

## 🎨 Customizações Rápidas

### Alterar cor primária

**Django** - `templates/base.html`:
```css
--primary-red: #C8102E;
```

**React** - `frontend/client/src/index.css`:
```css
--primary: #C8102E;
```

### Alterar título

**Django** - `templates/base.html`:
```html
<title>Seu Título</title>
```

**React** - `frontend/client/index.html`:
```html
<title>Seu Título</title>
```

---

## 📚 Documentação Completa

- **ESTRUTURA_COMPLETA.md** - Estrutura detalhada do projeto
- **FORMULARIOS_DISPONÍVEIS.md** - Todos os formulários
- **GUIA_VSCODE.md** - Edição no VSCode
- **README.md** - Documentação geral

---

## ✅ Próximos Passos

1. ✅ Instalar dependências
2. ✅ Executar migrações
3. ✅ Criar superusuário
4. ✅ Iniciar servidores
5. ⬜ Adicionar dados de teste
6. ⬜ Customizar conforme necessário
7. ⬜ Implementar novas funcionalidades

---

**Versão**: 1.0.0  
**Data**: Dezembro 2025

Pronto para começar! 🚀
