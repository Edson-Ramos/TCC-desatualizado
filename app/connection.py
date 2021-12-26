
import mysql.connector


try:
	connection = mysql.connector.connect(host='localhost', user='root', password='', database='easylub')
	cursor = connection.cursor()
except mysql.connector.Error as error:
	print("Erro ao Conectar Com o Banco de Dados")
	
def getConnection():	
	return (connection, cursor)	
	
def closeConnection():
	if connection.is_connected():
		cursor.close()
		connection.close()
	print("Conexao Encerrada!")



	