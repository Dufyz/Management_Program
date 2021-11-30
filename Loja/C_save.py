import time
import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '',
    port = 3306,
    database = 'incount'
)

cursor = db.cursor()

def db_funcionario():

    comando_mysql = f'SELECT *FROM funcionario'
    cursor.execute(comando_mysql)

    dbfuncionario = cursor.fetchall()

    print(f'\nFUNCIONÁRIOS REGISTRADOS: ')
    
    time.sleep(1)

    for c in dbfuncionario:
        print(f'\nID: {c[0]}',
              f'\nNome: {c[1]}',
              f'\nDocumento: {c[2]}',
              f'\nData de nascimento: {c[3]}',
              f'\nSalário: R${c[4]}\n')
    
    time.sleep(1)

    pass