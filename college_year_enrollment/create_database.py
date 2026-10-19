import mysql.connector


db_conf= {"host":"localhost",
           "user":"root",
           "passwd":"",
           "database":"sessiondb"}


def get_database_connection():
    myDB = mysql.connector.connect( host = db_conf['host'],
                                    user = db_conf['user'],
                                    passwd = db_conf['passwd'],
                                    database = db_conf['database'])
    return myDB


def check_table_existance(dbConn, tableName):
    dbCur = dbConn.cursor()
    dbCur.execute("SELECT COUNT(*) FROM sessiondb.tables WHERE table_name = '{0}'".format(tableName.replace("\'", "\'\'")))
    
    if dbCur.fetchone()[0] != 1:
        create_table(dbConn)
    dbCur.close()


def create_table(dbConn):
    myCursor = dbConn.cursor()
    sql = """CREATE TABLE session (
                session_id INT UNIQUE AUTO_INCREMENT,
                data VARCHAR(255))"""
    myCursor.execute(sql)
    myCursor.close()


dbConnection = get_database_connection()
# check_table_existance(dbConnection, 'session')
create_table(dbConnection)
dbConnection.close()


