from flask import Flask, jsonify, request
import json
import db

app = Flask(__name__)

name = "กุ้ย"

with open('apXrack.json', mode='r', encoding='utf-8') as json_file:
    apXrack = json.load(json_file)

for rack in apXrack:
    if rack['Rack'] == name :
        ap = rack['AP']
# Sample data: a list of products
order = db.getCollection("orders")


# Endpoint to get a product by ID
# @app.route('/product/<barcode>', methods=['GET'])
print(order)