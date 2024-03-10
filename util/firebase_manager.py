import datetime
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from google.cloud import storage

# Use a service account
cred = credentials.Certificate('util/serviceAccountKey.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

def pushData(data):
    doc_ref = db.collection('Database').document('status')
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


def pushVido():
    storage_client = storage.Client.from_service_account_json('util/serviceAccountKey.json')
    bucket = storage_client.get_bucket('robocup-784c9.appspot.com')
    blob = bucket.blob('output.mp4')
    blob.upload_from_filename('output.mp4')

def downloadVido():
    storage_client = storage.Client.from_service_account_json('util/serviceAccountKey.json')
    bucket = storage_client.get_bucket('robocup-784c9.appspot.com')
    blob = bucket.blob('output.mp4')
    blob.download_to_filename('output.mp4')