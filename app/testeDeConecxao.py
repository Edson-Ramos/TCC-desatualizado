import mysql.connector
from mysql.connector import Error
from user import User
from flask.globals import request
import UsuarioDAO
from equipamento import Equipamento






 
 
equip = Equipamento(10, "TesteMaquina", "TesteLinha", "TesteTrecho")
UsuarioDAO.insertEquipamentos(equip)