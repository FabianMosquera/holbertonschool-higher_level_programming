#!/usr/bin/python3
"""script that lists all states with a name starting with N"""
import MySQLdb
import sys


def get_states_n():
    """ Arguments argv to connect to database
    argv[1]: mysql username
    argv[2]: mysql password
    argv[3]: database name
    """
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id")
    # fetchall is necesary for that the print show as a tuple
    var = cur.fetchall()
    for i in var:
        print(i)
    cur.close()
    db.close()

if __name__ == "__main__":
    get_states_n()
