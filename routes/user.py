# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from flask import current_app as app, jsonify, request
from business.user import create, get

@app.route('/users', methods=['POST'])
def create__():
    body = request.json
    create(body)
    return jsonify({}), 201

@app.route('/users', methods=['GET'])
def get__():
    user = get(request.args)
    return jsonify(user), 201