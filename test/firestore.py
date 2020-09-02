from google.cloud import firestore



# Project ID is determined by the GCLOUD_PROJECT environment variable
db = firestore.Client()

doc_ref = db.collection(u'v1')

docs = doc_ref.stream()
DATA = {'places' : []}
for doc in docs:
    DATA["places"].append(doc.to_dict()["name"])

print(DATA)