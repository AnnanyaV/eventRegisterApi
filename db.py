from decimal import Decimal
import pymysql
from flask import jsonify
def query(querystr, return_json=True):
    connection= pymysql.connect(
                                host='database-2.cs5u2lp6velk.us-east-2.rds.amazonaws.com',
                                user='root',
                                password='annanya1234',
                                db='flaskevent',
        cursorclass=pymysql.cursors.DictCursor

    )
    connection.begin()
    cursor=connection.cursor()
    cursor.execute(querystr)
    result= encode(cursor.fetchall())
    connection.commit()
    cursor.close()
    connection.close()
    if return_json:
        return jsonify(result)
    else:
        return result

def encode(data):
    for row in data:
        for key,value in row.items():
            if isinstance(value, Decimal):
                row[key]=str(value)
    return data