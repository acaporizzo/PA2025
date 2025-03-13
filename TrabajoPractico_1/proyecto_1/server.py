# Ejemplo de aplicación principal en Flask
from flask import render_template
from modules.config import app

# Página de inicio
@app.route('/')
def index():
    #cantidad=20
    #
    return render_template('inicio.html')

@app.route('/saludar')
def funcion_saudar():
    return render_template('saludo.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)