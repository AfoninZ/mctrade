import datetime
import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class Item(SqlAlchemyBase):
    __tablename__ = 'items'

    id = sqlalchemy.Column(
        sqlalchemy.Integer,
        primary_key=True,
        autoincrement=True
    )
    game_id = sqlalchemy.Column(
        sqlalchemy.String,
        nullable=True
    )
    created_by = sqlalchemy.Column(
        sqlalchemy.Integer,
        sqlalchemy.ForeignKey('users.id')
    )
    created_date = sqlalchemy.Column(
        sqlalchemy.DateTime,
        default=datetime.datetime.now
    )
    owned_by = sqlalchemy.Column(
        sqlalchemy.Integer,
        sqlalchemy.ForeignKey('users.id')
    )
    #creator = orm.relation('User')
    #owner = orm.relation('User')