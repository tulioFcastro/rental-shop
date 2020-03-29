from flask import abort, jsonify, request

from app import app, db
from models import Item, Reservation, User
from api.util import cancel_reservation, reserve_item


@app.route("/reservation", methods=["GET"])
def get_all_reservations():
    try:
        reservations = Reservation.query.all()
        return jsonify([e.serialize() for e in reservations])
    except Exception as e:
        return abort(e.code, e)


@app.route("/reservation", methods=["POST"])
def post_reservation():
    if not request.is_json:
        abort(400, "The request payload is not in JSON format")
    else:
        try:
            data = request.get_json()
            if (
                "user_id" in data.keys()
                and "item_id" in data.keys()
                and "rent_date" in data.keys()
            ):
                user = User.query.get_or_404(data["user_id"])
                reservation = Reservation()
                reservation.user_id = user.id
                reservation.rent_date = data["rent_date"]

                db.session.add(reservation)
                db.session.commit()

                reserve_item(data["item_id"], reservation.id)
                return jsonify(reservation.serialize())
            else:
                abort(422)
        except Exception as e:
            return abort(e.code, e)


@app.route("/reservation/<reservation_id>", methods=["GET"])
def get_reservation(reservation_id):
    try:
        reservation = Reservation.query.get_or_404(reservation_id)
        return jsonify(reservation.serialize())
    except Exception as e:
        return abort(e.code, e)


@app.route("/reservation/<reservation_id>", methods=["DELETE"])
def delete_reservation(reservation_id):
    return cancel_reservation(reservation_id)
