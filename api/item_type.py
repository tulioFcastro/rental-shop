from flask import abort, jsonify, request

from app import app, db
from models import ItemType


@app.route("/item_type/<item_type_id>", methods=["DELETE"])
def delete_item_type(item_type_id):
    try:
        item_type = ItemType.query.get_or_404(item_type_id)
        db.session.delete(item_type)
        db.session.commit()
        return "ItemType deleted. item_type id={}, name={}".format(
            item_type.id, item_type.name
        )
    except Exception as e:
        return str(e)


@app.route("/item_type/<item_type_id>", methods=["PUT"])
def update_item_type(item_type_id):
    if not request.is_json:
        abort(400, "The request payload is not in JSON format")
    else:
        try:
            data = request.get_json()
            if data["name"] == None:
                abort(422)
            else:
                item_type = ItemType.query.get_or_404(item_type_id)
                item_type.name = data["name"]
                db.session.add(item_type)
                db.session.commit()
                return "ItemType updated. item_type id={}, name={}".format(
                    item_type.id, item_type.name
                )
        except Exception as e:
            return str(e)


@app.route("/item_type", methods=["GET"])
def get_item_type():
    try:
        items = ItemType.query.all()
        return jsonify([e.serialize() for e in items])
    except Exception as e:
        return str(e)


@app.route("/item_type", methods=["POST"])
def post_item_type():
    if not request.is_json:
        abort(400, "The request payload is not in JSON format")
    else:
        try:
            data = request.get_json()
            if data["name"] == None:
                abort(422)
            else:
                item_type = ItemType(name=data["name"])
                db.session.add(item_type)
                db.session.commit()
                return "ItemType added. item_type id={}, name={}".format(
                    item_type.id, item_type.name
                )
        except Exception as e:
            return str(e)
