import pyodbc


def ConnectDb(TableName):
    connection = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL server};'
        'SERVER=.;'
        'DATABASE=school;'
        'UID=sa;'
        'PWD=111;')
    cursor = connection.cursor()
    cursor.execute('''SELECT * FROM ''' + str(TableName))
    rows = cursor.fetchall()
    connection.close()
    return rows
