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

# Use the route() decorator to bind a function to a URL.

# @app.route('/')
# def index():
#     return 'Index Page'

# @app.route('/hello')
# def hello():
#     return 'Hello, World'

# Add variable sections to a URL by marking sections with <variable_name>.

@app.route('/user/<username>') # <динамічна змінна>
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)

