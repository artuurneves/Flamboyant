from flask import render_template, request, session, flash, abort, redirect, url_for
from app import app
# from mymap.database.core_insert import insertUser as insertUser
# from mymap.database.core_select import selectUser as selectUser
# from mymap.database.core_select import getPassword as getPassword

@app.route('/')
@app.route('/home')
def homepage():
    return render_template('homepage.html', title='Homepage')

@app.route('/cadcond')
def cadcond():
    return render_template('cadastro-condominos.html', title='IMAP Portal')

# @app.route('/charts')
# def charts():
#     return render_template('charts.html', title='Charts')
#
# @app.route('/widgets')
# def widgets():
#     return render_template('widgets.html', title='Widgets')
#
# @app.route('/tables')
# def tables():
#     return render_template('tables.html', title='Tables')
#
# @app.route('/grid')
# def grid():
#     return render_template('grid.html', title='Grid')
#
# @app.route('/form-basic')
# def formbasic():
#     return render_template('form-basic.html', title='Form-Basic')
#
# @app.route('/form-wizard')
# def formwizard():
#     return render_template('form-wizard.html', title='Form-Wizard')
#
# @app.route('/pages-buttons')
# def buttons():
#     return render_template('pages-buttons.html', title='Butttons')
#
# @app.route('/login')
# def login():
#     return render_template('authentication-login.html', title='Login')
#
# @app.route('/register')
# def loginreg():
#     return render_template('authentication-register.html', title='Register')
#
# # route to register new users
# @app.route('/register', methods=['POST', 'GET'])
# def getForm():
#     username = request.form['username']
#     mail = request.form['mail']
#     password = request.form['password']
#     insertUser(username, mail, password)
#     return render_template('authentication-register.html', title='Register')
#
#
# # route for handling the login page logic
# @app.route('/login', methods=['POST', 'GET'])
# def testlogin():
#     error = None
#     password = request.form['password']
#     if request.method == 'POST':
#         if selectUser(request.form['username']) == True:
#             if getPassword(request.form['username']) == password:
#                 return render_template('index.html', title='IMAP Portal')
#             else:
#                 return render_template('error-403.html', title='Error403') # password not match
#         else:
#             return render_template('error-403.html', title='Error403') # user not found