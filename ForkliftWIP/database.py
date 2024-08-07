import sqlite3 as db


def connect_to_database():
    return db.connect("trucks.sqlite")


def fetch_all_data(make):
    con = connect_to_database()
    try:
        cur = con.cursor()
        cur.execute(f"SELECT * FROM {make}")
        return cur.fetchall()
    except db.Error as e:
        raise e
    finally:
        cur.close()
        con.close()

'''
import sqlite3 as db

def connect_to_database():
    return db.connect("trucks.sqlite")

def fetch_all_data(brand):
    brand = brand.lower()  # Ensure the brand is in lowercase
    con = connect_to_database()
    try:
        cur = con.cursor()
        cur.execute(f"SELECT * FROM {brand}")
        return cur.fetchall()
    except db.Error as e:
        raise e
    finally:
        cur.close()
        con.close()
'''