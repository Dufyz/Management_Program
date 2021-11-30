#from A_menu_geral import menu_geral
from B_reg import  registrar_cliente
from B_save import db_cliente

def menu_clientes():
    
    print('\n', '-' * 50)   
    print('                 \n                   Menu Clientes')
    print('\n', '-' * 50)

    print('\n[1] Registrar Cliente',
        '\n[2] Banco de dados dos clientes',
        '\n[3] Editar banco de dados'
        '\n[4] Voltar')

    section = int(input('\nFaça sua escolha: '))

    if section == 1:
        registrar_cliente()
        return(menu_clientes())

    elif section == 2:
        db_cliente()
        return(menu_clientes())

    elif section == 3:
        pass

    elif section == 4:
        pass

    else:
        print('Parece que você não escolheu nenhuma opção válida')
