import mysql.connector 

def conexionPrincipal():
    try:
        conn = mysql.connector.connect(
            host="200.234.224.17",
            port=3389,
            user="ciso",
            password="ciso",
            database="usuarios_wisp"
        )
        return conn
    
    except mysql.connector.Error as err:
        print(f"No podemos establecer la conexion {err}")


def inicioUsuario(username, password):
    try:
        search = conexionPrincipal()
        cursor = search.cursor()
        sql = "SELECT data FROM usuarios WHERE username = %s AND password = %s"
        valores = (username, password)
        cursor.execute(sql, valores)

        resultado = cursor.fetchone()

        cursor.close()
        search.close()

        return resultado
    except mysql.connector.Error as err:
        print(f"No podemos hacer la consulta {err}")
        return "Busqueda Fallida"
    

def servidorPrincipal(db_name):
    try:
        conexion = mysql.connector.connect(
            host="200.234.224.17",
            port=3389,
            user="ciso",
            password="ciso",
            database=db_name
        )
        return conexion
    except mysql.connector.Error as err:
        print(f"No podemos establecer conexion con usuario {err}")
        return None
    