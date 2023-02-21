import pymysql

conexion = pymysql.connect(host = 'localhost',
                           user = 'ferfong',
                           password='Developer123!',
                           database='prueba',
                           cursorclass=pymysql.cursors.DictCursor)

#SELECT * from usuarios where nombre = 'Fernando';

with conexion:
    with conexion.cursor() as cursor:
        sql = "SELECT * FROM usuarios WHERE nombre = %s;"
        nombre = "Fernando"
        cursor.execute(sql, (nombre))
        respuesta = cursor.fetchall()
        print(respuesta)