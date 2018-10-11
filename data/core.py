from sqlalchemy import (create_engine, MetaData, Column, Table, Integer, String, DateTime)
from datetime import datetime

engine = create_engine('postgresql://postgres:dbadmin@localhost:5432/flamboyant', echo=False)

metadata = MetaData(bind=engine)

# Start Tables

# Tabela de Condôminos
table_cond = Table('users', metadata,
                   Column('id', Integer, primary_key=True),
                   Column('name', String(40), index=True),
                   Column('age', Integer, nullable=False),
                   Column('password', String),
                   Column('created_in', DateTime, default=datetime.now),
                   Column('updated_in', DateTime, default=datetime.now, onupdate=datetime.now)
                   )

# Tabela de Funcionarios
table_cond = Table('users', metadata,
                   Column('id', Integer, primary_key=True),
                   Column('name', String(40), index=True),
                   Column('age', Integer, nullable=False),
                   Column('password', String),
                   Column('created_in', DateTime, default=datetime.now),
                   Column('updated_in', DateTime, default=datetime.now, onupdate=datetime.now)
                   )

# Tabela de Prestadores de Serviços
table_prestserv = Table('users', metadata,
                   Column('id', Integer, primary_key=True),
                   Column('name', String(40), index=True),
                   Column('age', Integer, nullable=False),
                   Column('password', String),
                   Column('created_in', DateTime, default=datetime.now),
                   Column('updated_in', DateTime, default=datetime.now, onupdate=datetime.now)
                   )

# Tabela de Terrenos
table_prestserv = Table('users', metadata,
                   Column('id', Integer, primary_key=True),
                   Column('name', String(40), index=True),
                   Column('age', Integer, nullable=False),
                   Column('password', String),
                   Column('created_in', DateTime, default=datetime.now),
                   Column('updated_in', DateTime, default=datetime.now, onupdate=datetime.now)
                   )


# End Tables
metadata.create_all()