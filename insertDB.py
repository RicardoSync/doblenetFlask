from server import servidorPrincipal
from consulDB import buscarPaquete

def insertarPaquete(nombre, velocidad, precio, db_name):
    try:
        inserar = servidorPrincipal(db_name)
        cursor = inserar.cursor()
        sql = "INSERT INTO paquetes (nombre, velocidad, precio) VALUES (%s,%s,%s)"
        valores = (nombre, velocidad, precio)
        cursor.execute(sql, valores)
        inserar.commit()
        cursor.close()
        inserar.close()

        return "Exito"

    except Exception as err:
        print(f"No podemos almacenar los paquetes {err}")
        return "Error"    
    

def insertarEquipo(nombre, modelo, descripcion, db_name):
    try:
        insertar = servidorPrincipal(db_name)
        cursor = insertar.cursor()
        sql = "INSERT INTO equipos (nombre, modelo, descripcion) VALUES (%s,%s,%s)"
        valores = (nombre, modelo, descripcion)
        cursor.execute(sql, valores)

        insertar.commit()
        cursor.close()
        insertar.close()

        return "Exito"
    
    except Exception as err:
        print(f"Tenemos error {err}")
        return "Fallo"
    

def insertarCliente(nombre, domicilio, telefono, plan, equipo, db_name):
    #mensualidad la obtenemos el paquete
    #fecha de instalacion automatica, proximo pago es el numero +31
    #estado por defecto es activo
    print(f"hola {nombre, domicilio, telefono, plan, equipo, db_name}")
    mensualidad = buscarPaquete(db_name=db_name, nombrePaquete=plan)
    print(f"{mensualidad[0]}")
