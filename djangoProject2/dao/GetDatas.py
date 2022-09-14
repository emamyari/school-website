from djangoProject2.dao.sqlbase import sqlbase



def getFunFactData():
    # connect to database
    sqlBase = sqlbase()
    connection, cursor = sqlBase.getConnection()

    # Run command
    cursor.execute("select * from FunFacts")

    # get result
    rows = cursor.fetchall()
    # close con.
    cursor.close()
    connection.close()

    list = []
    for item in rows:
        a=(item[0], item[1], item[2])
        list.append(a)

    return list
