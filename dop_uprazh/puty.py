from flask import Flask

app = Flask(__name__)

@app.route('/file/<path:file>/')
def set_path(file):
    print(type(file))
    return f'Путь к файлу "{file}"'

# @app.route('/file/<path:file>/')
# def set_path(file):
#     print(type(file))
#     return f'Путь до файла "{file}"'


if (__name__) == "__main__":
    app.run()