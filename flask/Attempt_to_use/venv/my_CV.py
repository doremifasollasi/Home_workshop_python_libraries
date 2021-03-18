from flask import Flask

app = Flask(__name__) # створюємо екземпляр класу з параметром __name__


# @app.route('/') # декорую функцію, щоб виводити інформацію на веб-сторінку
# def hello_world():
#     return 'Hello, my dear friend!'

# cd ..
# $ set FLASK_APP=my_CV.py
# або
# set FLASK_ENV=development  тоді буде lazy loading, а також Debugger is active!
# $ flask run
#  * Running on http://127.0.0.1:5000/

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'
