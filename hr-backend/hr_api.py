"""
API: 1) rest over http: pull
     2) rest over websocket: pull/push/publish-subscribe
"""
import json

from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO
from pymongo import MongoClient

from hr.util import extract_employee_from_request

app = Flask(__name__)
app.config['DEBUG'] = True
cors = CORS(app)  # cross origin
socketio = SocketIO(app, cors_allowed_origins="*")

mongo_client = MongoClient("mongodb://localhost:27017")

hr_db = mongo_client['hr'].employees

"""
    1. REST over HTTP
"""
fields = ["identity", "fullName", "iban", "photo", "birthYear", "salary", "department", "fulltime"]


@app.route("/hr/api/v1/employees", methods=["GET"])
def getEmployees():
    return json.dumps([emp for emp in hr_db.find({})])


@app.route("/hr/api/v1/employees/<identity>", methods=["GET"])
def getEmployeeByIdentity(identity):
    return jsonify(hr_db.find_one({'_id': identity}))


@app.route("/hr/api/v1/employees", methods=["POST"])
def addEmployee():
    emp = extract_employee_from_request(request, fields)
    emp["_id"] = emp['identity']
    hr_db.insert_one(emp)
    socketio.emit('hire', emp)
    return jsonify({'status': 'ok'})


@app.route("/hr/api/v1/employees/<identity>", methods=["PUT", "PATCH"])
def updateEmployee(identity):
    emp = extract_employee_from_request(request, fields)
    emp["_id"] = identity
    employee = hr_db.find_one_and_update(
        {"_id": identity},
        {"$set": emp},
        upsert=False
    )
    return jsonify(employee)


@app.route("/hr/api/v1/employees/<identity>", methods=["DELETE"])
def removeEmployee(identity):
    employee = hr_db.find_one({"_id": identity})
    hr_db.delete_one({"_id": identity})
    socketio.emit('fire', employee)
    return jsonify(employee)


"""
    2. REST ove Websocket
"""


@socketio.on('message')
def handle_message(msg):
    print(f"received message: {msg}")


socketio.run(app, port=7001)
