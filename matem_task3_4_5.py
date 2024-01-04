from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "С подсчётами страница"

@app.route('/sum/<int:num1>_<int:num2>/')
def set_math(num1, num2):
    return str(num1 + num2)


@app.route('/len/<name>/')
def set_len(name):    
    return f'Колличество введённых букв в строке {str(len(name))}'


text = """
    <h1>Привет, меня зовут Алексей</h1>
    <p>Уже много лет я создаю сайты на Flask.<br/>Посмотрите на мой сайт.</p>
    """   

@app.route('/html/')
def html():
    
    return text


if (__name__) == "__main__":
    app.run()