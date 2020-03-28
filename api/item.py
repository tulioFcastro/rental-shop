from flask import jsonify

from app import app

# import models
from models import Item


@app.route("/item", methods=["GET"])
def get_items():
    try:
        items = Item.query.all()
        return jsonify([e.serialize() for e in items])
    except Exception as e:
        return str(e)
