from db.mysql_db import pool

class TypeDao:
    def search_list(self):
        try:
            conn = pool.connection()
            cursor = conn.cursor()
            sql = "SELECT id, type FROM news_type ORDER BY id;"
            cursor.execute(sql)
            result = cursor.fetchall()
            cursor.close()
            conn.close()
            return result
        except Exception as e:
            print(e)
