# Instalação da biblioteca - mysql-conector-python, que irá permitir a conexão com um banco de dados MYSQL
# instalação da biblioteca - dotenv, que irá armazenar as variáveis de ambiente

# Importação da biblioteca mysql.connector
# importação da classe Error, 
# importação de os (sistema operacional para resgatar as variáveis de ambiente)
# Importação da função - load_dotenv para carregar utilização das variáveis de ambiente

import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

# Dados do banco de dados: 
'''Banco de dados: dbcrud
   tabela: cargos
   campos: id, nome, cargo, salario 
'''

load_dotenv()
# função de conexão
def conexao ():
    
    try:
        co = mysql.connector.connect(
            user = os.getenv("CRUDUSER"),
            database = os.getenv("CRUDBD"),
            password= os.getenv("CRUDPASS")
        )
        return co
    except Error as e:
        print(f'Erro na conexão: {e}')
        return None


