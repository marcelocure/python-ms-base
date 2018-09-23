# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from flask import current_app as app, jsonify, request
from business.consulta import consulta
from utils.query_builder import build as build_query

@app.route('/consultas', methods=['GET'])
def get_consultas():
    args = request.args
    query = build_query(args.to_dict())
    consulta(query)
    return consulta(query)
