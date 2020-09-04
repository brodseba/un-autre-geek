from flask import Flask, abort, jsonify, render_template, Blueprint
from v1.app import api_bp as app_v1
from v2.app import api_bp as app_v2
import os
import json
from google.cloud import firestore

app = Flask(__name__)

# Project ID is determined by the GCLOUD_PROJECT environment variable
db = firestore.Client()

doc_ref = db.collection(u'v1')

docs = doc_ref.stream()
DATA = {'places' : []}
for doc in docs:
    DATA["places"].append(doc.to_dict()["name"])

@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404

@app.route('/')
@app.route('/<name>')
def hello(name=None):
    return render_template('hello.html', name=name, data=DATA)

app.register_blueprint(app_v1, url_prefix='/app/v1')
app.register_blueprint(app_v2, url_prefix='/app/v2')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))