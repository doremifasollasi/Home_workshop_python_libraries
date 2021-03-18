from flask import Flask

app = Flask(__name__) # створюємо екземпляр класу з параметром __name__


@app.route('/') # декорую функцію, щоб виводити інформацію на веб-сторінку
def hello_world():
    return 'Hello, World!'
