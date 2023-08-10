from .front import front_bp
from .admin import admin_bp
from .auth import auth_bp

def register_bp(app):
    app.register_blueprint(front_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(auth_bp)