import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '',
    port = 3306,
    database = 'incount'
)

cursor = db.cursor()

def registrar_funcionario():
    
    class funcionario():
        __nome = input(f'\nNome completo do funcionário: ')
        __documento = input('Documento do funcionário: ')
        __nascimento = input('Data de nascimento: ')
        __salario = input('Salário do funcionário: ')

        comando_mysql = f'INSERT INTO funcionario (nome, documento, nascimento, salario) VALUES (%s, %s, %s, %s)'
        info = (__nome, __documento, __nascimento, __salario)

        cursor.execute(comando_mysql, info)
        db.commit()

        print(f'\nFuncionário registrado com sucesso')
        print(f'\nID: gerado automáticamente',
              f'\nNome: {__nome}',
              f'\nDocumento: {__documento}',
              f'\nData de nascimento: {__nascimento}'
              f'\nSalário: R${__salario}\n')
        pass