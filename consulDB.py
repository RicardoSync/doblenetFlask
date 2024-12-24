from server import servidorPrincipal

def consultarPaquetes(db_name):
    try:
        consulta = servidorPrincipal(db_name)
        cursor = consulta.cursor()
        cursor.execute("SELECT id, nombre, velocidad, precio FROM paquetes")
        resultado = cursor.fetchall()

        cursor.close()
        consulta.close()

        return resultado  # Lista de tuplas con los datos
    except Exception as e:
        print(f"Error: {e}")
        return "Fallo"

def numeroPaquetes(db_name):
    try:
        contador = servidorPrincipal(db_name)
        cursor = contador.cursor()
        cursor.execute("SELECT COUNT(*) FROM paquetes")
        resultado = cursor.fetchone()
        cursor.close()
        contador.close()
        return resultado
    
    except Exception as e:
        print(f"Error al contar los paquetes home.html {e}")
        return "Fallo Consulta"
    

def consultarEquipos(db_name):
    try:
        consulta = servidorPrincipal(db_name)
        cursor = consulta.cursor()
        cursor.execute("SELECT id, nombre, modelo, descripcion FROM equipos")
        resultado = cursor.fetchall()
        cursor.close()
        consulta.close()
        return resultado
    
    except Exception as err:
        print(f"Error al condultar equipos {err}")
        return "Fallo"