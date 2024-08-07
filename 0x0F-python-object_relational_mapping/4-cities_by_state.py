#!/usr/bin/python3
""" selects states that start with N from the database htbn_0e_0_usa """

if __name__ == "__main__":
    import MySQLdb
    import sys

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
        user=username,
        password=password,
        database=database,
        host='localhost',
        port=3306
        )
    c = db.cursor()
    query = """SELECT cities.id AS city_id, cities.name AS city_name,
        states.name AS state_name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC;"""
    c.execute(query)
    result = c.fetchall()
    for row in result:
        print(row)
