import datetime
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account
cred = credentials.Certificate('serviceAccountKey.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

def setTemp(Temp=25, Hum=55, Pres=1000):
    Date = datetime.datetime.now()
    # キーを日付時刻で作成
    ref = db.collection('Database').document(str(Date))
    ref.set({
        u'Pres': Pres,
        u'Hum': Hum,
        u'Temp': Temp,
    })

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

if __name__ == '__main__':
    setTemp()
    resizeDatabase()