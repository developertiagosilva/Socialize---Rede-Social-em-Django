# 🌐 Socialize - Rede Social em Django

O **Socialize** é uma aplicação web de rede social desenvolvida em Python e Django. O projeto foi projetado com foco em boas práticas de arquitetura, modularização de apps, relacionamentos de banco de dados, autenticação de usuários e uma interface limpa e responsiva.

---

## 🚀 Funcionalidades

### 👤 Autenticação e Perfis de Usuário
- **Cadastro e Login:** Validação de credenciais e senhas coincidentes.
- **Criação Automática de Perfil:** Utilização de *Django Signals* para gerar o perfil automaticamente após o registro.
- **Página de Perfil (`/profile/<username>/`):** Visualização de dados do usuário, biografia, foto de perfil (avatar), histórico de posts e contadores.
- **Edição de Perfil:** Atualização de foto e biografia com suporte a upload de arquivos (*media*).
- **Exclusão de Conta:** Exclusão em cascata do usuário e todos os seus dados associados.

### 📝 Posts e Feed
- **Criação de Publicações:** Publicação de textos no Feed principal.
- **Feed de Notícias:** Exibição ordenada dos posts do mais recente ao mais antigo.
- **Curtidas em Posts:** Sistema de toggle para curtir e descurtir posts principais com contagem dinâmica.

### 💬 Comentários e Respostas Aninhadas
- **Comentários Principais:** Permite comentar diretamente nas publicações.
- **Respostas Aninhadas (Threads):** Sistema de respostas diretas aos comentários (comentário do comentário).
- **Curtidas em Comentários:** Sistema de curtidas individuais para cada comentário e resposta.

### 🤝 Conexões
- **Seguir / Deixar de Seguir:** Botão dinâmico para seguir outros usuários diretamente pelos posts do Feed ou pela página de perfil.

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3.12+
- **Framework Web:** Django 6.1
- **Banco de Dados:** SQLite (Desenvolvimento) / ORM Django
- **Front-end:** HTML5, CSS3, Bootstrap 5
- **Gerenciamento de Ambientes:** Virtualenv (`.venv`)

---

## 📂 Estrutura do Projeto

```text
rede_social_socialize/
│
├── socialize_core/       # Configurações globais do Django (settings, urls, wsgi)
├── profiles/             # App de gestão de usuários, autenticação e perfis
│   ├── models.py         # Model Profile
│   ├── views.py          # Views de Login, Registro, Perfil e Seguir
│   ├── forms.py          # Formulários de Cadastro e Edição de Perfil
│   └── signals.py        # Signal post_save para automação de Perfil
│
├── posts/                # App de publicações, comentários e interações
│   ├── models.py         # Models Post e Comment
│   ├── views.py          # Views de Criar Post, Comentar e Curtir
│   └── forms.py          # Formulários de Post
│
├── media/                # Diretório para uploads dos usuários (avatars)
├── static/               # Arquivos estáticos globais (imagens, CSS)
├── manage.py             # CLI do Django
└── README.md             # Documentação do projeto