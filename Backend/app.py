from flask import Flask, request, jsonify, redirect, url_for
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():
    data = request.form or request.json

    print("RECEIVED:", data)

    return jsonify({
        "message": "Success",
        "data": data
    }), 200

@app.route("/")
def home():
    return jsonify({"message": "Flask Backend Running"})

    data = request.form or request.json

    name = data.get('name')
    email = data.get('email')

    if not name or not email:
        return jsonify({"error": "Missing fields"}), 400

    return jsonify({
        "message": "Data received successfully",
        "name": name,
        "email": email
    }), 200


@app.route('/submittodoitem', methods=['POST'])
def submit_todo():
    data = request.form or request.json

    return jsonify({
        "message": "Todo received successfully",
        "data": data
    }), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
