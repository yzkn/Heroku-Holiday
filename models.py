from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, Unicode, UnicodeText, ForeignKey
from datetime import datetime

db = SQLAlchemy()

class Holiday(db.Model):
    """
    祝日
    """
    __tablename__ = "holidays"
    id = Column(Integer, primary_key=True)
    date = Column(Unicode(8), unique=True)
    name = Column(Unicode(255), unique=True)

    def __init__(self, date, name):
        self.date = date
        self.name = name

    def __repr__(self):
        return '<Holiday %r>' % self.name