from flask import Flask
# from markupsafe import escape
# from flask import redirect
from flask import render_template
from flask import request

from flask import Flask, escape, url_for

app = Flask(__name__) # створюємо екземпляр класу з параметром __name__


# @app.route('/') # декорую функцію, щоб виводити інформацію на веб-сторінку
# def hello_world():
#     return 'Hello, my dear friend!'

# cd Scripts 
# activate
# pip list
# cd ..
# set FLASK_APP=my_CV.py
# або
# set FLASK_ENV=development  тоді буде lazy loading, а також Debugger is active!
# $ flask run
#  * Running on http://127.0.0.1:5000/

# Use the route() decorator to bind a function to a URL.

# @app.route('/')
# def index():
#     return 'Index Page'

# @app.route('/hello')
# def hello():
#     return 'Hello, World'

# Add variable sections to a URL by marking sections with <variable_name>.

# @app.route('/user/<username>') # <динамічна змінна>
# def show_user_profile(username):
#     # show the user profile for that user
#     return 'User %s' % escape(username)  # from markupsafe import escape

# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     # show the post with the given id, the id is an integer
#     return 'Post %d' % post_id

# @app.route('/path/<path:subpath>')
# def show_subpath(subpath):
#     # show the subpath after /path/
#     return 'Subpath %s' % escape(subpath)

# To redirect a user to another endpoint, use the redirect() function

# @app.route("/admin")
# def hello_admin():
#     return "Hello, Admin!!!"

# @app.route("/guest/<guest>")
# def hello_guest(guest): 
#     return f"Hello {guest} as Guest"

# @app.route("/user/<name>")
# def hello_user(name): 
#     if name=="admin":
#         return redirect(url_for("hello_admin"))  # from flask import redirect
#     else:
#         return redirect(url_for("hello_guest", guest=name))

# if __name__ == '__main__': # для автоматичного дебагінгу
#     app.run(debug=True)


# Rendering Templates

# @app.route('/hello/')
# @app.route('/hello/<name>')
# def hello(name=None):
#     return render_template('hello.html', name=name) # from flask import render_template


########################### login.html ###########################

def valid_login(name,password):
    return name==password

def log_the_user_in(name):
    return f"Hello, {name}! You are lucky."



@app.route('/')
def hello():
    return render_template('hello.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)
