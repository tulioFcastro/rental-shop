from flask import abort, jsonify, request

from app import app, db
from models import User


@app.route("/user", methods=["GET"])
def get_all_users():
    try:
        users = User.query.all()
        return jsonify([e.serialize() for e in users])
    except Exception as e:
        return abort(e.code, e)


@app.route("/user", methods=["POST"])
def post_user():
    if not request.is_json:
        abort(400, "The request payload is not in JSON format")
    else:
        try:
            data = request.get_json()
            if "email" in data.keys() and "name" in data.keys():
                user = User(data["name"], data["email"])
                db.session.add(user)
                db.session.commit()
                return jsonify(user.serialize())
            else:
                abort(422)
        except Exception as e:
            return abort(e.code, e)


@app.route("/user/<user_id>", methods=["GET"])
def get_user(user_id):
    try:
        user = User.query.get_or_404(user_id)
        return jsonify(user.serialize())
    except Exception as e:
        return abort(e.code, e)


@app.route("/user/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    try:
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return jsonify(user.serialize())
    except Exception as e:
        return abort(e.code, e)


@app.route("/user/<user_id>", methods=["PUT"])
def update_user(user_id):
    if not request.is_json:
        abort(400, "The request payload is not in JSON format")
    else:
        try:
            data = request.get_json()
            if "name" in data.keys():
                user = User.query.get_or_404(user_id)
                user.name = data["name"]
                db.session.add(user)
                db.session.commit()
                return jsonify(user.serialize())
            else:
                abort(422)
        except Exception as e:
            return abort(e.code, e)
