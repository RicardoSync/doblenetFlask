from mysql.connector import connect, Error

def conexionServer(db_name):
    try:
        conexion = connect(
            host="localhost",
            port=3306,
            user="dni",
            password="MinuzaFea265/",
            database=db_name
        )
        return conexion
    
    except Error as err:
        print(f"No podemos establecer una conexion al servidor {err}")


def numClientes(db_name):
    try:
        motor = conexionServer(db_name)
        cursor = motor.cursor()
        cursor.execute("SELECT COUNT(*) FROM clientes")
        resultado = cursor.fetchone()
        cursor.close()
        motor.close()
        return resultado
    except:
        print("No podemos conectarnos")
        return "Error conexion"