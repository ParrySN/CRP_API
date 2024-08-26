import db
from flask import jsonify

def submit_order(order): 
    cur = db.connectDB()
    doc_ref = cur.collection("orders")
    doc_ref.add(order)
    
    # if not order_data:
    #     return jsonify({"error": "Invalid data"}), 400
    # Return a response with the new order ID
    return jsonify({"message": "New order created successfully"}), 201