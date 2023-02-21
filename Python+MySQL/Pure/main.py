import pymysql.cursors

connection = pymysql.connect(host='localhost',
                             user='ferfong',
                             password='Developer123!',
                             database='prueba',
                             cursorclass=pymysql.cursors.DictCursor)

with connection:
    with connection.cursor() as cursor:
        sql = "SELECT * from `usuarios`;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(type(result[0]))
        print(result)
