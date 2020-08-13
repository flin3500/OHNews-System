from db.redis_db import pool
import redis

class RedisNewsDao:

    def insert(self, id, title, username, type, content, if_top, create_time):
        conn = redis.Redis(connection_pool=pool)
        try:
            conn.hmset(id,{
                "title":title,
                "author":username,
                "type":type,
                "content":content,
                "if_top":if_top,
                "create_time":create_time
            })
            if if_top == 0:
                conn.expire(id, 24*60*60)
        except Exception as e:
            print(e)
        finally:
            del conn

    def delete(self, id):
        conn = redis.Redis(connection_pool=pool)
        try:
            conn.delete(id)
        except Exception as e:
            print(e)
        finally:
            del conn
