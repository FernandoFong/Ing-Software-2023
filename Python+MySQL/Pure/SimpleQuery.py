import pymysql

conexion = pymysql.connect(host = 'localhost',
                           user = 'ferfong',
                           password='Developer123!',
                           database='prueba',
                           cursorclass=pymysql.cursors.DictCursor)

#SELECT * from usuarios where nombre = 'Fernando';?

with conexion:
    with conexion.cursor() as cursor:
        insert_sql = "INSERT INTO usuarios values (%s, %s);"
        nombre = "Jorge"
        correo = "hola@ciencias.unam.mx"
        cursor.execute(insert_sql, (correo, nombre))
        sql = "SELECT * FROM usuarios WHERE nombre = %s;"
        nombre = "Fernando"
        cursor.execute(sql, (nombre))
        respuesta = cursor.fetchall()
        print(respuesta)
