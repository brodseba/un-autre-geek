from flask import Flask, Blueprint
from flask_restful import Resource, Api, reqparse
import os
from google.cloud import firestore
import __main__

app = Flask(__name__)

api_bp = Blueprint('app_v2', __name__)
api = Api(api_bp)


# Project ID is determined by the GCLOUD_PROJECT environment variable
db = firestore.Client()

doc_ref = db.collection(u'v1')

docs = doc_ref.stream()
__main__.DATA = {'places' : []}
for doc in docs:
    __main__.DATA["places"].append(doc.to_dict()["name"])


class Places(Resource):
    def get(self):
        # return our data and 200 OK HTTP code
        return {'data': __main__.DATA}, 200

    def post(self):
        # parse request arguments
        parser = reqparse.RequestParser()
        parser.add_argument('location', required=True)
        args = parser.parse_args()

        # check if we already have the location in places list
        if args['location'] in __main__.DATA['places']:
            # if we do, return 401 bad request
            return {
                'message': f"'{args['location']}' already exists."
            }, 401
        else:
            # otherwise, add the new location to places
            __main__.DATA['places'].append(args['location'])

            db.collection(u'v1').document().set({"name": args['location']})
            return {'data': __main__.DATA}, 200

    def delete(self):
        # parse request arguments
        parser = reqparse.RequestParser()
        parser.add_argument('location', required=True)
        args = parser.parse_args()

        # check if we have given location in places list
        if args['location'] in __main__.DATA['places']:
            # if we do, remove and return data with 200 OK
            __main__.DATA['places'].remove(args['location'])
            docs = db.collection(u'v1').where('name','==', args['location']).stream()
            for doc in docs:
                doc.reference.delete()
            return {'data': __main__.DATA}, 200
        else:
            # if location does not exist in places list return 404 not found
            return {
                'message': f"'{args['location']}' does not exist."
                }, 404


api.add_resource(Places, '/places')