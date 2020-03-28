from app import db

class Item(db.Model):
    __tablename__ = 'item'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    item_type_id = db.Column(db.Integer, db.ForeignKey('item_type.id'), nullable=False)
    rent_id = db.relationship('Rent', backref='item', lazy=True)
    reservation_id = db.relationship('Reservation', backref='item', lazy=True)

    def __init__(self, name, item_type_id):
        self.name = name
        self.item_type_id = item_type_id

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'id': self.id, 
            'name': self.name
        }

class ItemType(db.Model):
    __tablename__ = 'item_type'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    item_id = db.relationship('Item', backref='item_type', lazy=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'id': self.id, 
            'name': self.name
        }

class Client(db.Model):
    __tablename__ = 'client'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    rent_id = db.relationship('Rent', backref='client', lazy=True)
    reservation_id = db.relationship('Reservation', backref='client', lazy=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'id': self.id, 
            'name': self.name
        }

class Rent(db.Model):
    __tablename__ = 'rent'

    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'), nullable=False)

class Reservation(db.Model):
    __tablename__ = 'reservation'

    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'), nullable=False)