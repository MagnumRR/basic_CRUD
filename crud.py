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
        print('Conexão estabeleecida')
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
        
        
    
    