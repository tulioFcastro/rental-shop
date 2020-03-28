from flask import abort, jsonify, request

from app import app, db
from models import Client


@app.route("/client", methods=["GET"])
def get_all_clients():
    try:
        clients = Client.query.all()
        return jsonify([e.serialize() for e in clients])
    except Exception as e:
        return abort(e.code, e)


@app.route("/client", methods=["POST"])
def post_client():
    if not request.is_json:
        abort(400, "The request payload is not in JSON format")
    else:
        try:
            data = request.get_json()
            client = Client(data["name"])
            db.session.add(client)
            db.session.commit()
            return jsonify(client.serialize())
        except Exception as e:
            return abort(e.code, e)


@app.route("/client/<client_id>", methods=["GET"])
def get_client(client_id):
    try:
        client = Client.query.get_or_404(client_id)
        return jsonify(client.serialize())
    except Exception as e:
        return abort(e.code, e)


@app.route("/client/<client_id>", methods=["DELETE"])
def delete_client(client_id):
    try:
        client = Client.query.get_or_404(client_id)
        db.session.delete(client)
        db.session.commit()
        return jsonify(client.serialize())
    except Exception as e:
        return abort(e.code, e)


@app.route("/client/<client_id>", methods=["PUT"])
def update_client(client_id):
    if not request.is_json:
        abort(400, "The request payload is not in JSON format")
    else:
        try:
            data = request.get_json()
            if "name" in data.keys():
                client = Client.query.get_or_404(client_id)
                client.name = data["name"]
                db.session.add(client)
                db.session.commit()
                return jsonify(client.serialize())
            else:
                abort(422)
        except Exception as e:
            return abort(e.code, e)
