from google.cloud import firestore



# Project ID is determined by the GCLOUD_PROJECT environment variable
db = firestore.Client()

docs = db.collection(u'v1').stream()

DATA = {'places' : []}
for doc in docs:
    DATA["places"].append(doc.to_dict()["name"])

print(DATA)

db.collection(u'v1').document().set({"name": "testghfhgf"})

DATA = {'places' : []}
for doc in docs:
    DATA["places"].append(doc.to_dict()["name"])

docs = db.collection(u'v1').where('name','==', 'testghfhgf').stream()
for doc in docs:
    doc.reference.delete()

DATA = {'places' : []}
for doc in docs:
    DATA["places"].append(doc.to_dict()["name"])
