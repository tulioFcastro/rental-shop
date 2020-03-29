from flask import abort, jsonify, request

from app import app
from models import User


@app.route("/login", methods=["POST"])
def user_login():
    if not request.is_json:
        abort(400, "The request payload is not in JSON format")
    else:
        try:
            data = request.get_json()
            if "email" in data.keys():
                user = User.query.filter_by(email=data["email"]).first()
                if user is None:
                    abort(404)
                else:
                    return jsonify(user.serialize())
            else:
                abort(422)
        except Exception as e:
            return abort(e.code, e)
