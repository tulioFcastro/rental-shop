from flask import abort, jsonify, request

from app import app, db
from models import User, Rent
from api.util import rent_item, return_item


@app.route("/rent", methods=["GET"])
def get_all_rents():
    try:
        rents = Rent.query.all()
        return jsonify([e.serialize() for e in rents])
    except Exception as e:
        return abort(e.code, e)


@app.route("/rent", methods=["POST"])
def post_rent():
    if not request.is_json:
        abort(400, "The request payload is not in JSON format")
    else:
        try:
            data = request.get_json()
            if "user_id" in data.keys() and "item_id" in data.keys():
                user = User.query.get_or_404(data["user_id"])
                rent = Rent()
                rent.user_id = user.id
                db.session.add(rent)
                db.session.commit()
                rent_item(data["item_id"], rent.id)
                return jsonify(rent.serialize())
            else:
                abort(422)
        except Exception as e:
            return abort(e.code, e)


@app.route("/rent/<rent_id>", methods=["GET"])
def get_rent(rent_id):
    try:
        rent = Rent.query.get_or_404(rent_id)
        return jsonify(rent.serialize())
    except Exception as e:
        return abort(e.code, e)


@app.route("/rent/<rent_id>", methods=["DELETE"])
def delete_rent(rent_id):
    return return_item(rent_id)


@app.route("/rent/<rent_id>", methods=["PUT"])
def update_rent(rent_id):
    if not request.is_json:
        abort(400, "The request payload is not in JSON format")
    else:
        try:
            data = request.get_json()
            if "user_id" in data.keys():
                rent = Rent.query.get_or_404(rent_id)
                print(rent)
                user = user.query.get_or_404(data["user_id"])
                print(user)
                rent.user_id = user.id
                db.session.add(rent)
                db.session.commit()
                return jsonify(rent.serialize())
            else:
                abort(422)
        except Exception as e:
            return abort(e.code, e)
