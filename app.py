from flask import Flask, jsonify, request, Response, current_app, g
from flask.json import JSONEncoder
from sqlalchemy import create_engine, text
from flask_cors import CORS
import json

import libs.bibleFinder as bf
from service.remember.validator import validate
from service.remember.validator import list

from libs.htmlMaker import makeTable
from libs.htmlMaker import makeTr
import random

# Default JSON encoder는 set를 JSON으로 변환할 수 없다.
# 그러프로 커스텀 엔코더를 작성해서 set을 list로 변환하여
# JSON 으로 변환 가능하게 해주어야 한다.


class CustomJSONEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, set):
            return list(o)

        return JSONEncoder.default(self, o)


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
    def findSingle(index):
        # result = bf.findBetween("창",1, 2, 5)
        # return result[0]['text']
        result = bf.findByIndex(index)
        return makeTr(result[0])

    @app.route("/remember", methods=["GET"])
    def remember():
        num = random.randrange(0, len(list))
        dict = list[num]
        dict['index'] = num
        return json.dumps(dict)


    @app.route("/remember/answer", methods=["POST"])
    def rememberAnswer():
        num = {"num":random.randint(1, 12)}
        return json.dumps(num)

    @app.route("/json/find-single/<string:index>", methods=["GET"])
    def jsonFindSingle(index):
        result = bf.findByIndex(index)
        return json.dumps(result[0])

    @app.route("/json/find-between", methods=["GET"])
    def jsonFindBetween():
        book = request.args.get('book', default="창", type=str)
        chapter = request.args.get('chapter', default=1, type=int)
        verseFrom = request.args.get('verseFrom', default=1, type=int)
        verseTo = request.args.get('verseTo', default=1, type=int)
        verses = bf.findBetween(book, chapter, verseFrom, verseTo)
        return json.dumps(verses)

    @app.route("/find-between", methods=["GET"])
    def findBetween():
        book = request.args.get('book', default="창", type=str)
        chapter = request.args.get('chapter', default=1, type=int)
        verseFrom = request.args.get('verseFrom', default=1, type=int)
        verseTo = request.args.get('verseTo', default=1, type=int)
        verses = bf.findBetween(book, chapter, verseFrom, verseTo)
        return makeTable(verses)


    return app

