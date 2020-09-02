from flask import Flask, Blueprint
from flask_restful import Resource, Api, reqparse
import os
from google.cloud import firestore

app = Flask(__name__)

api_bp = Blueprint('app_v1', __name__)
api = Api(api_bp)

DATA = {
    'places':
        ['toronto',
         'montreal',
         'chambly',
         'granby',
         'Sherbrooke']
}

class Places(Resource):
    def get(self):
        # return our data and 200 OK HTTP code
        return {'data': DATA}, 200

    def post(self):
        # parse request arguments
        parser = reqparse.RequestParser()
        parser.add_argument('location', required=True)
        args = parser.parse_args()

        # check if we already have the location in places list
        if args['location'] in DATA['places']:
            # if we do, return 401 bad request
            return {
                'message': f"'{args['location']}' already exists."
            }, 401
        else:
            # otherwise, add the new location to places
            DATA['places'].append(args['location'])
            return {'data': DATA}, 200


api.add_resource(Places, '/places')