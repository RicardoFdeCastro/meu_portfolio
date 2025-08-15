# 🌟 Meu Portfólio com Django

Este é um projeto de **portfólio profissional** desenvolvido com **Django** para o backend e **Bootstrap 5** para o frontend.  
Ele permite gerenciar e exibir projetos de forma dinâmica usando o **Django Admin** e inclui **filtro por categorias** para facilitar a navegação.

---

## 🚀 Funcionalidades

- ✅ **Cadastro de Projetos** pelo painel administrativo
- ✅ **Upload de imagens** dos projetos
- ✅ **Links para Demo e GitHub** de cada projeto
- ✅ **Filtro por Categorias** (ex.: Web, Mobile, Data Science)
- ✅ **Interface Responsiva** com Bootstrap 5
- ✅ **Ordenação automática** dos projetos mais recentes primeiro

---

## 🛠 Tecnologias Utilizadas

- **Python 3.x**
- **Django 4.x**
- **Bootstrap 5**
- **HTML5 / CSS3**
- **Pillow** (para upload de imagens)

---

## 📂 Estrutura de Pastas

meu_portfolio/
│
├─ portfolio/ # App principal
│ ├─ migrations/
│ ├─ templates/portfolio/ # Templates HTML
│ │ └─ home.html
│ ├─ static/ # Arquivos estáticos (se necessário)
│ ├─ admin.py
│ ├─ models.py
│ ├─ views.py
│ ├─ urls.py
│
├─ meu_portfolio/ # Configurações do projeto
│ ├─ settings.py
│ ├─ urls.py
│
├─ media/ # Uploads de imagens
└─ README.md

yaml
Copiar
Editar

---

## ⚙️ Como Executar o Projeto

### 1️⃣ Clonar o repositório
```bash
git clone https://github.com/seuusuario/meu-portfolio.git
cd meu-portfolio
2️⃣ Criar ambiente virtual
bash
Copiar
Editar
python -m venv venv
venv\Scripts\activate  # Windows
# ou
source venv/bin/activate  # Linux/Mac
3️⃣ Instalar dependências
bash
Copiar
Editar
pip install -r requirements.txt
4️⃣ Configurar variáveis e banco de dados
Ajuste o arquivo settings.py se necessário.

Execute:

bash
Copiar
Editar
python manage.py makemigrations
python manage.py migrate
5️⃣ Criar superusuário para acessar o Django Admin
bash
Copiar
Editar
python manage.py createsuperuser
6️⃣ Executar o servidor
bash
Copiar
Editar
python manage.py runserver
Acesse no navegador:

cpp
Copiar
Editar
http://127.0.0.1:8000/
Painel Admin:

arduino
Copiar
Editar
http://127.0.0.1:8000/admin
📸 Demonstração
(Adicione aqui prints ou GIFs do site funcionando)

✨ Melhorias Futuras
🔹 Animações suaves na transição de categorias

🔹 Modo escuro

🔹 Página de detalhes para cada projeto

🔹 Formulário de contato integrado

📝 Licença
Este projeto é de uso pessoal.
Sinta-se livre para modificá-lo e adaptá-lo às suas necessidades.
