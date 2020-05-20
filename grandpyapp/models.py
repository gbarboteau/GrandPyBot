from flask_sqlalchemy import SQLAlchemy
import logging as lg

from .views import app

# Create database connection object
db = SQLAlchemy(app)

class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)

    def __init__(self, description):
        self.description = description

def init_db():
    db.drop_all()
    db.create_all()
    db.session.add(Content("Bonjour mon petit fardadet des étoiles !"))
    db.session.add(Content("Salutations ma petite douceur des îles !"))
    db.session.commit()
    lg.warning('Database initialized!')