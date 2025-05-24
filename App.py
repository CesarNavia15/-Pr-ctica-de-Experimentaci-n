from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "formulario_usuario"
mysql = MySQL(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    # Obtener datos del formulario
    fullname = request.form.get('name')
    age = request.form.get('age')
    cur= mysql.connection.cursor()
    cur.execute('INSERT INTO usuario (fullname, age) VALUES (%s, %s)',
                (fullname, age))
    mysql.connection.commit()
    return 'received'


if __name__ == '__main__':
    app.run(debug=True)