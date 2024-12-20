from mysql.connector import connect, Error

def conexion():
    try:
        conn = connect(
            host="localhost",
            user="dni",
            password="MinuzaFea265/",
            database="userDenisse"
        )
        return conn
    
    except Error as err:
        print(f"No podemos conectar al sercidor {err}")

def loginUsername(username, password):
    try:
        motor = conexion()
        cursor = motor.cursor()
        sql = """
        SELECT data FROM usuarios WHERE username = %s AND password = %s
        """
        valores = (username, password)
        cursor.execute(sql, valores)
        resultado = cursor.fetchone()  # Obtiene solo el primer resultado, no toda la lista
        
        cursor.close()
        motor.close()

        # Retorna el valor de 'database' si existe, de lo contrario, None
        if resultado:
            return resultado[0]
        else:
            return None
    except Error as err:
        print(f"Error durante la consulta: {err}")
        return None
