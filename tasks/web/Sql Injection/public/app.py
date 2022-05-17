# imports
import os
import sqlite3

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
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
