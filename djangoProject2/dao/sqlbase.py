import pyodbc

class sqlbase():
    def getConnection(self):
        connection=pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=185.83.183.254,11201;DATABASE=school;UID=sa;PWD=111@a')
        cursor=connection.cursor()
        return connection,cursor


