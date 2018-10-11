from sqlalchemy import (create_engine, MetaData, Column, Table, Integer, String, DateTime, Date, ForeignKey)
from datetime import datetime

engine = create_engine('postgresql://postgres:dbadmin@localhost:5432/flamboyant', echo=True)

metadata = MetaData(bind=engine)

# Start Tables

# Tabela de Condôminos
table_cond = Table('tb_cond', metadata,
                   Column('cpf', String(11), primary_key=True),
                   Column('nome', String(40), index=True, nullable=False),
                   Column('data_nasc', Date, nullable=False),
                   Column('password', String, nullable=False),
                   Column('created_in', DateTime, default=datetime.now),
                   Column('updated_in', DateTime, default=datetime.now, onupdate=datetime.now)
                   )

# Tabela de Funcionarios
table_func = Table('tb_func', metadata,
                   Column('cpf', String(11), primary_key=True),
                   Column('nome', String(40), index=True, nullable=False),
                   Column('data_nasc', Date, nullable=False),
                   Column('password', String, nullable=False),
                   Column('funcao', String, nullable=False),
                   Column('created_in', DateTime, default=datetime.now),
                   Column('updated_in', DateTime, default=datetime.now, onupdate=datetime.now)
                   )

# Tabela de Terrenos
table_terreno = Table('tb_terreno', metadata,
                   Column('id_terreno', Integer, primary_key=True),
                   Column('lote', Integer, index=True, nullable=False),
                   Column('endereco', String, nullable=False),
                   Column('cpf', String(11), ForeignKey("tb_cond.cpf")),
                   Column('created_in', DateTime, default=datetime.now),
                   Column('updated_in', DateTime, default=datetime.now, onupdate=datetime.now)
                   )

# Tabela de Prestadores de Serviços
table_prestserv = Table('tb_prestserv', metadata,
                   Column('cpf', String(11), primary_key=True),
                   Column('nome', String(40), index=True, nullable=False),
                   Column('data_nasc', Date, nullable=False),
                   Column('id_terreno', Integer, ForeignKey("tb_terreno.id_terreno"), nullable=False),
                   Column('created_in', DateTime, default=datetime.now),
                   Column('updated_in', DateTime, default=datetime.now, onupdate=datetime.now)
                   )


# End Tables
metadata.create_all()