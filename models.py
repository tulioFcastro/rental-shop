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
    value = db.Column(db.Float(), nullable=True, default=0)

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
            "value": self.value
        }


class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    rents = db.relationship("Rent", backref="rents", cascade="all")
    reservations = db.relationship("Reservation", backref="user", cascade="all")

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return "<id {}>".format(self.id)

    def serialize(self):
        return {"id": self.id, "name": self.name, "email": self.email}


class Rent(db.Model):
    __tablename__ = "rent"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=True, index=True)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    rent_item = db.relationship("Item", primaryjoin=Item.rent_id == id)

    def __repr__(self):
        return "id {} user_id {}".format(self.id, self.user_id)

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "created_at": self.created_at,
        }


class Reservation(db.Model):
    __tablename__ = "reservation"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=True, index=True)
    reservation_date = db.Column(db.DateTime(timezone=True), server_default=func.now())
    rent_date = db.Column(db.DateTime(timezone=True), server_default=func.now())
    reserved_item = db.relationship("Item", primaryjoin=Item.reservation_id == id)

    def __repr__(self):
        return "id {} user_id {} reservation_date {} rent_date {}".format(
            self.id, self.user_id, self.reservation_date, self.rent_date
        )

    def serialize(self):
        return {
            "id": self.id,
            "user": self.user_id,
            "reservation_date": self.reservation_date,
            "rent_date": self.rent_date,
        }
