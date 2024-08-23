import psycopg2
from psycopg2 import OperationalError, errorcodes, errors

conn = None

def db_query(criteria, payload):
    global conn

    try:
        if conn is not None:
            # declare a cursor object from the connection
            cursor = conn.cursor()
            # print ("cursor object:", cursor, "\n")
    except psycopg2.OperationalError as operr1:
        print("Print cursor state invalid")
        msg = f'Print cursor state invalid {operr1}'
    else:
        print("Cusrsor opened")

    try:
        sql_query = f'SELECT * FROM Customer where {criteria} = {payload};'
        cursor.execute(sql_query)
    except psycopg2.OperationalError as operr2:
        print("SELECT statement failed")
        msg = f'SELECT statement failed {operr2}'
    else:
        rows = cursor.fetchall()
        print(rows)
        if cursor.rowcount() != 0:
            msg = rows
        else:
            msg = f'Record not found'

    finally:
        print("Cursor closed")
        cursor.close()

    return msg



def db_connect(criteria, payload):
    global conn
    try:
        conn = psycopg2.connect(database="postgres",
                                user="postgres",
                                host='localhost',
                                password="Admin",
                                port=5432)

    except psycopg2.OperationalError as operr3:
        print("Data base connection error")
        msg = f'Data base connection error {operr3}'
        conn = None
    except psycopg2.DatabaseError as dberr:
        print("Data base connection error")
        msg = f'Data base connection error {dberr}'
        conn = None
    else:
        print("Database connected successfully")
        msg = db_query(criteria, payload)
    finally:
        print("Data base closed")
        if conn is not None:
            conn.close()

        return msg


