import db
import json

with open('SKUs.json', 'r') as file:
    skus = json.load(file)
    
cur = db.connectDB()
record = 0
doc_ref = cur.collection("skus")
for sku in skus:
    record += 1
    print(record)
    doc_ref.add(sku)

# users_ref = cur.collection("skus")
# docs = users_ref.stream()

# for doc in docs:
#     print(f"{doc.id} => {doc.to_dict()}")