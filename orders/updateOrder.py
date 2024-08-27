import db
from google.cloud import firestore
from flask import jsonify
import datetime

def update_order(order,status):
    cur = db.connectDB()
    doc_ref = cur.collection("orders")
    order_ref = doc_ref.document(order["id"])
    if status == "init" :
        order_ref.update({"qty":firestore.Increment(order['qty'])})
    order_ref.update({"leftQty":firestore.Increment(order['qty']),"status":status})
    order_ref.update({"history" : firestore.ArrayUnion([{
        "status": status,
        "creBy": order["name"],
        "qty":order["qty"],
        "time": str(datetime.datetime.now())
    }])})
    order_ref.update({"lstUpd" : str(datetime.datetime.now())})

    return jsonify({"message": "Order was updated successfully"}), 201