# imports
import os
import sqlite3

from flask import Flask, render_template, request

app = Flask(__name__)

app.config.update(DATABASE=os.path.join(os.path.dirname(__file__), 'sgl_db.db'), DEBUG=False,
                  SECRET_KEY='secretkey0007',
                  USERNAME='admin', PASSWORD='admin')


# cnx = sqlite3.connect(app.config['DATABASE'])
#
# cursor = cnx.cursor()
#
# cursor.execute('''
# CREATE TABLE users (
#     id int,
#     login varchar(255),
#     password varchar(255)
# );
# ''')
#
# cnx.commit()
#
#
# def add_user(id, status_text, published):
#     query = "insert into users (id,login,password) values({0},'{1}','{2}');".format(id, status_text, published)
#     cursor.execute(query)
#
#     cnx.commit()
#
#
# add_user(1, "Test", "5267")
# add_user(1535255, "Ivan", "1234")
# add_user(2256252, "Petr", "qwerty")
# add_user(3525364, "Vova", "vrnctf{sql_beg1nner_att4cker}")
# cursor.close()
# cnx.close()


@app.route('/')
def index():
    # cnx = sqlite3.connect(app.config['DATABASE'])
    # cursor = cnx.cursor()
    # cursor.execute("select * from users")
    # data = cursor.fetchall()
    # cursor.close()
    data = []
    return render_template('index.html', data=data)


@app.route('/find', methods=['POST'])
def find():
    data = []
    if request.method == 'POST':
        con = sqlite3.connect(app.config['DATABASE'])
        cursor = con.cursor()
        id = request.form['id']
        if id != '':
            try:
                cursor.execute("select * from users where id = " + id)
                data = cursor.fetchall()
                cursor.close()
                con.close()
            except:
                pass
    return render_template('index.html', data=data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3030, debug=False)
