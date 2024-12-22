from server import servidorPrincipal

def consultarPaquetes(db_name):
    try:
        consulta = servidorPrincipal(db_name)
        cursor = consulta.cursor()
        cursor.execute("SELECT  nombre, velocidad, precio FROM paquetes")
        resultado = cursor.fetchall()

        cursor.close()
        consulta.close()

        return resultado  # Lista de tuplas con los datos
    except Exception as e:
        print(f"Error: {e}")
        return "Fallo"
