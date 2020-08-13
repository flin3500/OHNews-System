from db.mysql_db import pool


class UserDao:
    def login(self, username, password):
        try:
            conn = pool.connection()
            cursor = conn.cursor()
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
            conn = pool.connection()
            cursor = conn.cursor()
            sql = "SELECT r.role FROM news_user as u JOIN user_role as r ON " \
                  "u.role_id=r.id where u.username=%s;"
            cursor.execute(sql, (username,))
            role = cursor.fetchone()[0]
            cursor.close()
            conn.close()
            return role

        except Exception as e:
            print(e)

    def add_user(self, username, password, email, role_id):
        try:
            conn = pool.connection()
            cursor = conn.cursor()
            sql = "INSERT INTO news_user(username, password, email, role_id) " \
                  "VALUES(%s,HEX(AES_ENCRYPT(%s, 'HelloWorld')),%s,%s);"
            cursor.execute(sql, (username, password, email, role_id))
        except Exception as e:
            conn.rollback()
            print(e)
        else:
            conn.commit()
        finally:
            cursor.close()
            conn.close()


    def search_count_page(self):
        """
        Show how many pages users needs to show in page
        :return: show pages number
        """
        try:
            conn = pool.connection()
            cursor = conn.cursor()
            sql = "SELECT CEIL(COUNT(*)/5) FROM news_user;"
            cursor.execute(sql)
            count_page = cursor.fetchone()[0]
            cursor.close()
            conn.close()
            return count_page
        except Exception as e:
            print(e)


    def search_list(self, page):
        """
        Show all the users in the specified pages
        :param page: which page (int)
        :return: all users in the specified pages
        """
        try:
            conn = pool.connection()
            cursor = conn.cursor()
            sql = "SELECT u.id, u.username,r.role " \
                  "FROM news_user u JOIN user_role r " \
                  "ON u.role_id=r.id " \
                  "ORDER BY u.id " \
                  "LIMIT %s,%s"
            cursor.execute(sql, ((page - 1) * 5, 5))
            result = cursor.fetchall()
            cursor.close()
            conn.close()
            return result
        except Exception as e:
            print(e)

    def update_user(self, id, username, password, email, role_id):
        """
        Update user information
        :param id: which user
        :param username: new username
        :param password: new password
        :param email: new email
        :param role_id: new role_id
        :return: None
        """
        try:
            conn = pool.connection()
            cursor = conn.cursor()
            sql = "UPDATE news_user SET " \
                  "username=%s, " \
                  "password=HEX(AES_ENCRYPT(%s, 'HelloWorld')), " \
                  "email=%s, " \
                  "role_id=%s " \
                  "WHERE id=%s;"
            cursor.execute(sql, (username, password, email, role_id, id))
        except Exception as e:
            conn.rollback()
            print(e)
        else:
            conn.commit()
        finally:
            cursor.close()
            conn.close()


    def delete_user(self, id):
        """
        Delete user
        :param id: which user
        :return: None
        """
        try:
            conn = pool.connection()
            cursor = conn.cursor()
            sql = "DELETE FROM news_user WHERE id=%s;"
            cursor.execute(sql, (id,))
        except Exception as e:
            conn.rollback()
            print(e)
        else:
            conn.commit()
        finally:
            cursor.close()
            conn.close()

    def search_userid(self, username):
        try:
            conn = pool.connection()
            cursor = conn.cursor()
            sql = "SELECT id From news_user WHERE username=%s;"
            cursor.execute(sql, (username,))
            user_id = cursor.fetchone()[0]
            cursor.close()
            conn.close()
            return user_id
        except Exception as e:
            print(e)


