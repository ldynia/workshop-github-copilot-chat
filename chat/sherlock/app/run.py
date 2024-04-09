import os
import json
from json.decoder import JSONDecodeError

from flask import Flask
from flask import jsonify
from flask import render_template
from flask import request

from rengine import Sherlock


app = Flask(__name__)
app.json.ensure_ascii = False
APP_DIR = os.path.dirname(os.path.realpath(__file__))

def read_data(source):
    data = []
    errors = []
    try:
        with open(source) as db:
            content = db.read()
        data = json.loads(content)
    except FileNotFoundError as e:
        errors = [f"Reading {source}, {str(e)}"]
    except JSONDecodeError as e:
        errors = [f"Reading {source}, {str(e)}"]
    except Exception as e:
        errors = [f"Reading {source}, {str(e)}"]

    return data, errors


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/livez", methods=["GET"])
def alive():
    return jsonify({"ping": "ok"}), 200


@app.route("/api/v1/movies/recommend", methods=["GET"])
def recommend():
    MOVIES, errors = read_data(f"{APP_DIR}/db.json")
    if errors:
        return jsonify({"errors": errors, "status_code": 500}), 500

    sherlock = Sherlock(MOVIES, request.args)
    recommendation = sherlock.recommend()

    return jsonify(recommendation)
