# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from flask import current_app as app, jsonify, request
from repositories.consulta import buscar, criar
from utils.query_builder import build as build_query
from models.consulta import Consulta
import datetime

@app.route('/consultas', methods=['GET'])
def get_consultas():
    args = request.args
    query = build_query(args.to_dict())
    return jsonify(buscar(query))

@app.route('/consultas', methods=['POST'])
def create_consultas():
    body = request.json
    consulta = Consulta(type=body['type'], goal=body['goal'], height=body['height'], weight=body['weight'], paciente=body['links']['paciente'], strategy=body['strategy'])
    print consulta.__dict__
    criar(consulta)
    return 'ok', 201
