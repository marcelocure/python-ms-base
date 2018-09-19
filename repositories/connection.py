#sudo apt-get install libmysqlclient-dev
import MySQLdb # para o MySQL
from config import host, username, password, database

def get_connection():
    conn = MySQLdb.connect(host=host, user=username, passwd=password, db=database)
    conn.select_db(database)
    return conn
