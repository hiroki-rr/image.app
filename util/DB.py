import pymysql

class DB:
    def getConnection():
        try:
            conn = pymysql.connect(
            host="localhost",
            db="imagesdb",
            user="root",
            password="Mysql1111!",
            charset="utf8",
            cursorclass=pymysql.cursors.DictCursor
        )
            return conn
        except (ConnectionError):
            print("コネクションエラーです")
            conn.close()
