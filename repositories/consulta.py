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
