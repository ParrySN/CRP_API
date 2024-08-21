from flask import jsonify
import db

def create_order(order_data):
    # global order_id_counter
    cur = db.connectDB()
    orders = cur.collection("orders")
    
    if not order_data:
        return jsonify({"error": "Invalid data"}), 400
    orders.add(order_data)
    # Return a response with the new order ID
    return jsonify({"message": "Order created successfully"}), 201


