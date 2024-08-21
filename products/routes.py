from products import getSkuByBarcode
from flask import Blueprint
import db

products_bp = Blueprint('sku', __name__)

@products_bp.route('/products/<barcode>', methods=['GET'])
def GetSKUsByBarcode(barcode):
      # Get the JSON data from the request body
  return getSkuByBarcode.get_products(barcode)

@products_bp.route('/product/<barcode>', methods=['GET'])
def GetSKUByBarcode(barcode):
      # Get the JSON data from the request body
  return getSkuByBarcode.get_product(barcode)