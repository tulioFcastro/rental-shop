from app import db
from sqlalchemy.sql import func


class ItemType(db.Model):
    __tablename__ = "item_type"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "id {}".format(self.id)

    def serialize(self):
        return {"id": self.id, "name": self.name}


class Item(db.Model):
    __tablename__ = "item"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    item_type_id = db.Column(
        db.Integer, db.ForeignKey("item_type.id"), nullable=True, index=True
    )

    rent_id = db.Column(db.Integer, db.ForeignKey("rent.id"), nullable=True, index=True)

    reservation_id = db.Column(
        db.Integer, db.ForeignKey("reservation.id"), nullable=True, index=True
    )

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "id {}, name {}, item_type_id {}, rent_id {}, reservation_id {}".format(
            self.id, self.name, self.item_type_id, self.rent_id, self.reservation_id,
        )

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "item_type_id": self.item_type_id,
            "rent_id": self.rent_id,
            "reservation_id": self.reservation_id,
        }


class Client(db.Model):
    __tablename__ = "client"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    rents = db.relationship("Rent", backref="rents", cascade="all")
    reservations = db.relationship("Reservation", backref="client", cascade="all")

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<id {}>".format(self.id)

    def serialize(self):
        return {"id": self.id, "name": self.name}


class Rent(db.Model):
    __tablename__ = "rent"

    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(
        db.Integer, db.ForeignKey("client.id"), nullable=True, index=True
    )
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    rent_item = db.relationship("Item", backref="rent", cascade="all")

    def __init__(self, client):
        self.client = client

    def __repr__(self):
        return "id {} client_id {}".format(self.id, self.client_id)

    def serialize(self):
        return {"id": self.id, "client": self.client_id, "created_at": self.created_at}


class Reservation(db.Model):
    __tablename__ = "reservation"

    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(
        db.Integer, db.ForeignKey("client.id"), nullable=True, index=True
    )
    reservation_date = db.Column(db.DateTime(timezone=True), server_default=func.now())
    rent_date = db.Column(db.DateTime(timezone=True), server_default=func.now())
    item = db.relationship("Item", backref="reservation", cascade="all")

    def __init__(self, client):
        self.client = client

    def __repr__(self):
        return "id {} client_id {} reservation_date {} rent_date {}".format(
            self.id, self.client_id, self.reservation_date, self.rent_date
        )

    def serialize(self):
        return {
            "id": self.id,
            "client": self.client_id,
            "reservation_date": self.reservation_date,
            "rent_date": self.rent_date,
        }
