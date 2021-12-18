#!/usr/bin/python3
# Lists all states from a database

if __name__ == "__main__":
    import MySQLdb
    from sys import argv, exit

    if len(argv) != 5:
        print("Usage: ./2.py <username> <password> <database> <search>")
        exit(1)

    usr = argv[1]
    pwd = argv[2]
    dbe = argv[3]
    ser = argv[4]

    try:
        database = MySQLdb.Connect(user=usr, passwd=pwd, db=dbe, port=3306)
    except Exception as err:
        print(err)
        exit(1)
    cursor = database.cursor()
    cursor.execute("""
        SELECT * FROM states WHERE states.name LIKE '%{:s}%'
        ORDER BY states.id ASC
    """.format(ser))
    for row in cursor.fetchall():
        if row[1][0] == 'N':
            print(row)
    cursor.close()
    database.close()
