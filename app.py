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


def makeMessage(row):
    return "{} {}".format(row['index'], row['text'])

# 유저 정보 가져오기
def get_user(user_id):
    user = current_app.database.execute(
        text(
            """
        SELECT
        id,
        name,
        email,
        profile
        FROM users
        WHERE id = :user_id   
    """
        ),
        {"user_id": user_id},
    ).fetchone()

    return (
        {
            "id": user["id"],
            "name": user["name"],
            "email": user["email"],
            "profile": user["profile"],
        }
        if user
        else None
    )


def get_user_id_and_password(email):
    row = current_app.database.execute(
        text(
            """
        SELECT 
            id,
            hashed_password
        FROM users
        WHERE email = :email
    """
        ),
        {"email": email},
    ).fetchone()

    return {"id": row["id"], "hashed_password": row["hashed_password"]} if row else None


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
        return makeMessage(result[0])




    return app

