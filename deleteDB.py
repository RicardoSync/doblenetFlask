from server import servidorPrincipal


def eliminarPaquete(id, db_name):
    try:
        conexion = servidorPrincipal(db_name)
        cursor = conexion.cursor()
        query = "DELETE FROM paquetes WHERE id = %s"
        cursor.execute(query, (id,))
        conexion.commit()
        cursor.close()
        conexion.close()
        return "Exito"
    except Exception as e:
        print(f"Error al eliminar el paquete: {e}")
        return "Error"