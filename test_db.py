# coding=utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:cpy25511211@localhost:3306/test'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    hide = db.Column(db.Boolean, nullable=True)

    def __init__(self, username, email, hide):
        self.username = username
        self.email = email
        self.hide = hide

    def __repr__(self):
        return '<User %r>' % self.username


# db.create_all()
admin = User('admin2', 'admin2@example.com', True)
db.session.add(admin)
db.session.commit()
all = User.query.all()
for each in all:
    print each.username, each.email
# db.session.commit()

