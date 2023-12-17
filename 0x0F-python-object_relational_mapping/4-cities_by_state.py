#!/usr/bin/python3
"""
script that lists all cities from the database hbtn_0e_4_usa
"""
if __name__ == "__main__":
    import MySQLdb
    import sys as s

    conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=s.argv[1],
            passwd=s.argv[2],
            db=s.argv[3],
            charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities \
            JOIN states ON states.id=cities.state_id ORDER BY cities.id ASC")
    query_res = cur.fetchall()
    for row in query_res:
        print(row)
    cur.close()
    conn.close()
