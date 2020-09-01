import flask
from v1.app import api_bp as app_v1
import os

app = flask.Flask(__name__)
app.register_blueprint(app_v1, url_prefix='/app/v1')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))