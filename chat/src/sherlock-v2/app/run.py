from flask import Flask
from flask import jsonify
from flask import request

from app import db_data
from app import db_errors
from app.rengine import Sherlock


app = Flask(__name__)
app.json.ensure_ascii = False
sherlock = Sherlock(db_data)


@app.route("/api/v1/movies/recommend", methods=["GET"])
def recommend():
    if db_errors:
        return jsonify({"errors": db_errors, "status_code": 500}), 500

    recommendation = sherlock.recommend(request.args.get("title", ""))

    return jsonify(recommendation)


@app.route("/livez", methods=["GET"])
def alive():
    return jsonify({"ping": "ok"}), 200
