import os
from flask import Flask, jsonify
from tinydb import TinyDB


def create_app(config=None):

    app = Flask(__name__)
    app.config.from_object(config or os.environ['APP_SETTINGS'])

    db = TinyDB(app.config['DATABASE'])

    @app.route("/")
    def home():
        return "Howdy from home!"

    @app.route("/fruits", methods=["GET"])
    def list_fruits():
        return jsonify(db.all())

    return app
