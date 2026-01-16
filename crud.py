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

    if len(cargos) > 0: # Se o tamanho dos elementos da tabela cargos for maior que zero retorna os dados da tabela
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
    
    # Parâmetros da inserção
    query = "INSERT INTO cargos (nome, cargo, salario) VALUES (%s, %s, %s)"
    cursor.execute(query, (nome, cargo, salario))
    # Salvando os dados na tabela
    co.commit()
    
    # Realiza-se uma conferência, onde houver pelo menos uma linha armazenada no banco retorna-se uma mensagem de confirmação.
    if cursor.rowcount == 1:
        print(f'O funcionário: {nome} foi adicionado com sucesso')
    else:
        print('Funcionário não cadastrado!')
        co.close()


# Funcionalidade - Atualizando dados
def atualizar():
    co = conexao()
    
    if co is not None:
        print('- Conexão estabelecida -')
        cursor = co.cursor()
    else:
        print('Sem conexão com o banco!')
    
    cod = int(input('Id do funcionário: '))
    nome = input('Nome do funcionário: ')
    cargo = input('Cargo do funcionário: ')
    salario = float(input('Salário do funcionário: '))
    
    query = "UPDATE cargos SET nome=%s, cargo=%s, salario=%s WHERE id=%s"
    cursor.execute(query, (nome, cargo, salario, cod))
    co.commit()
    
    if cursor.rowcount == 1:
        print(f'Os dados do funcionário: {nome} foram atualizados!')
    else:
        print('Falha ao atualizar os dados')
        co.close()    

# Funcionalidade - Excluindo dados
def excluir():
    co = conexao()
    
    if co is not None:
        print('- Conexão estabelecida -')
        cursor = co.cursor()
    else:
        print('Sem conexão com o banco!')
    
    cod = int(input('Informe o id do funcionário: '))
    
    # Parâmetros de consulta ao MySQL:
    query = "SELECT nome FROM cargos WHERE id=%s"
    cursor.execute(query, (cod,))
    res = cursor.fetchone()
    
    if res is not None:
        print(f'Funcionário designado: {res[0]}') # Consulta com base no id (item [0] da tabela)
        conf = input('Deseja excluir este cadastro? (s - Sim / n -- não): ')
        if conf == 's':
            query2 = "DELETE FROM cargos WHERE id=%s"
            cursor.execute(query2, (cod,))
            co.commit()
            print('Exclusão realizada com sucesso')
        else:
            print('Exclusão cancelada!')        
    else:
        print('Funcionário inexistente')
    co.close()    
