from flask_sqlalchemy import SQLAlchemy
from datetime import datetime 

db = SQLAlchemy()

def configure(app):
    db.init_app(app)
    app.db = db


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    price = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

