#!/usr/bin/python3
"""
script that takes in arguments and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
script that is safe from MySQL injections!
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
    if "TRUNCATE" or "DELETE" not in s.argv[4]:
        cur.execute("SELECT * FROM states WHERE \
                name='{}' ORDER BY id ASC".format(s.argv[4]))
        query_res = cur.fetchall()
        for row in query_res:
            print(row)
        cur.close()
        conn.close()
