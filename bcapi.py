import os
import pusher
from pymongo import Connection, ASCENDING
from bson.objectid import ObjectId
from bson import json_util
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash, jsonify, json


# The app
app = Flask(__name__)
app.config.from_object('settings')

# Pusher
pusher.app_id = app.config['PUSHER_APP_ID']
pusher.key = app.config['PUSHER_KEY']
pusher.secret = app.config['PUSHER_SECRET']


# DB Connection
def connect_db():
    connection = Connection(app.config['DB_URI'])
    return connection[app.config['DB_NAME']]


# Middleware
@app.before_request
def before_request():
    g.db = connect_db()


@app.teardown_request
def teardown_request(exception):
    g.db.connection.close()


# Views
@app.route('/event', methods=['GET'])
def events():
    return json.dumps(g.db.event_user.distinct('event'), default=json_util.default)


@app.route('/event/<event_id>', methods=['GET', 'POST'])
def event(event_id):
    if request.method == 'GET':
        events = [e for e in g.db.event_user.find({'event':event_id})]
        return json.dumps(events, default=json_util.default)

    elif request.method == 'POST':
        post = json.loads(request.data)
        events = []
        for e in post:
            e.update(event=event_id)
            events.append(e)
        g.db.event_user.insert(events)
        g.db.event_user.create_index([('event', ASCENDING)])
        
        p = pusher.Pusher()
        p['core'].trigger('user_created', json.loads(json.dumps(events, default=json_util.default)))
        return json.dumps(events, default=json_util.default)


@app.route('/event/<event_id>/<user_id>', methods=['GET', 'PUT'])
def user(event_id, user_id):
    if request.method == 'GET':
        user = g.db.event_user.find_one({'event':event_id, '_id':ObjectId(user_id)})
        return json.dumps(user, default=json_util.default)
    
    elif request.method == 'PUT':
        put = json.loads(request.data)
        g.db.event_user.update({'event':event_id, '_id':ObjectId(user_id)},
            {"$set": {"checked_in": put['checked_in']}})
        user = g.db.event_user.find_one({'event':event_id, '_id':ObjectId(user_id)})

        p = pusher.Pusher()
        p['core'].trigger('user_updated', json.loads(json.dumps(user, default=json_util.default)))
        return json.dumps(user, default=json_util.default)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
