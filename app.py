# Importação
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = "Beni_123"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'


login_manager = LoginManager()
db = SQLAlchemy(app)
login_manager.init_app(app)
login_manager.login_view = 'login'
CORS(app)

# Modelagem
class User(db.Model, UserMixin):
 id = db.Column(db.Integer, primary_key=True)
 username = db.Column(db.String(80), nullable=False,unique=True)
 password = db.Column(db.String(80), nullable=True)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=True)

# Autenticação
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

    @app.route('/login', methods=["POST"])
    def login():
       data = request.json 
       user = User.query.filter_by(username=data.get("username")).first()

       if user and data.get("password") == user.password:
                 login_user(user)
                 return jsonify({"message": "Logged in successfully"})
       
       return jsonify({"message": "Unauthorized. Invalid credentials"}),401


    @app.route('/api/products/add', methods=["POST"])
    @login_required
    def add_products():
        data = request.json
        if 'nome' in data and 'price' in data:
            product = Product(nome=data["nome"], price=data["price"],description=data.get("description",""))
            db.session.add(product)
            db.session.commit()
            return jsonify({"message": "Product added successfully"}), 201
            return jsonify({"Invalid product data"}), 400

@app.route('/api/products/delete/<int:product_id>', methods=["DELETE"])
def delete_product(product_id):
    product = Product.query.get(product_id)
    if product:
        db.session.delete(product)
        db.session.commit()
        return jsonify({"message": "Product deleted successfully"}), 201
    return jsonify({"Product not found "}), 404

@app.route('/api/products/<int:product_id>', methods=["GET"])
def get_produtcs_details(product_id):
 product = Product.query.get(product_id)
 if product:
     return jsonify({
         "id": product.id,
         "nome": product.nome,
         "price": product.price,
         "description": product.description
     })
 return jsonify ({"message": " product not found"}), 404

@app.route('/api/products/update/<int:product_id>', methods=["PUT"])
def update_produtc(product_id):
    product = Product.query.get(product_id)
    if not product:
     return jsonify({"message": " product not found"}), 404

    data = request.json
    if 'nome' in data:
     product.nome = data ['nome']

    if 'price' in data:
     product.price = data ['price']

    if 'description' in data:
     product.description= data ['description']

    db.session.commit()
    return jsonify({'message': 'Product update sucessfully'})

@app.route('/api/products', methods=["GET"])
def get_products():
    products = Product.query.all()
    product_list = []

    for product in products:
        product_data = {
            "id": product.id,
            "nome": product.nome,
            "price": product.price
        }
        product_list.append(product_data)  # ✅ Adiciona cada produto na lista

    return jsonify(product_list)  # ✅ Agora retorna toda a lista depois do loop


















# Definir rota raiz
@app.route('/')
def hello_World():
   return 'Hello World'
if __name__== "__main__":
    app.run(debug=True)