# -*- coding: utf-8 -*-
from connection import get_connection
from models.user import User

def create(user):
    conn = get_connection()
    cursor = conn.cursor()
    sql = 'insert into user (name, email_address, password, profile) values(%s, %s, %s)'
    params = (user.name, user.email_address, user.password, user.profile)
    cursor.execute(sql, params)
    conn.commit()
    conn.close()

def _build_user(data):
    return User(id=data[0], email_address=data[1], password= data[2], name=data[4], profile=data[3]).__dict__

def get(query):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute('select * from user' + query)
    user = map(_build_user, cursor.fetchall())
    conn.close()
    
    return user[0]
