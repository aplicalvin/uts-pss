import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# --- KONFIGURASI DATABASE ---
DB_USER = os.environ.get('MYSQL_USER', 'root')
DB_PASS = os.environ.get('MYSQL_PASSWORD', 'rootpass')
DB_HOST = os.environ.get('MYSQL_HOST', 'db') 
DB_NAME = os.environ.get('MYSQL_DATABASE', 'mydatabase')

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# --- MODEL DATABASE ---

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True) # Tambahkan description
    price = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Product {self.name}>'

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Product {self.name}>'

# --- ROUTES (URL) ---

@app.route('/')
def dashboard():
    """Halaman dashboard utama."""
    return render_template('dashboard.html')

# --- CRUD User ---

@app.route('/users')
def list_users():
    """Menampilkan semua user (Read)."""
    users = User.query.all()
    return render_template('users.html', users=users)

@app.route('/users/add', methods=['POST'])
def add_user():
    """Menambah user baru (Create)."""
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        new_user = User(username=username, email=email)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('list_users'))

@app.route('/users/update/<int:id>', methods=['POST'])
def update_user(id):
    """Update user (Update)."""
    user = User.query.get_or_404(id)
    if request.method == 'POST':
        user.username = request.form['username']
        user.email = request.form['email']
        db.session.commit()
        return redirect(url_for('list_users'))

@app.route('/users/delete/<int:id>')
def delete_user(id):
    """Menghapus user (Delete)."""
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('list_users'))

# --- CRUD Product ---
@app.route('/products')
def list_products():
    """Menampilkan semua produk (Read)."""
    products = Product.query.all()
    # Kirim juga 'product_to_edit' sebagai None agar template tidak error
    return render_template('products.html', products=products, product_to_edit=None)

@app.route('/products/add', methods=['POST'])
def add_product():
    """Menambah produk baru (Create)."""
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description'] # Ambil description
        price = request.form['price']
        
        new_product = Product(name=name, description=description, price=price)
        db.session.add(new_product)
        db.session.commit()
        return redirect(url_for('list_products'))

@app.route('/products/edit/<int:id>')
def edit_product_page(id):
    """Menampilkan halaman produk dengan form edit terisi (Halaman Update)."""
    product_to_edit = Product.query.get_or_404(id)
    all_products = Product.query.all()
    # Kita kirim data produk yg mau diedit dan semua produk ke template
    return render_template('products.html', products=all_products, product_to_edit=product_to_edit)

@app.route('/products/update/<int:id>', methods=['POST'])
def update_product(id):
    """Memproses update produk (Update)."""
    product = Product.query.get_or_404(id)
    if request.method == 'POST':
        product.name = request.form['name']
        product.description = request.form['description'] # Update description
        product.price = request.form['price']
        db.session.commit()
        return redirect(url_for('list_products'))

@app.route('/products/delete/<int:id>')
def delete_product(id):
    """Menghapus produk (Delete)."""
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    return redirect(url_for('list_products'))



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0')