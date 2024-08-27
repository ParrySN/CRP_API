import db
from flask import jsonify
import datetime

def submit_order(data): 
    cur = db.connectDB()
    doc_ref = cur.collection("orders")
    order = {
    "branch": data["branch"],
    "name": data['name'],
    "utqName": data['utqName'],
    "utqQty": data['utqQty'],
    "code": data['code'],
    "sku": data['sku'],
    "ap": data['ap'],
    "qty": data["qty"],
    "leftQty": data["qty"],
    "status": 'init',
    "startDate": str(datetime.datetime.now()),
    "lstUpd": None,
    "cat": data['cat'],
    "bnd": data['bnd'],
    "tag": data["tag"],
    "history" :[{
        "status":"init",
        "creBy": data["user"],
        "qty":data["qty"],
        "time": str(datetime.datetime.now())
    }]}
    doc_ref.add(order)
    
    # if not order_data:
    #     return jsonify({"error": "Invalid data"}), 400
    # Return a response with the new order ID
    return jsonify({"message": "New order created successfully"}), 201