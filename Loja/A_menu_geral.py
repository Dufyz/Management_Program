import time

from B_menu01 import menu_clientes
from C_menu03 import menu_funcionarios
from D_menu02 import menu_estoque

def menu_geral():

    print('\n', '-' * 50)   
    print('                 \n                   Menu Geral')
    print('\n', '-' * 50)

    print('\n[1] Clientes',
        '\n[2] Funcionários'
        '\n[3] Estoque'
        '\n[4] SAIR')

    section = int(input('\nFaça sua escolha: '))

    if section == 1:
        menu_clientes()
        return(menu_geral())

    elif section == 2:
        menu_funcionarios()
        return(menu_geral())

    elif section == 3:
        menu_estoque()
        return(menu_geral())

    elif section == 4:
        pass

    else:
        print('\nParece que você não escolheu nenhuma opção válida')
        menu_geral()

    time.sleep(1)
    print('\nFechando programa \n')
    time.sleep(1)

menu_geral()