import pymysql
from util.DB import DB

class dbConnect:
    def addImage(filename):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "INSERT INTO images (img_path) VALUES (%s);"
            cur.execute(sql, (filename))
            conn.commit()
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()

    def getImage():
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT img_path FROM images;"
            cur.execute(sql)
            img_path = cur.fetchone()
            return img_path
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()
