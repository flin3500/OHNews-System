from db.mysql_db import pool


class NewsDao:

    def search_unreview_list(self, page):
        try:
            conn = pool.connection()
            cursor = conn.cursor()
            sql = "SELECT n.id,n.title,t.type,u.username " \
                  "FROM news as n JOIN news_type as t ON n.type_id=t.id " \
                  "JOIN news_user u ON n.editor_id=u.id " \
                  "WHERE n.status=%s " \
                  "ORDER BY n.create_time DESC " \
                  "LIMIT %s,%s"
            cursor.execute(sql, ("Reviewing", (page - 1) * 5, 5))
            result = cursor.fetchall()
            cursor.close()
            conn.close()
            return result
        except Exception as e:
            print(e)

    def search_unreview_count_page(self):
        try:
            conn = pool.connection()
            cursor = conn.cursor()
            sql = "SELECT CEIL(COUNT(*)/5) FROM news WHERE status=%s;"
            cursor.execute(sql, ("Reviewing",))
            count_page = cursor.fetchone()[0]
            cursor.close()
            conn.close()
            return count_page
        except Exception as e:
            print(e)

    def review_news(self, id):
        try:
            conn = pool.connection()
            cursor = conn.cursor()
            sql = "UPDATE news SET status=%s WHERE id=%s;"
            cursor.execute(sql, ("POST", id))
        except Exception as e:
            conn.rollback()
            print(e)
        else:
            conn.commit()
        finally:
            cursor.close()
            conn.close()

    def search_list(self, page):
        try:
            conn = pool.connection()
            cursor = conn.cursor()
            sql = "SELECT n.id,n.title,t.type,u.username " \
                  "FROM news as n JOIN news_type as t ON n.type_id=t.id " \
                  "JOIN news_user u ON n.editor_id=u.id " \
                  "ORDER BY n.create_time DESC " \
                  "LIMIT %s,%s"
            cursor.execute(sql, ((page - 1) * 5, 5))
            result = cursor.fetchall()
            cursor.close()
            conn.close()
            return result
        except Exception as e:
            print(e)

    def search_count_page(self):
        try:
            conn = pool.connection()
            cursor = conn.cursor()
            sql = "SELECT CEIL(COUNT(*)/5) FROM news;"
            cursor.execute(sql)
            count_page = cursor.fetchone()[0]
            cursor.close()
            conn.close()
            return count_page
        except Exception as e:
            print(e)

    def delete_news(self, id):
        try:
            conn = pool.connection()
            cursor = conn.cursor()
            sql = "DELETE FROM news WHERE id=%s;"
            cursor.execute(sql, (id,))
        except Exception as e:
            conn.rollback()
            print(e)
        else:
            conn.commit()
        finally:
            cursor.close()
            conn.close()

    def add_news(self, title, editor_id, type_id, content_id, if_top):
        try:
            conn = pool.connection()
            cursor = conn.cursor()
            sql = "INSERT INTO news(title,editor_id,type_id,content_id,if_top,status) " \
                  "VALUES(%s,%s,%s,%s,%s,%s);"
            cursor.execute(sql, (title, editor_id, type_id, content_id, if_top, "Reviewing"))
        except Exception as e:
            conn.rollback()
            print(e)
        else:
            conn.commit()
        finally:
            cursor.close()
            conn.close()

