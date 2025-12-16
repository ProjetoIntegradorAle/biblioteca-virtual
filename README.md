# 🏛️ Biblioteca Virtual - Alexandria

## 📑 Sobre
A Biblioteca Virtual é um software que reúne trabalhos acadêmicos em um repositório digital acessível online. Com interface intuitiva e recursos de pesquisa eficientes, facilita o acesso a documentos, artigos, relatórios e vídeos produzidos por alunos do campus, promovendo o conhecimento de forma simples e democrática. 

## 🛠️ Tecnologias
HTML | CSS | PYTHON | DJANGO

## ⚙️ Instalação e Configuração
### 1. Clone o repositório
```plaintext
git clone https://github.com/ProjetoIntegradorAle/biblioteca-virtual.git
```

### 2. Crie e ative um ambiente virtual
- Windows:
```plaintext 
python -m venv venv
```
```plaintext
venv\Scripts\activate
```

- Linux/Mac:
```plaintext
python3 -m venv venv
```
```plaintext
source venv/bin/activate
```

### 3. Instale as dependências
```plaintext
pip install -r requirements.txt
```

### 4. Execute as migrações do banco de dados
```plaintext
python manage.py migrate
```

### 5. Execute o servidor
```plaintext
python manage.py runserver
```

Acesse localmente: http://localhost:8000

## 📂 Estrutura do Projeto
```plaintext
BIBLIOTECA-VIRTUAL/
├── app/                     # Aplicações principais do Django
├── config/                  # Configurações gerais do projeto
├── docs/                   # Documentação do projeto
├── media/                  # Arquivos enviados pelos usuários
├── react-jsonplaceholder/  # Frontend React
├── staticfiles/            # Arquivos estáticos (CSS, JS, imagens)
├── usuarios/               # Módulo de autenticação e perfis
├── venv/                   # Ambiente virtual
├── .gitignore              # Arquivos e pastas ignorados pelo Git
├── .python-version         # Versão do Python usada
├── db.sqlite3              # Banco de dados SQLite
├── frase.json              # Arquivo JSON 
├── manage.py               # Gerenciador do Django
├── Procfile                # Configuração para deploy (Render)
├── README.md               # Documentação do projeto
└── requirements.txt        # Dependências do projeto
```

## 📌 Funcionalidades
- Para instruções detalhadas, consulte o Manual do Usuário em: 

## 👥 Autores 
[Luana Lima](https://github.com/luanatslima) e 
[João Victor](https://github.com/jv-victtor)

## 👨‍🏫 Orientador
[Ari Oliveira](https://github.com/aribarreto)
