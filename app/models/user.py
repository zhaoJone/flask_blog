from datetime import datetime

from sqlalchemy.dialects.mysql import INTEGER

from settings import db


class User(db.Model):
    id = db.Column(INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    avatar = db.Column(db.String(200), nullable=False)
    info = db.Column(db.Text)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
