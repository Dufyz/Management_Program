import mysql.connector

db = mysql.connector.connect(

    host = 'localhost',
    user = 'root',
    passwd = '',
    port = 3306,
    database = 'incount'
)

cursor = db.cursor()

def registrar_estoque():
    
    class estoque():
        
        __nome = input(f'\nNome do produto: ')
        __marca = input('Marca do produto: ')
        __quantidade = input('Quantidade disponível do produto: ')
        __descricao = input('Descrição do produto: ')

        comando_mysql = f'INSERT INTO estoque (nome, marca, quantidade, descricao) VALUES (%s, %s, %s, %s)'
        info = (str(__nome), str(__marca), str(__quantidade), str(__descricao)) 
        cursor.execute(comando_mysql, info)
        db.commit()

        print('Produto registrado com sucesso')

        print(f'\nFuncionário registrado com sucesso')
        print(f'\nID: gerado automaticamente',
              f'\nNome: {__nome}',
              f'\nMarca: {__marca}',
              f'\nQuantidade: {__quantidade}',
              f'\nDescrição: {__descricao}',)
