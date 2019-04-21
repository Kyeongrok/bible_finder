import bcrypt
import jwt

from flask import Flask, jsonify, request, Response, current_app, g
from flask.json import JSONEncoder
from sqlalchemy import create_engine, text
from datetime import datetime, timedelta
from functools import wraps
from flask_cors import CORS

import libs.bibleFinder as bf

# Default JSON encoder는 set를 JSON으로 변환할 수 없다.
# 그러프로 커스텀 엔코더를 작성해서 set을 list로 변환하여
# JSON 으로 변환 가능하게 해주어야 한다.


class CustomJSONEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, set):
            return list(o)

        return JSONEncoder.default(self, o)


def makeHtmlMessage(row):
    return "<html><body>{} {}</body></html>".format(row['index'], row['text'])


def create_app(test_config=None):
    app = Flask(__name__)

    CORS(app)
    app.json_encoder = CustomJSONEncoder

    if test_config is None:
        app.config.from_pyfile("config.py")
    else:
        app.config.update(test_config)

    database = create_engine(app.config["DB_URL"], encoding="utf-8", max_overflow=0)
    app.database = database

    @app.route("/find-single/<string:index>", methods=["GET"])
    def ping(index):
        # result = bf.findBetween("창",1, 2, 5)
        # return result[0]['text']
        result = bf.findByIndex(index)
        return makeHtmlMessage(result[0])


    @app.route("/find-between", methods=["GET"])
    def findBetween():
        book = request.args.get('book', default="창", type=str)
        result = bf.findBetween("창",1, 2, 5)
        # return result[0]['text']
        # result = bf.findByIndex(index)

        return book


    return app

