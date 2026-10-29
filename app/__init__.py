from flask import Flask

def create_app():
    app = Flask(__name__)

    # Importar e registrar los Blueprints
    from .admin import admin_bp
    from .blog import blog_bp
    from .auth.routes import auth_bp
    from .productos.routes import productos_bp
    from .usuarios.routes import usuarios_bp

    app.register_blueprint(admin_bp, url_prefix='/admin')
    app.register_blueprint(blog_bp, url_prefix='/blog')
    app.register_blueprint(auth_bp)
    app.register_blueprint(productos_bp)
    app.register_blueprint(usuarios_bp)

    return app