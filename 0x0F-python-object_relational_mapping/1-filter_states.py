#!/usr/bin/python3
"""
script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
"""

if __name__ == "__main__":
    import sys as s
    import MySQLdb

    conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=s.argv[1],
            passwd=s.argv[2],
            db=s.argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    query_response = cur.fetchall()
    for row in query_response:
        print(row)
    cur.close()
    conn.close()
