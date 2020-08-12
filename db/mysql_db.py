import pymysql
from DBUtils.PooledDB import PooledDB

'''1. use pymysql'''
__config = PooledDB(
    creator=pymysql,
    maxconnections=10,
    mincached=2,
    maxcached=5,
    maxshared=1,
    blocking=True,
    maxusage=None,
    setsession=[],
    ping=2,
    host='127.0.0.1',
    port=3306,
    user='root',
    password='mysqllin',
    database='galaxy',
    charset='utf8'
)

pool = __config

'''2. use mysql.connector'''
# import mysql.connector.pooling
# __config = {
#     "host": "localhost",
#     "port": 3306,
#     "user": "root",
#     "password": "mysqllin",
#     "database": "galaxy",
#     "auth_plugin": "mysql_native_password"
# }
#
# try:
#     pool = mysql.connector.pooling.MySQLConnectionPool(
#         **__config,
#         pool_name="aa",
#         pool_size=10
#     )
# except Exception as e:
#     print(e)
