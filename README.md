💻 Projeto

Este é um projeto de API para um sistema de e-commerce, desenvolvido com Flask e SQLite. A API permite autenticação de usuários, gerenciamento de produtos e
 funcionalidades de carrinho de compras.

 

🚀  Tecnologias Utilizadas
Flask – Framework web para Python
Flask-SQLAlchemy – ORM para manipulação do banco de dados
Flask-Login – Gerenciamento de autenticação de usuários
Flask-CORS – Permissão de acesso a partir de outras origens
SQLite – Banco de dados local


🔧 Instalação
Clone o repositório

bash
git clone https://github.com/seu-repositorio.git

bash
python -m venv venv
source venv/bin/activate  # No Windows use: venv\Scripts\activate
Instale as dependências

bash
pip install -r requirements.txt

Abra um terminal Python e execute:
from app import db
db.create_all()

bash
python app.py
A API estará disponível em: http://127.0.0.1:5000

Autenticação
O sistema usa Flask-Login para gerenciar sessões de usuários. Algumas rotas exigem autenticação para acesso.



📌 Rotas de Autenticação
POST /login – Login de usuário
POST /logout – Logout do usuário
Formato esperado para login:

json
{
  "username": "usuario123",
  "password": "senha123"
}



🛒 Rotas da API
📦 Produtos
GET /api/products → Lista todos os produtos
GET /api/products/{id} → Detalhes de um produto
POST /api/products/add → Adiciona um novo produto (autenticado)
PUT /api/products/update/{id} → Atualiza um produto (autenticado)
DELETE /api/products/delete/{id} → Remove um produto (autenticado)
Formato esperado para adicionar um produto:

json
{
  "nome": "Produto X",
  "price": 99.99,
  "description": "Descrição do produto X"
}



🛍️ Carrinho de Compras
POST /api/cart/add/{product_id} → Adiciona um produto ao carrinho (autenticado)
DELETE /api/cart/remove/{product_id} → Remove um item do carrinho (autenticado)
GET /api/cart → Lista os itens do carrinho (autenticado)
POST /api/cart/checkout → Finaliza a compra e limpa o carrinho (autenticado)



📂 Estrutura do Banco de Dados
Tabela User
Campo	         Tipo	           Descrição
id	         Integer	         Chave primária
username    String(80)      Nome de usuário (único)
password	  String(80)	       Senha do usuário



Tabela Product
Campo           	Tipo             	Descrição
id	             Integer	       Chave primária
nome	         String(120)	    Nome do produto
price           	Float        	Preço do produto
description	       Text	       Descrição do produto



Tabela CartItem
Campo	          Tipo	           Descrição
id	           Integer       	Chave primária
user_id	       Integer	      Chave estrangeira referenciando User.id
product_id   	Integer        	Chave estrangeira referenciando Product.id



📘 Documentação Swagger
A API segue a especificação Swagger 2.0, disponível no arquivo swagger.yaml.
