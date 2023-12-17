#!/usr/bin/python3
"""
script that takes in an argument and displays all values in the states table of
hbtn_0e_0_usa where name matches the argument
"""
if __name__ == "__main__":
    import sys as s
    import MySQLdb

    conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=s.argv[1],
            passwd=s.argv[2],
            db=s.argv[3],
            charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE\
            name='{}' ORDER BY id ASC".format(s.argv[4]))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
