# Aplicação Django - Relatório de Projetos China Fácil

## 📋 Visão Geral

Aplicação Django completa para gerenciamento de projetos de sourcing, baseada na estrutura de uma planilha Google Sheets. Inclui cadastro de usuários, projetos, pesquisa avançada e registro de acessos.

## 🎨 Design

- **Paleta de Cores**: Vermelho China Fácil (#C8102E), Carvão (#2C2C2C), Ouro (#D4AF37)
- **Tipografia**: Roboto para corpo, Oswald para títulos
- **Responsividade**: Totalmente adaptada para desktop e mobile


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


**Versão**: 1.0.0  
**Última Atualização**: Dezembro 2025
