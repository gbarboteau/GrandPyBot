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
    db.session.add(Content("THIS IS SPARTAAAAAAA!!!"))
    db.session.add(Content("What's your favorite scary movie?"))
    db.session.commit()
    lg.warning('Database initialized!')