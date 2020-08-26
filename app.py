from flask import Flask, request, jsonify, abort
from models import User
import db

app = Flask(__name__)


@app.route("/")
def index():
    return jsonify({"message": "unnko"})


@app.route("/user/add", methods=["POST"])
def add_user():
    new_user = User(request.json["id"], request.json["password"])
    if new_user.id in db.list_user_ids():
        return jsonify({"message": f"user {new_user.id} is exists."}), 404
    db.add_user(new_user)
    return jsonify({"message": f"add user {new_user.id}."}), 200


@app.route("/user/login", methods=["POST"])
def login_user():
    user = User(request.json["id"], request.json["password"])
    return jsonify({"check": db.check_password(user)})


@app.route("/user/list")
def list_users():
    return jsonify(db.list_user_ids())


app.run(debug=True)
