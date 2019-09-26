from flask import Flask
from flask_migrate import Migrate
from .Models.Product import configure as config_db
from .serializer import configure as config_ma

def create_app():
    # app configuration
    app = Flask(__name__)

    # sqlalchemy configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/crud.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # setup db and serializer 
    config_db(app)
    config_ma(app)

    # setup migration
    Migrate(app, app.db)

    from .Controllers.ProductController import bp_products
    app.register_blueprint(bp_products)
    return app