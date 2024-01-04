from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Главная страница"

@app.route("/about/")
def about():
    return "about страница"

@app.route('/contact/')
def contact():
    return "contact страница"


@app.route('/павел/')
@app.route('/паша/')
@app.route('/павлик/')
def pavel():
    return "Привет Павел!"

if (__name__) == '__main__':
    app.run()
