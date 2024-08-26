from flask import Flask
from orders import orders_bp
from products import products_bp
from users import users_bp
# from products import products_bp

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(orders_bp, url_prefix='/')
app.register_blueprint(products_bp, url_prefix='/')
# app.register_blueprint(users_bp, url_prefix='/')
# app.register_blueprint(products_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)
