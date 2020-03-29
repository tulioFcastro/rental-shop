from models import Item, Reservation

def reserve_item(item_id, reservation_id):
    try:
        pass
        item = Item.query.get_or_404(item_id)
        item.reservation_id = reservation_id

        db.session.add(item)
        db.session.commit()

        return item
    except Exception as e:
        pass


def cancel_reservation(reservation_id):
    try:
        reservation = Reservation.query.get_or_404(reservation_id)
        db.session.delete(reservation)
        db.session.commit()
        return jsonify(reservation.serialize())
    except Exception as e:
        return abort(e.code, e)