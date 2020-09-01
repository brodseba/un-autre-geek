from flask import Flask, abort, jsonify, render_template, Blueprint
from flask_restful import Resource, Api, reqparse
import os

app = Flask(__name__)

api_bp = Blueprint('api_v1', __name__)
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

    def delete(self):
        # parse request arguments
        parser = reqparse.RequestParser()
        parser.add_argument('location', required=True)
        args = parser.parse_args()

        # check if we have given location in places list
        if args['location'] in DATA['places']:
            # if we do, remove and return data with 200 OK
            DATA['places'].remove(args['location'])
            return {'data': DATA}, 200
        else:
            # if location does not exist in places list return 404 not found
            return {
                'message': f"'{args['location']}' does not exist."
                }, 404


api.add_resource(Places, '/places')


@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404


@app.route('/')
@app.route('/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


@app.route('/list')
def list(data=None):
    return render_template('places.html', data=DATA)