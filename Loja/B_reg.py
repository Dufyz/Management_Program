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

def registrar_cliente():
    
    class cliente():
        __nome = str(input(f'\nNome completo do cliente: '))
        __documento = str(input('Documento: '))
        __nascimento = str(input('Data de nascimento: '))
        __compras = int(input('Total de compras: '))

        comando_mysql = f'INSERT INTO clientes (nome, documento, nascimento, compras) VALUES (%s, %s, %s, %s)'
        info = (str(__nome), str(__documento), str(__nascimento), str(__compras))

        cursor.execute(comando_mysql, info)
        db.commit()

        time.sleep(1)

        print(f'\n Cliente registrado com sucesso'),
        print(f'\nID: gerado automaticamente',
              f'\nNome: {__nome}',
              f'\nDocumento: {__documento}',
              f'\nData de nascimento: {__nascimento}',
              f'\nCompras: {__compras}')
        
        pass