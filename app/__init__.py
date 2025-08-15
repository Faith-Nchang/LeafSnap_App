from flask import Flask

def create_app():
    app = Flask(__name__, static_folder='static', template_folder='templates')
    app.config.from_object('config.Config')

    from app.routes.init import register_routes


    # Initialize routes
    register_routes(app)

    return app