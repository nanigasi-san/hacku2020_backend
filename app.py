from flask import Flask, request, jsonify, abort
import db

app = Flask(__name__)


@app.route("/")
def index():
    return jsonify({"message": "unnko"})


@app.route("/user/add", methods=["POST"])
def add_user():
    username, password_hash_md5 = request.json["username"], request.json["password_hash"]
    if username in db.list_user_usernames():
        return jsonify({"message": f"user {username} is exists."}), 404
    db.add_user(username, password_hash_md5)
    return jsonify({"message": f"add user {username}."}), 200


@app.route("/user/login", methods = ["POST"])
def login_user():
    username, password_hash_md5=request.json["username"], request.json["password_hash"]
    return jsonify({"check": db.check_password_hash(username, password_hash_md5)})


@app.route("/user/list")
def list_users():
    return jsonify(db.list_user_usernames())


app.run(debug=True)
