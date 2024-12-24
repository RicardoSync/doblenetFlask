from server import servidorPrincipal

def actualizarPaquete(id, nombre, velocidad, precio, db_name):
    try:
        conexion = servidorPrincipal(db_name)
        cursor = conexion.cursor()
        query = """
            UPDATE paquetes 
            SET nombre = %s, velocidad = %s, precio = %s 
            WHERE id = %s
        """
        cursor.execute(query, (nombre, velocidad, precio, id))
        conexion.commit()
        cursor.close()
        conexion.close()
        return "Exito"
    except Exception as e:
        print(f"Error al actualizar el paquete: {e}")
        return "Error"

def actualizarEquipos(id, nombre, modelo, descripcion, db_name):
    try:
        conexion = servidorPrincipal(db_name)
        cursor = conexion.cursor()
        query = """
            UPDATE equipos 
            SET nombre = %s, modelo = %s, descripcion = %s 
            WHERE id = %s
        """
        cursor.execute(query, (nombre, modelo, descripcion, id))
        conexion.commit()
        cursor.close()
        conexion.close()
        return "Exito"
    except Exception as e:
        print(f"Error al actualizar el paquete: {e}")
        return "Error"

