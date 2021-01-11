from flask import Flask

from src.models import db
from src.views.InventoryView import inventory_blueprint
from src.utils.error import handle_internal_server_error

def create_app():
    """
    Create a instance of Flask App
    """
    app = Flask(__name__)
    #set config
    app.config.from_object('config')
    #start db
    db.init_app(app)

    #set blueprints
    app.register_blueprint(inventory_blueprint, url_prefix='/api/v1/inventory')

    #handlers
    app.register_error_handler(500, handle_internal_server_error)
    return app

def create_test_app():
    app = create_app()
    return app