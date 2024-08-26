import db
from google.cloud import firestore
from flask import jsonify

def update_order(order):
    cur = db.connectDB()
    transaction = cur.transaction()
    doc_ref = cur.collection("orders")
    order_ref = doc_ref.document(order['id'])
    # snapshot = order_ref.get(transaction=transaction).get('qty')
    order_ref.update({"qty" : firestore.Increment(order['qty']),"leftQty":firestore.Increment(order['qty'])})

    # if not order_data:
    #     return jsonify({"error": "Invalid data"}), 400
    # # Return a response with the new order ID
    return jsonify({"message": "Order was updated successfully"}), 201

