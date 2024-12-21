from flask import Flask, render_template, request, redirect, url_for, flash
from server import inicioUsuario

app = Flask(__name__)

db_name = ""

#aqui vamos a poner la ruta para el inciio de sesion
@app.route('/', methods=["POST", "GET"])
def inicioSesion():
    global db_name

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        db_name = inicioUsuario(username, password)

        #return redirect(url_for('home', db_name=db_name))
        return redirect('/home')

    return render_template('login.html')

#aqui vamos a poner el dashboard si es exitoso el inicio de sesion
@app.route('/home')
def home():
    print(f"{db_name}")
if __name__ == '__main__':
    app.run(debug=True)