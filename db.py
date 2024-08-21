import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use the application default credentials.
def connectDB():
    cred = credentials.Certificate('./serviceAccount.json')

    firebase_admin.initialize_app(cred)
    db = firestore.client()
    return db

def getCollection(collection):
    db = connectDB()

    doc_ref = db.collection(collection)
    documents = doc_ref.stream()

    output = []
    for doc in documents:
        doc_dict = doc.to_dict()
        output.append(doc_dict)
    return output


