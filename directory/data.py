from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Data(db.Model):
    __tablename__ = "table"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    surname = db.Column(db.String(100))
    phone = db.Column(db.String(100))
    address = db.Column(db.String)

    def __init__(self, name, surname, phone, address):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.address = address
