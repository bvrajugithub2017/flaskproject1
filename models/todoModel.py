from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

#create a model
class Todo(db.Model):
    tid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(20), nullable=False)
    desc = db.Column(db.String(100), nullable=False)
    created_on_date = db.Column(db.DateTime, default=datetime.now)

    def __str__(self):
        return str(self.title)