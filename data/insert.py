import core
conn = core.engine.connect()

ins_tb_cond = core.table_cond.insert()
ins_tb_func = core.table_func.insert()
ins_tb_terreno = core.table_terreno.insert()
ins_tb_prestserv = core.table_prestserv.insert()

def insertCond(cpf, nome, data_nasc, password):
    new_Cond = ins_tb_cond.values(cpf=cpf,
                                  nome=nome,
                                  data_nasc=data_nasc,
                                  password=password)

    conn.execute(new_Cond)

def insertFunc(cpf, nome, data_nasc, password, funcao):
    new_Func = ins_tb_func.values(cpf=cpf,
                                  nome=nome,
                                  data_nasc=data_nasc,
                                  password=password,
                                  funcao=funcao)

    conn.execute(new_Func)

def insertTerreno(lote, endereco, cpf):
    new_Terreno = ins_tb_terreno.values(lote=lote,
                                        endereco=endereco,
                                        cpf=cpf)

    conn.execute(new_Terreno)

def insertPresserv(cpf, nome, data_nasc, id_terreno):
    new_Prestserv = ins_tb_prestserv.values(cpf=cpf,
                                            nome=nome,
                                            data_nasc=data_nasc,
                                            id_terreno=id_terreno)
    conn.execute(new_Prestserv)

# Insert Multiple Values
# conn.execute(user_table.insert(),[
#     {'name': 'Monique', 'age': '25', 'password:': 'Monique123'},
#     {'name': 'Jean', 'age': '18', 'password:': 'rio123'},
#     {'name': 'Fabio', 'age': '35', 'password:': 'sp123'},
#     {'name': 'Jurandir', 'age': '27', 'password:': 'Teste'}
# ])


# To Debug
# if __name__ == '__main__':
#     ins = insertCond("12345665409", "Artur Neves", "1990-08-20", "Teste123")
#     ins = insertFunc("12309876543", "Monique Assis", "1993-03-19", "Teste321", "Administradora")
#     ins = insertTerreno(100, "Rua Teste 123", "12345665409")
#     ins = insertPresserv('12309812312', "Joao Silva", "1985-08-07", 2)