#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys


def get_names_save():
    """ Arguments argv to connect to database
    argv[1]: mysql username
    argv[2]: mysql password
    argv[3]: database name
    argv[4]: state name searched
    """
    db = MySQLdb.connect(host="localhost",
                        port=3306,
                        user=sys.argv[1],
                        passwd=sys.argv[2],
                        db=sys.argv[3])

    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities\
                JOIN states ON cities.state_id = states.id\
                ORDER BY cities.id ASC")
    # fetchall is necesary for that the print show as a tuple
    var = cur.fetchall()
    for i in var:
        print(i)
    cur.close()
    db.close()

if __name__ == "__main__":
    get_names_save()
