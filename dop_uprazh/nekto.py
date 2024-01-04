from flask import Flask

app = Flask(__name__)


@app.route('/file/<path:file>/')
def set_path(file):
    print(type(file))
    return f'Путь к файлу "{file}"'


@app.route('/')
def hello():
    return 'Привет незнакомец! Как тебя зовут?' 


# @app.route('/file/<path:file>/')
# def set_path(file):
#     print(type(file))
#     return f'Путь до файла "{file}"'



# @app.route('/')
@app.route('/<name>/')
def pot(name='ghjjjjjj'):
    # return 'Привет, '+ name +' !'
    return f"Привествую вас! {name}"

if (__name__) == "__main__":
    app.run()