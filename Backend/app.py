from flask import Flask, request, jsonify, redirect, url_for
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017")
client = MongoClient(mongo_uri)

db = client["test_db"]
collection = db["users"]
todo_collection = db["todo_items"]

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
