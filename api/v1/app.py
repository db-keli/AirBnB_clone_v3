#!/usr/bin/python3
"""
Flask rest api
"""
from flask import Flask
from flask_cors import CORS
from models import storage
from api.v1.views import app_views
import os

app = Flask(__name__)
app.url_map.strict_slashes = False
app.register_blueprint(app_views)
CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def close(self):
    """call close method"""
    storage.close()


@app.errorhandler(404)
def page_not_found(e):
    """return 404 error"""
    return {"error": "Not found"}, 404


if __name__ == "__main__":
    """run the app using the env variables"""
    host = os.environ.get('HBNB_API_HOST') or '0.0.0.0'
    port = os.environ.get('HBNB_API_PORT') or 5000
    app.run(host=host, port=port, threaded=True)
