import datetime
import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id = sqlalchemy.Column(
        sqlalchemy.Integer,
        primary_key=True,
        autoincrement=True
    )
    name = sqlalchemy.Column(
        sqlalchemy.String,
        nullable=True
    )
    hashed = sqlalchemy.Column(
        sqlalchemy.String,
        nullable=True
    )
    created_date = sqlalchemy.Column(
        sqlalchemy.DateTime,
        default=datetime.datetime.now
    )
    balance = sqlalchemy.Column(
        sqlalchemy.Integer
    )

    #items_created = orm.relation('Item', back_populates='creator')
    #items_owned = orm.relation('Item', back_populates='owner')