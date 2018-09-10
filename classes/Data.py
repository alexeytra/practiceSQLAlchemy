from app import db
class Example(db.Model):
    __tablename__ = 'data'
    id = db.column('id', db.Integer, primary_key=True)
    data = db.Column('data', db.Unicode)