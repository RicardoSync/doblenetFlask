from flask import Flask, render_template, request, redirect, url_for, flash
from server import loginUsername
from consultas import numClientes

app = Flask(__name__)
app.secret_key = "super_secret_key"  # Necesario para usar mensajes flash


@app.route("/", methods=["GET", "POST"])

def login():
    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        db_name = loginUsername(username, password)

        if db_name:
            return redirect(url_for('home', db_name=db_name))  # <--- Añade el parámetro 'db_name' al URL
        else:
            print("intento fallido alv")

    return render_template("login.html")



@app.route("/home")
def home(db_name):
    numeroClientes = numClientes(db_name)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
