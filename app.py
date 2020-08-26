from flask import Flask, request, jsonify
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


@app.route("/user/login", methods=["POST"])
def login_user():
    username, password_hash_md5 = request.json["username"], request.json["password_hash"]
    return jsonify({"check": db.check_password_hash(username, password_hash_md5)})


@app.route("/user/list")
def list_users():
    return jsonify(db.list_user_usernames())


@app.route("/contest/add", methods=["POST"])
def add_contest():
    contest_name = request.json["contest_name"]
    start = request.json["start"]
    finish = request.json["finish"]
    data_path = request.json["data_path"]
    db.add_contest(contest_name, start, finish, data_path)
    return jsonify({})


@app.route("/contest/join", methods=["POST"])
def join_contest():
    contest_name = request.json["contest_name"]
    username = request.json["username"]
    db.join_contest(contest_name, username)
    return jsonify({})


@app.route("/contest/<contest_name>")
def get_contest(contest_name):
    data = db.get_contest_info(contest_name)
    return jsonify(data)


@app.route("/contest/standings/<contest_name>")
def get_standings(contest_name):
    return jsonify(db.get_standings(contest_name))


app.run(debug=True)
