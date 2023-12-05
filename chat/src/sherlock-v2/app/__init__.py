import sys
import os
import json
from json.decoder import JSONDecodeError


# Add current working dir to system path
sys.path.append(os.path.dirname(os.path.realpath(__file__)))


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


APP_DIR = os.path.dirname(os.path.realpath(__file__))
db_data, db_errors = read_data(f"{APP_DIR}/db.json")
