# -*- coding: utf-8 -*-

from connection import get_connection
from models.consulta import Consulta
from utils.encoding_utils import decode

def build_consulta(data):
    return Consulta(id=data[0], type=data[1], date=data[6], goal=decode(data[2]), height=data[3],
                    weight=data[4], paciente=data[5], strategy=decode(data[7])).__dict__

def buscar(query):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('select * from app_consulta' + query)
    consultas = map(build_consulta, cursor.fetchall())
    conn.close()
    return consultas

def criar(consulta):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "insert into app_consulta(type, date, goal, height, weight, paciente_id, strategy) \
    values ('{0}', CURDATE(), '{1}', '{2}', '{3}', '{4}', '{5}')".format(consulta.type, consulta.goal, consulta.height, consulta.weight, consulta.paciente, consulta.strategy)
    cursor.execute(sql)
    conn.commit()
    conn.close()
    return {}
