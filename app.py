from flask import Flask

from src.config.app import Environment
from src.models import db
from src.views.InventoryView import inventory_blueprint

def create_app():
    """
    Create a instance of Flask App
    """
    app = Flask(__name__)
    #set config
    app.config.from_object(Environment)
    #start db
    db.init_app(app)

    #set blueprints
    app.register_blueprint(inventory_blueprint, url_prefix='/api/v1/inventory')
    
    return app