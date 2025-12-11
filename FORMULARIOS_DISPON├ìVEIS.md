# Formulários Disponíveis - China Fácil

## Sumário de Formulários

Todos os formulários estão implementados e prontos para uso. Abaixo está a documentação completa de cada um.

---

## 1. Formulário de Cadastro de Projeto

**Arquivo**: `projetos/forms.py` - `ProjetoForm`

**Localização Web**: `/projetos/novo/` ou `/projetos/<id>/editar/`

**Campos**:
```
- CF Código (CharField, max_length=20, único)
- Cliente (CharField, max_length=200)
- Plataforma (ChoiceField)
  * Alibaba
  * Global Sources
  * TradeKey
  * Outra
- Fornecedor (CharField, max_length=200)
- Descrição (TextField)
- Status (ChoiceField)
  * Em Análise
  * Em Cotação
  * Aguardando Aprovação
  * Concluído
- Data de Início (DateField)
- Operador (ModelChoiceField - Usuário)
```

**Validações**:
- CF Código é obrigatório e único
- Cliente é obrigatório
- Descrição mínimo 10 caracteres
- Data de início não pode ser futura

**Exemplo de Uso**:
```html
<form method="post">
  {% csrf_token %}
  {{ form.as_p }}
  <button type="submit">Salvar Projeto</button>
</form>
```

---

## 2. Formulário de Pesquisa Avançada

**Arquivo**: `projetos/forms.py` - `PesquisaProjetoForm`

**Localização Web**: `/projetos/pesquisa/`

**Campos**:
```
- CF (CharField, opcional)
- Cliente (CharField, opcional)
- Status (ChoiceField, opcional)
  * Em Análise
  * Em Cotação
  * Aguardando Aprovação
  * Concluído
- Data Atualização De (DateField, opcional)
- Data Atualização Até (DateField, opcional)
```

**Validações**:
- Data "De" não pode ser maior que data "Até"
- Pelo menos um campo deve ser preenchido

**Exemplo de Uso**:
```html
<form method="get">
  {{ form.as_p }}
  <button type="submit">Pesquisar</button>
</form>
```

---

## 3. Formulário de Registro de Usuário

**Arquivo**: `usuarios/forms.py` - `RegistroForm`

**Localização Web**: `/registro/`

**Campos**:
```
- Username (CharField, max_length=150, único)
- Email (EmailField, único)
- Senha (PasswordInput)
- Confirmar Senha (PasswordInput)
- Primeiro Nome (CharField, max_length=30)
- Último Nome (CharField, max_length=150)
```

**Validações**:
- Username: mínimo 3 caracteres, sem espaços
- Email: formato válido, único
- Senha: mínimo 8 caracteres, com números e letras
- Senhas devem ser iguais
- Nomes: sem números

**Exemplo de Uso**:
```html
<form method="post">
  {% csrf_token %}
  {{ form.as_p }}
  <button type="submit">Registrar</button>
</form>
```

---

## 4. Formulário de Login

**Arquivo**: `usuarios/forms.py` - `LoginForm`

**Localização Web**: `/`

**Campos**:
```
- Username (CharField)
- Senha (PasswordInput)
- Lembrar-me (BooleanField, opcional)
```

**Validações**:
- Username e senha obrigatórios
- Credenciais devem ser válidas

**Exemplo de Uso**:
```html
<form method="post">
  {% csrf_token %}
  {{ form.as_p }}
  <button type="submit">Login</button>
</form>
```

---

## 5. Formulário de Perfil de Usuário

**Arquivo**: `usuarios/forms.py` - `PerfilForm`

**Localização Web**: `/perfil/`

**Campos**:
```
- Primeiro Nome (CharField, max_length=30)
- Último Nome (CharField, max_length=150)
- Email (EmailField)
- Telefone (CharField, max_length=20, opcional)
- Cargo (CharField, max_length=100, opcional)
- Departamento (CharField, max_length=100, opcional)
```

**Validações**:
- Email deve ser único (exceto email atual)
- Telefone: apenas números e caracteres especiais
- Nomes: sem números

**Exemplo de Uso**:
```html
<form method="post">
  {% csrf_token %}
  {{ form.as_p }}
  <button type="submit">Atualizar Perfil</button>
</form>
```

---

## 6. Componente de Busca (React)

**Arquivo**: `frontend/client/src/pages/Home.tsx`

**Localização**: Dashboard principal

**Funcionalidades**:
```
- Busca por texto em tempo real
- Busca por CF
- Busca por Cliente
- Busca por Nome do Projeto
```

**Exemplo de Uso**:
```typescript
<input 
  type="text" 
  placeholder="Buscar projeto..." 
  onChange={(e) => handleSearch(e.target.value)}
/>
```

---

## 7. Componente de Filtros (React)

**Arquivo**: `frontend/client/src/pages/Home.tsx`

**Localização**: Dashboard principal

**Filtros Disponíveis**:
```
- Por Status
  * Em Análise
  * Em Cotação
  * Aguardando Aprovação
  * Concluído
- Por Data de Atualização
  * Últimos 7 dias
  * Últimos 30 dias
  * Últimos 90 dias
  * Personalizado (de/até)
- Por Cliente
```

**Exemplo de Uso**:
```typescript
<select onChange={(e) => handleStatusFilter(e.target.value)}>
  <option value="">Todos os Status</option>
  <option value="analise">Em Análise</option>
  <option value="cotacao">Em Cotação</option>
</select>
```

---

## 8. Formulário de Exportação (React)

**Arquivo**: `frontend/client/src/pages/Home.tsx`

**Localização**: Dashboard - Botão "Exportar Relatório"

**Formatos Suportados**:
- CSV
- Excel (.xlsx)
- PDF

**Exemplo de Uso**:
```typescript
<Button onClick={() => exportData('csv')}>
  Exportar como CSV
</Button>
```

---

## Fluxo de Formulários

### Criação de Projeto
```
1. Usuário clica em "Novo Projeto"
2. Formulário ProjetoForm é exibido
3. Usuário preenche campos
4. Validação no servidor
5. Projeto salvo no banco
6. Redirecionado para lista de projetos
```

### Pesquisa de Projeto
```
1. Usuário acessa "/projetos/pesquisa/"
2. Formulário PesquisaProjetoForm é exibido
3. Usuário preenche filtros
4. Formulário é enviado (GET)
5. Resultados são filtrados
6. Tabela é atualizada
```

### Registro de Novo Usuário
```
1. Usuário acessa "/registro/"
2. Formulário RegistroForm é exibido
3. Usuário preenche dados
4. Validação de email único
5. Validação de senha
6. Usuário é criado
7. Redirecionado para login
```

### Login
```
1. Usuário acessa "/"
2. Formulário LoginForm é exibido
3. Usuário preenche credenciais
4. Validação de autenticação
5. RegistroAcesso é criado
6. Redirecionado para dashboard
```

---

## Validações Implementadas

### Backend (Django)

```python
# Validação de CF único
def clean_cf_codigo(self):
    cf = self.cleaned_data.get('cf_codigo')
    if Projeto.objects.filter(cf_codigo=cf).exists():
        raise ValidationError("CF já existe")

# Validação de datas
def clean(self):
    if self.cleaned_data.get('data_inicio') > timezone.now().date():
        raise ValidationError("Data não pode ser futura")
```

### Frontend (React)

```typescript
// Validação de email
const validateEmail = (email: string) => {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
};

// Validação de data
const validateDate = (date: string) => {
  return new Date(date) <= new Date();
};
```

---

## Customização de Formulários

### Adicionar novo campo

**1. No Model** (`projetos/models.py`):
```python
class Projeto(models.Model):
    novo_campo = models.CharField(max_length=100, blank=True)
```

**2. No Form** (`projetos/forms.py`):
```python
class ProjetoForm(forms.ModelForm):
    class Meta:
        fields = [..., 'novo_campo']
```

**3. No Template**:
```html
{{ form.novo_campo }}
```

### Alterar validações

**1. No Form**:
```python
def clean_novo_campo(self):
    valor = self.cleaned_data.get('novo_campo')
    if not valor.startswith('CF'):
        raise ValidationError("Deve começar com CF")
    return valor
```

### Adicionar campo customizado

```python
class ProjetoForm(forms.ModelForm):
    campo_customizado = forms.CharField(
        label="Meu Campo",
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite algo'
        })
    )
```

---

## Testes de Formulários

### Testar Formulário de Projeto

```bash
python manage.py shell
```

```python
from projetos.forms import ProjetoForm

# Dados válidos
dados = {
    'cf_codigo': 'CF-2025-001',
    'cliente': 'Teste Ltda',
    'plataforma': 'alibaba',
    'fornecedor': 'Fornecedor Teste',
    'descricao': 'Descrição do projeto',
    'status': 'analise',
    'data_inicio': '2025-01-01',
    'operador': 1
}

form = ProjetoForm(data=dados)
print(form.is_valid())  # True
```

---

## Erros Comuns

### "Este campo é obrigatório"
- Verifique se todos os campos required=True estão preenchidos

### "Valor inválido para este campo"
- Verifique o tipo de dado (data, número, etc)
- Verifique o formato esperado

### "Este valor já existe"
- Campo tem unique=True
- Verifique se o valor já está no banco

### "Senhas não coincidem"
- Confirme que as duas senhas são idênticas
- Verifique espaços em branco

---

## Próximos Passos

1. Customize os formulários conforme necessário
2. Adicione mais validações
3. Implemente upload de arquivos
4. Configure email para confirmação
5. Implemente CAPTCHA para registro

---

**Versão**: 1.0.0  
**Data**: Dezembro 2025
