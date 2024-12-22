from server import servidorPrincipal

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

    except mysql.connector.Error as err:
        print(f"No podemos almacenar los paquetes {err}")
        return None
    