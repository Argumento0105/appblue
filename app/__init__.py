from flask import Flask

def create_app():
    app = Flask(__name__)

    # Importar e registrar los Blueprints con sus prefijos URL
    from .admin import admin_bp
    from .blog import blog_bp

    app.register_blueprint(admin_bp, url_prefix='/admin')
    app.register_blueprint(blog_bp, url_prefix='/blog')

    return app