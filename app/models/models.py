from sqlalchemy import schema
from sqlalchemy import types
from sqlalchemy import ForeignKey

from .. import db


class User(db.Model):
    __tablename__ = "user"
    user_id = schema.Column(types.Integer, primary_key=True)
    username = schema.Column(types.String(256), nullable=False)
    password = schema.Column(types.String(512), nullable=False)
    salt = schema.Column(types.String(4), nullable=False)
    private_key = schema.Column(types.String(256), nullable=False)
    disabled = schema.Column(types.Boolean)
