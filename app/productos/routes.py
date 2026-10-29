from flask import render_template
from . import productos_bp

@productos_bp.route('/productos')
def lista_productos():
    # Lista de productos requerida
    productos = ["Gaseosas", "Lacteos", "Golosinas"]
    return render_template('productos/index.html', productos=productos)