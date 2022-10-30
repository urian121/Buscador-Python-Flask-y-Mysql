#Importando  flask y algunos paquetes
from flask import Flask, render_template, request, redirect, url_for
import time
from confiDB import *  #Importando conexion BD


#Declarando nombre de la aplicación e inicializando, crear la aplicación Flask
app = Flask(__name__)
application = app

app.secret_key = '97110c78ae51a45afcb3380af008f90b23a5d1616bf19bc29098105da20fe'



#Creando mi Decorador para el Home
@app.route('/', methods=['GET','POST'])
def inicio():
    return render_template('public/index.html')
      
      
#Buscar empleado
@app.route('/buscar-empleado', methods=['GET','POST'])
def BuscarEmpleado():
    if request.method    == "POST":
        search           = request.form['buscar']
        conexion_MySQLdb = connectionBD() #creando mi instancia a la conexion de BD
        cur      = conexion_MySQLdb.cursor(dictionary=True)
        querySQL = cur.execute("SELECT * FROM trabajadores WHERE nombre='%s' ORDER BY id  DESC" % (search,))
        resultadoBusqueda = cur.fetchone()  
        cur.close() #Cerrando conexion SQL
        conexion_MySQLdb.close() #cerrando conexion de la BD
        time.sleep(0.5) #tiempo de espera
        return render_template('public/resultadoBusqueda.html', miData = resultadoBusqueda, busqueda = search)
    return redirect(url_for('inicio'))  
   

#Redireccionando cuando la página no existe
@app.errorhandler(404)
def not_found(error):
        return redirect(url_for('inicio'))
    
    

if __name__ == "__main__":
    app.run(debug=True, port=8000)

