from flask import Flask, render_template, request, redirect, url_for, flash
from server import inicioUsuario

app = Flask(__name__)

#declaramos las variables globales
db_name = ""
username = ""

#aqui vamos a poner la ruta para el inciio de sesion
@app.route('/', methods=["POST", "GET"])
def inicioSesion():
    global db_name, username #convertmimos en variable global el db_name y username

    if request.method == "POST":
        username = request.form.get("username") #si es obtener, obtenemos los datos del formulario html
        password = request.form.get("password")

        db_name = inicioUsuario(username, password) #llamamos a la funcion de inicar sesion, pasando los parametros

        if db_name: #si es correcto entonces mandamos a home
            return redirect(url_for('home')) 
        else:
            return render_template('error.html')

    return render_template('login.html')


#aqui vamos a poner el dashboard si es exitoso el inicio de sesion
@app.route('/home')
def home():
    usuario = username
    return render_template('home.html', user=usuario, db=db_name)


#aqui vamos a poner las opciones de los paquetes
@app.route('/paquetes', methods=["POST", "GET"])    
def paquetes():
    return render_template('paquetes.html')

if __name__ == '__main__':
    app.run(debug=True)