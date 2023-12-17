#!/usr/bin/python3
"""
script that takes in the name of a state as an argument and lists all
cities of that state, using the database hbtn_0e_4_usa
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
    sql_injects = ["TRUNCATE", "DELETE", ";"]
    if all(c not in s.argv[4] for c in sql_injects):
        cur.execute("SELECT cities.name, cities.id FROM cities JOIN states ON \
                states.id=cities.state_id WHERE states.name='{}' ORDER BY \
                cities.id ASC".format(s.argv[4]))
        query_res = cur.fetchall()
        length = len(query_res)
        for i, row in enumerate(query_res):
            if i < length - 1:
                print(row[0], end=", ")
            else:
                print(row[0])
    cur.close()
    conn.close()
