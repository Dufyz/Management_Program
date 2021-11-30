from C_reg import  registrar_funcionario
from C_save import db_funcionario

def menu_funcionarios():
    
    print('\n', '-' * 50)   
    print('                 \n                  Menu Funcionários')
    print('\n', '-' * 50)

    print('\n[1] Registrar Funcionáro',
        '\n[2] Banco de dados dos funcionários',
        '\n[3] Editar banco de dados'
        '\n[4] Voltar')

    section = int(input('\nFaça sua escolha: ')) 

    if section == 1:
        registrar_funcionario()
        return(menu_funcionarios())

    elif section == 2:
        db_funcionario()
        return(menu_funcionarios())

    elif section == 3:
        pass

    elif section == 4:
        pass

    else:
        print('Parece que você não escolheu nenhuma opção válida')
