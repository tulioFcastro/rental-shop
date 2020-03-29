from flask import abort, jsonify

from app import db
from models import Item, Rent, Reservation


def reserve_item(item_id, reservation_id):
    try:
        pass
        item = Item.query.get_or_404(item_id)
        item.reservation_id = reservation_id

        db.session.add(item)
        db.session.commit()

        return item
    except Exception as e:
        return abort(e.code, e)


def cancel_reservation(reservation_id):
    try:
        reservation = Reservation.query.get_or_404(reservation_id)
        db.session.delete(reservation)
        db.session.commit()
        return jsonify(reservation.serialize())
    except Exception as e:
        return abort(e.code, e)

def rent_item(item_id, rent_id):
    try:
        print('rent_item', rent_id)
        item = Item.query.get_or_404(item_id)
        item.rent_id = rent_id
        print('rent_item', item)
        db.session.add(item)
        db.session.commit()
        return jsonify(item.serialize())
    except Exception as e:
        return abort(e.code, e)

def return_item(rent_id):
    try:
        rent = Rent.query.get_or_404(rent_id)
        db.session.delete(rent)
        db.session.commit()
        return jsonify(rent.serialize())
    except Exception as e:
        return abort(e.code, e)