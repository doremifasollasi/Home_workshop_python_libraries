# from flask import Flask
# # from markupsafe import escape
# # from flask import redirect
# from flask import render_template
# from flask import request

from flask import escape, url_for



###############################################
#          Import some packages               #
###############################################
from flask import Flask, render_template
from Forms.forms import ContactForm
from flask import request
import pandas as pd
###############################################
#          Define flask app                   #
###############################################
app = Flask(__name__)
app.secret_key = 'secretKey'
###############################################
#       Render Contact page                   #
###############################################

@app.route('/', methods=["GET","POST"])
def get_contact():
    form = ContactForm()
    # here, if the request type is a POST we get the data on contat
    #forms and save them else we return the contact forms html page
    if request.method == 'POST':
        name =  request.form["name"]
        email = request.form["email"]
        subject = request.form["subject"]
        message = request.form["message"]
        res = pd.DataFrame({'name':name, 'email':email, 'subject':subject ,'message':message}, index=[0])
        res.to_csv('./contactusMessage.csv')
        print("The data are saved !")
        return f"Thanks for your message. I will try to answer you as soon as possible."
    else:
        return render_template('hello.html', form=form)
###############################################
#                Run app                      #
###############################################
if __name__ == '__main__':
    app.run(debug=True)


######## login.html ###########################
# app = Flask(__name__) # створюємо екземпляр класу з параметром __name__

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
