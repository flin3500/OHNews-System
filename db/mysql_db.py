import mysql.connector.pooling

__config = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "mysqllin",
    "database": "galaxy",
    "auth_plugin": "mysql_native_password"
}

try:
    pool = mysql.connector.pooling.MySQLConnectionPool(
        **__config,
        pool_name="aa",
        pool_size=10
    )
except Exception as e:
    print(e)
