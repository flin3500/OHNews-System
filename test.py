import mysql.connector.pooling

__config = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "mysqllin",
    "database": "galaxy"
}


pool = mysql.connector.pooling.MySQLConnectionPool(
    **__config,
    pool_name="aa",
    pool_size=10
)
