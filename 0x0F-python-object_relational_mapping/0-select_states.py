#!/usr/bin/python3
# script that lists all states from the database hbtn_0e_0_usa
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
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
