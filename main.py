# Acesso ao sistema de consulta e cadastro
# Importação das funcionalidades do arquivo "crud.py"
import crud

# fucncionalidade - Menu
def menu ():
    print('--------- SISTEMA CRUD ----------')
    print('1) Consultar cadastros')
    print('2) Inserir novo cadastro')
    print('3) Atualizar cadastro')
    print('4) Excluir cadastro')
    print('5) Sair')    
    print('--------------------------------\n')
        
    conf = 's'
    while conf == 's':
        op = int(input('Informe a opção desejada: '))
        if op > 0 and op < 6:
            if op == 1:
                crud.conferir()
            elif op == 2:
                crud.inserir()    
            elif op == 3:     
                crud.atualizar()
            elif op == 4:
                crud.excluir()
            elif op == 5:
                print('Sessão encerrada')
                break
            else:     
                op = int(input('Opção Inválida!, informe a opção correta'))
        conf = input('\nNova consulta? s - Sim / n - Não: ')
    print(' >>> Sessão encerrada <<<')                       
        
menu()    