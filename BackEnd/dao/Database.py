import pyodbc


def ConnectDb(TableName):
    connection = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL server};'
        'SERVER=185.83.183.254,11201;'
        'DATABASE=school;'
        'UID=sa;'
        'PWD=111@a;')
    cursor = connection.cursor()
    cursor.execute('''SELECT * FROM ''' + str(TableName))
    rows = cursor.fetchall()
    connection.close()
    return rows
