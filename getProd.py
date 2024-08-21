import db
    
skus = db.getCollection("skus")
barcode = '14801010525506'
for item in skus:
    for bar in item['barcodes'] :
        if bar == barcode :
            sku = item
            continue

print(sku)
row=[]
for p in sku['goods']:
    r = {
    'name' : sku['name'],
    'bnd': sku['bnd'], 
    'cat': sku['cat'], 
    'img': sku['img'], 
    'code': p['code'], 
    'utqQty': p['utqQty'], 
    'utqName': p['utqName'], 
    'price8': p['price8'], 
    'price0': p['price0'],
    }
    row.append(r)
