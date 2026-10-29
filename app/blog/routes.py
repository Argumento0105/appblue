from flask import render_template
from . import blog_bp

# Base de datos simulada para las entradas
ENTRADAS = {
    1: "Introducción a Flask y Blueprints en Python",
    2: "Cómo estructurar aplicaciones modulares profesionales",
    3: "Uso avanzado de plantillas Jinja2 y herencia"
}

@blog_bp.route('/entrada/<int:id>')
def entrada(id):
    titulo = ENTRADAS.get(id, f"Entrada no encontrada (ID: {id})")
    return render_template('blog/entrada.html', id=id, titulo=titulo)