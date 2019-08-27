from flask import Flask,render_template,escape,request,jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///databases/estudiantes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)
app.secret_key='mysecretkey'

@app.route('/',methods= ['GET'])
def hello_world(): 
    return render_template('inicio.html')

@app.route('/users/list',methods= ['GET'])
def lista(): 
    datos=db.engine.execute('select * from estudiantes')
    return render_template('lista.html',estudents=datos)

@app.route('/api/v1/users/')
def lista2():
    resultado=db.engine.execute('select * from estudiantes')
    return jsonify({'listado':[dict(row)for row in resultado]})
 
if __name__ == "__main__":
    app.run(debug= True, host= '0.0.0.0', port=80)
