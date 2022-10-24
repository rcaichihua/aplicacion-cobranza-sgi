from logging import exception
from psycopg2 import connect

connection = connect(
    user='postgres',
    password='1234',
    host='127.0.0.1',
    port=5432,
    database='ecommerce'
)

cursor = connection.cursor()
try:
    cursor.execute("insert into roles values(4,'prueba',true);")
    connection.commit()
except Exception as e:
    connection.rollback()
    print(f'An error occurred -> {e}')

# print(cursor.fetchall())

cursor.close()
connection.close()
