import mysql.connector
import time

db = mysql.connector.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    passwd = '',
    database = 'incount'
    )

cursor = db.cursor()

def db_cliente():
    
    comando_mysql = f'SELECT *from clientes'
    cursor.execute(comando_mysql)
    dbcliente = cursor.fetchall()

    print(f'\nCLIENTES REGISTRADOS: ')

    time.sleep(1)

    for c in dbcliente:
        print(f'\nID: {c[0]}')
        print(f'Nome: {c[1]}')
        print(f'Documento: {c[2]}')
        print(f'Data de nascimento: {c[3]}')
        print(f'Total de compras: {c[4]}') 
    pass
