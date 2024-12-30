from flask import Flask, render_template, request, redirect, url_for, flash
from server import inicioUsuario
from insertDB import insertarPaquete, insertarEquipo, insertarCliente
from consulDB import consultarPaquetes, numeroPaquetes, consultarEquipos, consultaPaqueteLista
from deleteDB import eliminarPaquete, deleteEquipo
from updateDB import actualizarPaquete, actualizarEquipos
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
            return redirect(url_for('paquetes'))
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
@app.route('/equipos', methods=["POST", "GET"])    
def equipos():
    if request.method == "POST":
        nombreEquipo = request.form.get("nombreEquipo")
        modeloEquipo = request.form.get("modeloEquipo")
        descripcionEquipo = request.form.get("descripcionEquipo")
        data = db_name[0]

        insertarEquipo(nombre=nombreEquipo, modelo=modeloEquipo, descripcion=descripcionEquipo, db_name=data)

        if insertarEquipo == "Exito":
            return render_template('equipos')
        elif insertarEquipo == "Fallo":
            return render_template('errorGay.html', error_message="Tenemos un problema para almacenar el equipo, intenta nuevamente")
    
    data = db_name[0]
    consultar_Equipos = consultarEquipos(data)

    return render_template('equipos.html', variableEquipos=consultar_Equipos)


@app.route('//eliminarEquipo<int:id>', methods=["POST", "GET"])

def eliminarEquipo(id):
    data = db_name[0]
    comando_eliminar = deleteEquipo(id=id, db_name=data)

    if comando_eliminar == "Exito":
        return redirect(url_for('equipos'))
    else:
        print("No podemos eliminar el equipo, tenemos un problema")
        return render_template('errorGay.html', error_message="Tenemos un problema al querer eliminar el equipo, cierra sesion y reintenta")


# Cargar el formulario con los datos del paquete
@app.route('/editar_equipo/<int:id>', methods=["GET"])
def editar_equipo(id):
    data = db_name[0]
    conexion = servidorPrincipal(data)
    cursor = conexion.cursor()
    query = "SELECT * FROM equipos WHERE id = %s"
    cursor.execute(query, (id,))
    equipos = cursor.fetchone()
    cursor.close()
    conexion.close()

    if len(equipos)>0:
        #return f"Id del equipo {equipos[0]} con nombre {equipos[1]} con modelo {equipos[2]} y descripcion {equipos[3]}"
        return render_template('editar_equipos.html', equiposHTML=equipos)
    else:
        return render_template('errorGay.html', error_message="No podemos realizar la busqueda de ese equipo para poder actualizar. Error 203x001")

# Procesar los cambios en el paquete
@app.route('/actualizar_equipos/<int:id>', methods=["POST"])
def actualizar_equipos(id):
    nombreEquipo = request.form.get("nombre_equipo")
    modeloEquipo = request.form.get("modelo_equipo")
    descripcionEquipo = request.form.get("descripcion_equipo")

    data = db_name[0]
    comando_actualizar = actualizarEquipos(id=id, nombre=nombreEquipo, modelo=modeloEquipo, descripcion=descripcionEquipo, db_name=data)

    if comando_actualizar == "Exito":
        return redirect(url_for('equipos'))
    elif comando_actualizar == "Error":
        return render_template('errorGay.html', error_message="No podemos realizar la actualizacion, intenta mas tarde")
#--------------------------------------------------------FUNCIONES DE LOS EQUIPOS ----------------------------------------------#


#--------------------------------------------------------FUNCIONES DE LOS CLIENTES ----------------------------------------------#
@app.route('/clientes', methods=["GET", "POST"])
def clientes():
    if request.method == "POST":
        nombreCliente = request.form.get("nombre")
        domicilioCliente = request.form.get("domicilio")
        telefonoCliente = request.form.get("telefono")
        planCliente = request.form.get("plan")
        equipoCliente = request.form.get("equipo")
        data = db_name[0]
        insertarCliente(
            nombre=nombreCliente, 
            domicilio=domicilioCliente, 
            telefono=telefonoCliente, 
            plan=planCliente, 
            equipo=equipoCliente, 
            db_name=data
        )

    # Consultar paquetes y equipos desde la base de datos
    data = db_name[0]
    #paquetes = consultarPaquetes(db_name=data)  # Obtener paquetes
    paquetes = consultaPaqueteLista(db_name=data)
    equipos = consultarEquipos(data)  # Obtener equipos

    return render_template('clientes.html', paquetes=paquetes, equipos=equipos)

if __name__ == '__main__':
    app.run(debug=True)