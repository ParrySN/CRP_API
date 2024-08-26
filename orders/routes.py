from orders import createOrder
from orders import getOrder
from flask import request, Blueprint
import db

orders_bp = Blueprint('orders', __name__)

@orders_bp.route('/orders', methods=['POST'])
def CreateOrder():
    order_data = request.json  # Get the JSON data from the request body
    return createOrder.create_order(order_data)

@orders_bp.route('/orders/', methods=['GET'])
def GetOrder():
    order_data = request.json  # Get the JSON data from the request body
    return getOrder.get_order(order_data)
