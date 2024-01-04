from flask import Flask
from flask import render_template
# from tabulete import tabulete
# import pandas as ps

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello незнакомец!'


@app.route('/table/')
def get_table():
     poople = [
        {'Имя': 'Иван', 'Фамилия':'Иванов' , 'Возраст': 20, 'Средний балл': 4.5},
        {'Имя': 'Пётр', 'Фамилия':'Петров' , 'Возраст': 21, 'Средний балл': 4.2},
        {'Имя': 'Сергей', 'Фамилия':'Сергеев' , 'Возраст': 19, 'Средний балл': 4.8},
        {'Имя': 'Анна', 'Фамилия':'Иванова' , 'Возраст': 20, 'Средний балл': 4.7},
     ]
    


if (__name__) == "__main__":
    app.run()