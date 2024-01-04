from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello незнакомец!'


@app.route('/studens/')
def stu_list():
    poople = [
        {'Имя': 'Иван', 'Фамилия':'Иванов' , 'Возраст': 20, 'Средний бал': 4.5},
        {'Имя': 'Пётр', 'Фамилия':'Петров' , 'Возраст': 21, 'Средний бал': 4.2},
        {'Имя': 'Сергей', 'Фамилия':'Сергеев' , 'Возраст': 19, 'Средний бал': 4.8},
        {'Имя': 'Анна', 'Фамилия':'Иванова' , 'Возраст': 20, 'Средний бал': 4.7},
    ]
    return render_template('studens.html',studens =poople)


if (__name__) == "__main__":
    app.run()