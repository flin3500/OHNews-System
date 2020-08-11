import db.mysql_db


class UserDao:
    def login(self, username, password):
        try:
            conn = db.mysql_db.pool.get_connection()
            cursor = conn.cursor
            sql = "SELECT COUNT(*) FROM news_user WHERE username=%s AND " \
                  "AES_DECRYPT(UNHEX(password), 'HelloWorld')=%s;"
            cursor.execute(sql, (username, password))
            count = cursor.fetchone()[0]
            cursor.close()
            conn.close()
            return True if count == 1 else False
        except Exception as e:
            print(e)

    def search_role(self, username):
        try:
            conn = db.mysql_db.pool.get_connection()
            cursor = conn.cursor
            sql = "SELECT r.role FROM news_user as u JOIN user_role as r ON " \
                  "u.role_id=r.id where u.username=%s;"
            cursor.execute(sql, (username,))
            role = cursor.fetchone()[0]
            cursor.close()
            conn.close()
            return role

        except Exception as e:
            print(e)
