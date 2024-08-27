from orders import submitOrder
from orders import updateOrder

def create_order(order_data):
    # global order_id_counter
    try:
        order_data['id']
        return updateOrder.update_order(order_data,"init")
    except :
        return submitOrder.submit_order(order_data)
        # return "None"
    
    

