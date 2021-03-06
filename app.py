import os

from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object(os.environ["APP_SETTINGS"])
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# enable CORS
CORS(app, resources={r"/*": {"origins": "*"}})

# import API
from api import auth, item, item_type, rent, reservation, user


if __name__ == "__main__":
    app.run()
