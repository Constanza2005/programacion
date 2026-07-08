import mysql.connector

def conectar_db():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="rifa_t"
        )
        
        if conexion.is_connected():
            return conexion

    except mysql.connector.Error as err:
        print(f"Error: {err}")

def guardar_datos(consulta,datos):
    conexion = conectar_db()
    if conexion:
        cursor = conexion.cursor()
        if cursor:
            cursor.execute(consulta,datos)
            conexion.commit()
            id_insercion = cursor.lastrowid
            print(f'Se ha insertado el registro N°: {id_insercion}')
            cursor.close()
            conexion.close()