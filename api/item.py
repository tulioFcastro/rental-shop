from flask import jsonify, abort, request

from app import app, db

from models import Item, ItemType


@app.route("/item", methods=["GET"])
def get_all_items():
    try:
        items = Item.query.all()
        return jsonify([e.serialize() for e in items])
    except Exception as e:
        return abort(e.code, e)


@app.route("/item", methods=["POST"])
def post_item():
    if not request.is_json:
        abort(400, "The request payload is not in JSON format")
    else:
        try:
            data = request.get_json()
            item = Item(data["name"])
            if "item_type_id" in data.keys():
                item_type = ItemType.query.get_or_404(data["item_type_id"])
                item.item_type_id = item_type.id
                item.type = item_type
            db.session.add(item)
            db.session.commit()
            return jsonify(item.serialize())
        except Exception as e:
            return abort(e.code, e)


@app.route("/item/<item_id>", methods=["GET"])
def get_item(item_id):
    try:
        item = Item.query.get_or_404(item_id)
        return jsonify(item.serialize())
    except Exception as e:
        return abort(e.code, e)


@app.route("/item/<item_id>", methods=["DELETE"])
def delete_item(item_id):
    try:
        item = Item.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return jsonify(item.serialize())
    except Exception as e:
        return abort(e.code, e)


@app.route("/item/<item_id>", methods=["PUT"])
def update_item(item_id):
    if not request.is_json:
        abort(400, "The request payload is not in JSON format")
    else:
        try:
            data = request.get_json()
            if data["name"] is None:
                abort(422)
            else:
                item = Item.query.get_or_404(item_id)
                if data["item_type_id"]:
                    item_type = ItemType.query.get_or_404(data["item_type_id"])
                    item.type = item_type
                item.name = data["name"]
                db.session.add(item)
                db.session.commit()
                return jsonify(item.serialize())
        except Exception as e:
            return abort(e.code, e)
