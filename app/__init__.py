from flask import Flask
from app.routes.init import register_routes

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Initialize routes
    register_routes(app)

    return app