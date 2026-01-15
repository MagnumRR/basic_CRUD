# basic_CRUD
Demonstração de CRUD simples utilizando linguagem python

## Estrutura do projeto:
	├── main.py - Arquivo principal para acesso ao menu do sistema
	├── crud.py - Estrutura das funcionalidades CRUD
	├── db.py - Funcionalidade para conexão com banco de dados
	├── .gitignore - Com dados de variáveis de ambiente
	├──	README.md
	└── requirements.txt

## Estrutura do arquivo db.py
	Para este projeto foi designado uma conexão com um banco de Dados MySQL. Para instalação de algumas bibliotecas foi criado um ambiente virtual, chamado "venv".
	Comandos para instalação das bibliotecas:
		* pip install mysql-conector-python
		* pip install dotenv

	* Instalação da biblioteca - mysql-conector-python, que irá permitir a conexão com um banco de dados MYSQL
	* instalação da biblioteca - dotenv, que irá armazenar as variáveis de ambiente

	Para utilização dessas bibliotecas foram realizadas as seguintes importações:
		* Importação da biblioteca mysql.connector
		* importação da classe Error, 
		* importação de os (sistema operacional para acessar as variáveis de ambiente do sistema local)
		* Importação da função - load_dotenv para carregar utilização das variáveis de ambiente

	* import mysql.connector
	* from mysql.connector import Error
	* import os
	* from dotenv import load_dotenv

	Utilização da função "load_dotenv()" para reconhecimento das variáveis de ambiente no projeto
	load_dotenv()
	
	* Cria-se a função de conexão
	def conexao ():
		
		try:
			co = mysql.connector.connect(
				user = os.getenv("CRUDUSER"),
				database = os.getenv("CRUDBD"),
				password= os.getenv("CRUDPASS")
			)
			return co, print('Conexão estabelecida com sucesso!')
		except Error as e:
			print(f'Erro na conexão: {e}')
			return None

## Bibliotecas utilizadas - Requirements.txt
	Aqui se encontram as bibliotecas utilizadas neste projeto:
	 * dotenv==0.9.9
	 * mysql-conector-python==0.1.8
	 * python-dotenv==1.2.1

## Estrutura do arquivo crud.py
	Este arquivo conterá todas as funcionalidades essenciais que O CRUD realiza: (CREATE - CRIAR / READ - LEITURA / UPDATE - ATUALIZAR / DELETE - EXCLUIR)

## Leitura do banco de dados - Função Conferir
	from db import conexao
import db
import mysql.connector
# Para cada funcionalidade será criada uma função

	def conferir(): 
		**Acesso ao banco de dados:
		co = conexao()
		**Para o manuseio do banco de dados faz-se necessário o uso do "cursor"
		if co is not None:
			print('Conexão estabeleecida')
			cursor = co.cursor()
		else:
			print('Sem conexão com o banco!')
		**Através do cursor realiza-se a operação de leitura dos dados contidos no banco
		cursor.execute('SELECT * FROM cargos')
		cargos = cursor.fetchall()  # O cursor devolve ao atributo cargos na forma de tabela

		** Realizar-se um loop, com a condição: se houver algo na tabela, ela então exibe os dados, caso contrário retorna uma mensagem
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
