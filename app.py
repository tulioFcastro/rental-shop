import os
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

from models import Item, ItemType

@app.route("/items")
def get_all_items():
    try:
        items=Item.query.all()
        return jsonify([e.serialize() for e in items])
    except Exception as e:
	    return(str(e))

@app.route("/item_types")
def get_all_item_types():
    try:
        items=ItemType.query.all()
        return jsonify([e.serialize() for e in items])
    except Exception as e:
	    return(str(e))

if __name__ == '__main__':
    app.run()