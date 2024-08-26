from products import getSkuByBarcode
from flask import jsonify
import json
import db
from google.cloud.firestore_v1.base_query import FieldFilter



def get_order(data):
    cur = db.connectDB()
    doc_ref = cur.collection("orders")
    # get product by barcode
    
    document = doc_ref.where(filter=FieldFilter('sku', '==', data['skuId'])).where('branch','==',data['branch']).stream()
    for doc in document:    
        if doc:
            json_output = doc.to_dict()
            return json_output
        else:
            return jsonify({'error': 'Order not found'}), 404
    
    # print(id)  

# order ={
#     "barcode": "14902430735022",
#     "branch" : "000",
#     "status" : "init"
# }

# get_order(order)
