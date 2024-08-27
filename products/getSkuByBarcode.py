from flask import jsonify
import json
import db
from orders import getOrder
from google.cloud.firestore_v1.base_query import FieldFilter

# Sample data: a list of products

cur = db.connectDB()
doc_ref = cur.collection("skus")

def get_products(branch,barcode):
    # Find the product with the given ID
    documents = doc_ref.where(filter=FieldFilter('barcodes', 'array_contains', barcode)).stream()
    for skus in documents:
        product = skus.to_dict()
    product["id"] = skus.id
    order = getOrder.get_order({"skuId": skus.id,"branch" : branch,})
    output = json.dumps({"sku":product,"order": order},ensure_ascii=False, indent=2)
    if product:
        return jsonify(output), 200
    else:
        return jsonify({'error': 'Product not found'}), 404
    
def get_product(barcode):
    # Find the product with the given ID
    documents = doc_ref.where(filter=FieldFilter('barcodes', 'array_contains', barcode)).stream()
    
    if documents :
        # for doc in documents:
        #     print(f'{doc.id} => {doc.to_dict()}')  
        row=[]
        for skus in documents:
            sku = skus.to_dict()
            row.append({"sku_id":skus.id}) 
            r = {
                "name": sku['name'],
                "bnd": sku['bnd'],
                "cat": sku['cat'],
                "img": sku['img'],
                "ap": sku['ap'],
                "code": sku['goods']['code' == barcode]['code'],
                "utqQty":sku['goods']['code' == barcode]['utqQty'],
                "utqName": sku['goods']['code' == barcode]['utqName'],
                "price8": sku['goods']['code' == barcode]['price8'],
                "price0": sku['goods']['code' == barcode]['price0']
                }
        row.append(r)
    
    if row:
        json_output = json.dumps(row, ensure_ascii=False, indent=2)
        return json_output
    else:
        return jsonify({'error': 'Product not found'}), 404
    
# print(get_product("8850006322482"))