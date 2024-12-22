from flask import Flask, render_template, request, redirect, url_for, flash
from server import inicioUsuario
from insertDB import insertarPaquete
from consulDB import consultarPaquetes, numeroPaquetes
from deleteDB import eliminarPaquete
from updateDB import actualizarPaquete
from server import servidorPrincipal

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
    contadorPaquetes = numeroPaquetes(db_name)
    if len(contadorPaquetes)>0:
        usuario = username
        numPkg = contadorPaquetes
        return render_template('home.html', user=usuario, db=db_name, numeroPaquetes=numPkg) #mandamos esas variables al html
    else:
        usuario = username
        numPkg = "N/A"
        return render_template('home.html', user=usuario, db=db_name, numeroPaquetes=numPkg) #mandamos esas variables al html


#--------------------------------------------------------FUNCIONES DE LOS PAQUETES ----------------------------------------------#
#aqui vamos a poner las opciones de los paquetes
@app.route('/paquetes', methods=["POST", "GET"])    
def paquetes():
    if request.method == "POST":
        nombrePaquete = request.form.get("nombre_paquete")
        velocidadPaquete = request.form.get("velocidad")
        precioPaquete = request.form.get("precio")
        data = db_name[0]
        almacenar = insertarPaquete(nombre=nombrePaquete, velocidad=velocidadPaquete, precio=precioPaquete, db_name=data)

        if almacenar == "Exito":
            return redirect(url_for('home'))
        else:
            return render_template('errorAlmacenamiento.html')
        
    data = db_name[0]
    paquetesAlmacenados = consultarPaquetes(db_name=data)
    return render_template('paquetes.html', database=data, pkg=paquetesAlmacenados)


# Eliminar paquete
@app.route('/eliminar_paquete/<int:id>', methods=["POST", "GET"])
def eliminar_paquete(id):
    data = db_name[0]
    resultado = eliminarPaquete(id=id, db_name=data)  # Llama a la función de eliminación en tu backend

    if resultado == "Exito":
        return redirect(url_for('paquetes'))
    else:
        print("Hubo un error al eliminar el paquete")
        return render_template('error.html')

# Cargar el formulario con los datos del paquete
@app.route('/editar_paquete/<int:id>', methods=["GET"])
def editar_paquete(id):
    data = db_name[0]
    conexion = servidorPrincipal(data)
    cursor = conexion.cursor()
    query = "SELECT * FROM paquetes WHERE id = %s"
    cursor.execute(query, (id,))
    paquete = cursor.fetchone()
    cursor.close()
    conexion.close()

    if paquete:
        return render_template('editar_paquete.html', paquete=paquete)
    else:
        return render_template('error.html')

# Procesar los cambios en el paquete
@app.route('/actualizar_paquete/<int:id>', methods=["POST"])
def actualizar_paquete(id):
    nombre = request.form.get("nombre_paquete")
    velocidad = request.form.get("velocidad")
    precio = request.form.get("precio")
    data = db_name[0]

    resultado = actualizarPaquete(id=id, nombre=nombre, velocidad=velocidad, precio=precio, db_name=data)

    if resultado == "Exito":
        return redirect(url_for('paquetes'))
    else:
        print("Hubo un error al actualizar el paquete")
        return render_template('error.html')
#--------------------------------------------------------FUNCIONES DE LOS PAQUETES ----------------------------------------------#


#--------------------------------------------------------FUNCIONES DE LOS EQUIPOS ----------------------------------------------#

#--------------------------------------------------------FUNCIONES DE LOS EQUIPOS ----------------------------------------------#


if __name__ == '__main__':
    app.run(debug=True)