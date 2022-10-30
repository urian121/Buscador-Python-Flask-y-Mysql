
#Importando Libreria mysql.connector para conectar Python con MySQL
import mysql.connector

def connectionBD():
    mydb = mysql.connector.connect(
        host ="localhost",
        user ="root",
        passwd ="",
        database = "ejemplo_youtube"
        )
    return mydb
    '''       
    if mydb:
        print ("Conexion exitosa")
    else:
        print ("Error en la conexion a BD")
    '''