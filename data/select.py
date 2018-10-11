import core
from sqlalchemy import select

# Select Condômino por CPF
def selectCond(cpf):
    selCond = select([core.table_cond]).where(core.table_cond.c.cpf == cpf)
    for row in selCond.execute():
        print(row)

# Select Funcionario por CPF
def selectFunc(cpf):
    selFunc = select([core.table_func]).where(core.table_func.c.cpf == cpf)
    for row in selFunc.execute():
        print(row)

# Select Terreno por número de lote
def  selectTerreno(lote):
    selTerreno = select([core.table_terreno]).where(core.table_terreno.c.lote == lote)
    for row in selTerreno.execute():
        print(row)

# Select Prestador de Serviço por CPF
def selectPrestserv(cpf):
    selPrestserv = select([core.table_prestserv]).where(core.table_prestserv.c.cpf == cpf)
    for row in selPrestserv.execute():
        print(row)


# To Debug
# if __name__ == '__main__':
    # sel = selectCond("38339663860")
    # sel = selectFunc("40890663971")
    # sel = selectTerreno(100)
    # sel = selectPrestserv('12309812312')