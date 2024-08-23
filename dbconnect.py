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
    except psycopg2.OperationalError:
        print("Print cursor state invalid")
        cursor.close()
    else:
        print("Cusrsor opened")

    try:
        sql_query = f'SELECT * FROM Customer where {criteria} = {payload};'
        cursor.execute(sql_query)
    except psycopg2.OperationalError:
        print("SELECT statement failed")
    else:
        rows = cursor.fetchall()
        print(rows)
    finally:
        print("Cursor closed")
        cursor.close()


def db_connect(criteria, payload):
    global conn
    try:
        conn = psycopg2.connect(database="postgres",
                                user="postgres",
                                host='localhost',
                                password="Admin",
                                port=5432)

    except psycopg2.OperationalError:
        print("Data base connection error")
        conn = None
    except psycopg2.DatabaseError:
        print("Data base connection error")
        conn = None
    else:
        print("Database connected successfully")
        db_query(criteria, payload)
    finally:
        print("Data base closed")
        if conn is not None:
            conn.close()

