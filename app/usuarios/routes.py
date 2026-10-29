from flask import Blueprint, render_template

usuarios_bp = Blueprint('usuarios', __name__, url_prefix='/usuarios', template_folder='templates')

@usuarios_bp.route('/lista')
def lista():
    # Lista de usuarios de ejemplo
    lista_usuarios = ["Juan", "Maria", "Carlos", "Dante"]
    return render_template('lista.html', usuarios=lista_usuarios)

@usuarios_bp.route('/perfil/<nombre>')
def perfil(nombre):
    return f"<h1>Bienvenido, {nombre}!</h1><p>Esta es tu página de perfil.</p>"