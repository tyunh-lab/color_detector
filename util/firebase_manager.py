import datetime
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account
cred = credentials.Certificate('serviceAccountKey.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

def pushData(data):
    doc_ref = db.collection('Database').document(str(datetime.datetime.now()))
    doc_ref.set(data)

maxLength = 20

def resizeDatabase():
    ref = db.collection('Database')
    docs = ref.stream()
    dataSize = 0
    for doc in docs:
        print(doc.id, doc._data)
        dataSize += 1
        if dataSize == 1:
            firstDateId = doc.id

    if dataSize > maxLength:
        deleteDoc(firstDateId)

def deleteDoc(id):
    db.collection('Database').document(id).delete()