from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgre:postgres@localhost/mydata'
db = SQLAlchemy(app)
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost/mydata'

engine = create_engine(SQLALCHEMY_DATABASE_URI)


# Many to many

subs = db.Table('subs',
                db.Column('user_id', db.Integer, db.ForeignKey('user.user_id')),
                db.Column('channel_id', db.Integer, db.ForeignKey('channel.channel_id'))
                )


class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    subscription = db.relationship('Channel', secondary=subs, backref=db.backref('subscribers', lazy='dynamic'))


class Channel(db.Model):
    channel_id = db.Column(db.Integer, primary_key=True)
    channel_name = db.Column(db.String(20))


# One to many
# class Person(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(20))
#     pets = db.relationship('Pet', backref='owner')
#
#
# class Pet(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(20))
#     owner_id = db.Column(db.Integer, db.ForeignKey('person.id'))


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
