import mysql.connector
from mysql.connector import Error
from user import User
from flask.globals import request
import UsuarioDAO




def buscar_dados():
    api_url = UsuarioDAO.listAllUsers
    print(api_url)
    

if __name__ == '__main__':
    buscar_dados()

"""
try:

    con = mysql.connector.connect(host='localhost', database='easylub', user='root', password='')

    consulta_sql = "SELECT * FROM usuario"
    cursor = con.cursor()
    cursor.execute(consulta_sql)
    linhas = cursor.fetchall()
    retorno = []
    print("Números Total de Registros Encontrados: ", cursor.rowcount)

    print("\nMostrando Dados")
   # for linha in linhas:
    #    print("Id: ", linha[0])
    #    print("Nome: ", linha[1])
    #    print("Sobre Nome: ", linha[2])
    #    print("Email: ",linha[3])
    #    print("Senha: ", linha[4],"\n")
           
    for us in linhas:
        user = User(us[0], us[1], us[2], us[3], us[4])
        retorno.append(user)        
        print("Id: ", us[0])
        print("Nome: ", us[1])
        print("Sobre Nome: ", us[2])
        print("Email: ",us[3])
        print("Senha: ", us[4],"\n")
    
except Error as e:
    print("Erro Ao Tentar Acessar o Banco de Dados")

finally:
    if(con.is_connected()):
        con.close()
        cursor.close()
        print("Conexão ao MySql Encerrada!")
        """