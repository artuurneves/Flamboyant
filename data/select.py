from data import core
from sqlalchemy import select

# Select * from TB_COND
def select_All_Cond():
    selCond = select([core.table_cond])
    for row in selCond.execute():
        print(row)

# Select Condômino por CPF
def select_CPF_Cond(cpf):
    selCond = select([core.table_cond]).where(core.table_cond.c.cpf == cpf)
    for row in selCond.execute():
        print(row)

# Select * from TB_FUNC
def select_All_Func():
    selFunc = select([core.table_func])
    for row in selFunc.execute():
        print(row)

# Select Funcionario por CPF
def selectFunc(cpf):
    selFunc = select([core.table_func]).where(core.table_func.c.cpf == cpf)
    for row in selFunc.execute():
        print(row)

# Select * from TB_TERRENO
def select_All_Terreno():
    selTerreno = select([core.table_terreno])
    for row in selTerreno.execute():
        print(row)

# Select Terreno por número de lote
def  selectTerreno(lote):
    selTerreno = select([core.table_terreno]).where(core.table_terreno.c.lote == lote)
    for row in selTerreno.execute():
        print(row)

# Select * from TB_PrestServ
def select_All_PrestServ():
    selPrestServ = select([core.table_prestserv])
    for row in selPrestServ.execute():
        print(row)

# Select Prestador de Serviço por CPF
def selectPrestserv(cpf):
    selPrestserv = select([core.table_prestserv]).where(core.table_prestserv.c.cpf == cpf)
    for row in selPrestserv.execute():
        print(row)


# To Debug
# if __name__ == '__main__':
    # sel = select_All_Cond()
    # sel = select_CPF_Cond("38339663860")
    # sel = select_All_Func()
    # sel = selectFunc("40890663971")
    # sel = select_All_Terreno()
    # sel = selectTerreno(100)
    # sel = select_All_PrestServ()
    # sel = selectPrestserv('12309812312')