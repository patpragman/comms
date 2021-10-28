# This file is where we'll process the SQL db for the app.
# Alex and Pat
# 10/2/21

import sqlite3
from config import DatabaseConfig as DBC


"""
This file defines several functions that manage database insertions, 
updates, clearing rows, query, etc.
"""


def execute_sql(sql: str, data: tuple) -> None:
    """

    :param sql: A string with the SQL statement
    :param data: a tuple with the data to pass into the db
    :return: nothing - it works or it doesn't
    """

    # connect to the database
    conn = sqlite3.connect(DBC.path)
    cur = conn.cursor()
    cur.execute(sql, data)
    conn.commit()
    conn.close()


def select_all_from(table: str, where: str = "") -> list:
    """

    :param table: this is the table you wish to
    :param where: string to add to add to the query
    :return: list of all the rows in the database
    """

    conn = sqlite3.connect(DBC.path)
    cur = conn.cursor()
    if where == "":
        cur.execute(DBC.select.format(table=table))
    else:
        cur.execute(DBC.select_where.format(table=table, where=where))

    rows = cur.fetchall() # get all the rows back from the DB
    return rows

def check_user(user: str) -> bool:
    conn = sqlite3.connect(DBC.path)
    cur = conn.cursor()
    cur.execute(DBC.user_exists.format(user=user))
    if cur.fetchone():
        return True
    else:
        return False

def update_password(user: str, newPassword: str):
    conn = sqlite3.connect(DBC.path)
    cur = conn.cursor()
    cur.execute(DBC.set_password.format(user=user, newPassword=newPassword))
    conn.commit()  #HAS TO RUN AFTER ANY UPDATE OR INSERT