from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
import os
from app.routes.user_routes import user_bp
from app.routes.employees_routes import employee_bp

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY') or '1017'
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

app.register_blueprint(user_bp, url_prefix='/user')
app.register_blueprint(employee_bp, url_prefix='/employees')

if __name__ == '__main__':
    app.run(debug=True)