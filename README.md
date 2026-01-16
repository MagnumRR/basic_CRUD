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

# Funcionalidade - Leitura da tabela (Conferir)

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
		if len(cargos) > 0: **Se o tamanho dos elementos da tabela cargos for maior que zero retorna os dados da tabela
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

## Funcionalidade - Inserção de dados (Inserir)
	**Funcionalidade - inserindo dados
	def inserir():
		co = conexao()
		
		if co is not None:
			print('- Conexão estabelecida -')
			cursor = co.cursor()
		else:
			print('Sem conexão com o banco!')        
		
		**Solicitando ao usuário que informe os dados serem adicionados
		nome = input('Informe o nome: ')
		cargo = input('Informe o cargo: ')
		salario = float(input('Informe o salario: '))
		
		**Parâmetros da inserção
    	query = "INSERT INTO cargos (nome, cargo, salario) VALUES (%s, %s, %s)"
    	cursor.execute(query, (nome, cargo, salario))
    	**Salvando os dados na tabela
    	co.commit()
		
		**Realiza-se uma conferência, onde houver pelo menos uma linha armazenada no banco retorna-se uma mensagem de confirmação.
		if cursor.rowcount == 1:
			print(f'O funcionário: {nome} foi gravado com sucesso')
		else:
			print('Funcionário não cadastrado!')
			co.close()

# Funcionalidade - Atualização de dados (atualizar)
	**Funcionalidade - Atualizando dados
	def atualizar():
		co = conexao()
		
		if co is not None:
			print('- Conexão estabelecida -')
			cursor = co.cursor()
		else:
			print('Sem conexão com o banco!')
		
		**Entrada de dados pelo usuário a serem atualizados
		cod = int(input('Id do funcionário: '))
		nome = input('Nome do funcionário: ')
		cargo = input('Cargo do funcionário: ')
		salario = float(input('Salário do funcionário: '))
		
		query = "UPDATE cargos SET nome=%s, cargo=%s, salario=%s WHERE id=%s"
    	cursor.execute(query, (nome, cargo, salario, cod))
   		**Dados gravados
		co.commit()
		
		**Se pelo menos uma linha de dados foi gravada é retornado uma mensagem de confirmação
		if cursor.rowcount == 1:
			print(f'Os dados do funcionário: {nome} foram atualizados!')
		else:
			print('Falha ao atualizar os dados')
			co.close()

## Funcionalidade - Exclusão de dados
	**Função EXCLUIR dados da tabela
	def excluir():
		co = conexao()
		
		if co is not None:
			print('- Conexão estabelecida -')
			cursor = co.cursor()
		else:
			print('Sem conexão com o banco!')
		
		cod = int(input('Informe o id do funcionário: '))
		
		**Parâmetros de consulta ao MySQL:
		query = "SELECT nome FROM cargos WHERE id=%s"
		cursor.execute(query, (cod,))
		res = cursor.fetchone()
		
		if res is not None:
			print(f'Funcionário designado: {res[0]}') **Consulta com base no id (item [0] da tabela)
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