# http://flask.pocoo.org/docs/1.0/quickstart/#a-minimal-application
# http://flask.pocoo.org/docs/1.0/installation/#installation

#pip install Flask
#Create file hello.py

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'



# set FLASK_APP=hello.py

# flask run

# Hello.py
