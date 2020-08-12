from db.mysql_db import pool

class RoleDao:
    def search_list(self):
        try:
            conn = pool.connection()
            cursor = conn.cursor()
            sql = "SELECT id, role FROM user_role;"
            cursor.execute(sql)
            result = cursor.fetchall()
            cursor.close()
            conn.close()
            return result
        except Exception as e:
            print(e)