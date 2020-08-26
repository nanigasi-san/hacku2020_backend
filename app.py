from flask import Flask, jsonify
app = Flask(__name__)


@app.route("/")
def index():
    return jsonify({"message": "unnko"})

@app.route("/")