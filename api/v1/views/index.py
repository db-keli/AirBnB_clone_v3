#!/usr/bin/python3
"""
Blueprint for the API
"""

from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'])
def status():
    """return status"""
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'])
def stats():
    """return stats"""
    from models import storage
    classes = {"Amenity": "amenities", "City": "cities", "Place": "places",
               "Review": "reviews", "State": "states", "User": "users"}
    stats = {}
    for key, value in classes.items():
        stats[value] = storage.count(key)
    return jsonify(stats)
