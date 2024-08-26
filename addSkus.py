import db
import json

with open('PC.json', 'r') as file:
    data = json.load(file)
    
cur = db.connectDB()
record = 0
doc_ref = cur.collection("users")
for d in data:
    doc_ref.document(d['Code']).set(d)
    record += 1
    print(record)
    
    # doc_ref.add(data)

users_ref = cur.collection("users")
doc = users_ref.document("54801").get()

# print(docs.get())
print(f"{doc.id} => {doc.to_dict()}")
# for doc in docs:

