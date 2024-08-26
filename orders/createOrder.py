from flask import jsonify
from orders import submitOrder
from orders import updateOrder
import db

cur = db.connectDB()
orders = cur.collection("orders")

def create_order(order_data):
    # global order_id_counter
    try:
        order_data['order']
        return updateOrder.update_order(order_data)
    except :
        return submitOrder.submit_order(order_data)
    
    

