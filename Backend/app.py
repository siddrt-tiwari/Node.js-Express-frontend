from flask import Flask, request, jsonify, redirect, url_for
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

mongo_uri = os.getenv("MONGO_URI")
client = MongoClient(mongo_uri)

db = client["test_db"]
collection = db["users"]
todo_collection = db["todo_items"]

@app.route('/submit', methods=['POST'])
def submit():
    data = request.form or request.json

    name = data.get('name')
    email = data.get('email')

    if not name or not email:
        return jsonify({"error": "Missing fields"}), 400

    if collection.find_one({"email": email}):
        return jsonify({"error": "Email exists"}), 400

    collection.insert_one({"name": name, "email": email})
    return jsonify({"message": "Success"}), 200


@app.route('/submittodoitem', methods=['POST'])
def submit_todo():
    data = request.form or request.json

    item_name = data.get('itemName')
    item_description = data.get('itemDescription')
    item_id = data.get('itemId')

    if not item_name or not item_description or not item_id:
        return jsonify({"error": "Missing fields"}), 400

    todo_collection.insert_one({
        "itemId": item_id,
        "itemName": item_name,
        "itemDescription": item_description
    })

    return jsonify({"message": "Success"}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)