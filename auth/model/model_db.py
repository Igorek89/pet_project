from  sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP
from datetime import datetime


metadate = MetaData()

users = Table(
    'users',
    metadate,
    Column('id', Integer, primary_key=True),
    Column('email', String, nullable=False),
    Column('password', String, nullable=False),
    Column('created_at', TIMESTAMP, default=datetime.utcnow),
    Column('updated_at', TIMESTAMP, )
)
