import sqlite3


def validate(username, password):
    conn = sqlite3.connect("travel_expenses.db")
    cur = conn.cursor()

    sql = "SELECT username, password FROM members WHERE username = ? AND password = ?"
    cur.execute(sql, (username, password))
    username = cur.fetchone()
    conn.close()

    if not username:
        return False
    return True


def show_trips_data(sql, current_user):  # query db & return records
    conn = sqlite3.connect("travel_expenses.db")
    cur = conn.cursor()
    cur.execute(sql, (current_user,))
    allRows = cur.fetchall()
    cur.close()
    conn.close()
    return allRows


def add_new_trip(data):  # add record to students table
    conn = sqlite3.connect("travel_expenses.db")
    cur = conn.cursor()
    sql = "INSERT INTO trips VALUES(?, ?, ?, ?, ?, ?)"
    cur.execute(
        sql,
        data,
    )
    conn.commit()
    conn.close()
