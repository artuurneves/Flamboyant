from flask import render_template, request, session, flash, abort, redirect, url_for
from app import app
from data import insert as ins
# from mymap.database.core_select import selectUser as selectUser
# from mymap.database.core_select import getPassword as getPassword

@app.route('/')
@app.route('/home')
def homepage():
    return render_template('homepage.html', title='Homepage')

@app.route('/conscond')
def conscond():
    return render_template('consulta-condominos.html', title='Consulta Condominos')

@app.route('/cadcond')
def cadcond():
    return render_template('cadastro-condominos.html', title='Cadastro Condominos')

@app.route('/cadcond', methods=['POST', 'GET'])
def getCadCond():
    condcpf = request.form['condcpf']
    condnome = request.form['condnome']
    conddn = request.form['conddn']
    condpw = request.form['condpw']
    ins.insertCond(condcpf, condnome, conddn, condpw)
    return render_template('homepage.html', title='Homepage')

@app.route('/cadfunc')
def cadfunc():
    return render_template('cadastro-funcionario.html', title='Cadastro Funcionario')

@app.route('/cadfunc', methods=['POST', 'GET'])
def getCadFunc():
    funccpf = request.form['funccpf']
    funcnome = request.form['funcnome']
    funcdn = request.form['funcdn']
    funcpw = request.form['funcpw']
    funcfuncao = request.form['funcfuncao']
    ins.insertFunc(funccpf, funcnome, funcdn, funcpw, funcfuncao)
    return render_template('homepage.html', title='Homepage')


@app.route('/cadprestserv')
def cadprestserv():
    return render_template('cadastro-prestserv.html', title='Cadastro Prestador de Serviço')

@app.route('/cadprestserv', methods=['POST', 'GET'])
def getPrestServ():
    prestservcpf = request.form['prestservcpf']
    prestservnome = request.form['prestservnome']
    prestservdn = request.form['prestservdn']
    prestservid_terreno = request.form['prestservid_terreno']
    ins.insertPresserv(prestservcpf, prestservnome, prestservdn, prestservid_terreno)
    return render_template('homepage.html', title='Homepage')


@app.route('/cadterreno')
def cadterreno():
    return render_template('cadastro-terreno.html', title='Cadastro Terreno')

@app.route('/cadterreno', methods=['POST', 'GET'])
def getCadTerreno():
    terrenolote = request.form['terrenolote']
    terrenoendereco = request.form['terrenoendereco']
    terrenoid_cpf = request.form['terrenoid_cpf']
    ins.insertTerreno(terrenolote, terrenoendereco, terrenoid_cpf)
    return render_template('homepage.html', title='Homepage')
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