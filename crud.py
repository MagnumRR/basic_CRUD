# O arquivo CRUD contém todas as funcionalidades (CREATE - READ - UPDATE - DELETE)

# importar do arquivo "db.py" a função de conexão ao banco de dados.
from db import conexao
import db
import mysql.connector
# Para cada funcionalidade será criada uma função

def conferir():
    # Acesso ao banco de dados:
    co = conexao()
    # Para o manuseio do banco de dados faz-se necessário o uso do "cursor"
    if co is not None:
        print('Conexão estabelecida')
        cursor = co.cursor()
    else:
        print('Sem conexão com o banco!')
    # Através do cursor realiza-se a operação de leitura dos dados contidos no banco
    cursor.execute('SELECT * FROM cargos')
    cargos = cursor.fetchall()  # O cursor devolve ao atributo cargos na forma de tabela

    if len(cargos) > 0:
        for ca in cargos:
            print('-------Tabela Cargos ----------')
            print(f'Id: {ca[0]}')
            print(f'Nome: {ca[1]}')
            print(f'Cargo: {ca[2]}')
            print(f'Salário: {ca[3]}')
    else:
        print('Tabela vazia')        
        cursor.close()    
        co.close()    
        
# Funcionalidade - inserindo dados
def inserir():
    co = conexao()
    
    if co is not None:
        print('- Conexão estabelecida -')
        cursor = co.cursor()
    else:
        print('Sem conexão com o banco!')        
    
    # Solicitando ao usuário que informe os dados serem adicionados
    nome = input('Informe o nome: ')
    cargo = input('Informe o cargo: ')
    salario = float(input('Informe o salario: '))
    
    # Realizando a inserção 
    cursor.execute(f"INSERT INTO cargos (nome, cargo, salario) VALUES ('{nome}', '{cargo}', {salario})")
    # Salvando os dados na tabela
    co.commit()
    
    # Realiza-se uma conferência, onde houver pelo menos uma linha armazenada no banco retorna-se uma mensagem de confirmação.
    if cursor.rowcount == 1:
        print(f'O funcionário: {nome} foi gravado com sucesso')
    else:
        print('Funcionário não cadastrado!')
        co.close()


    
    
    
    
    
    