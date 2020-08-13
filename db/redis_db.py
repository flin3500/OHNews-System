import redis

try:
	pool = redis.ConnectionPool(
        host = "127.0.0.1",
		port = 6379,
		password = "redislin",
		db = 1,
		max_connections=20
	)
except Exception as e:
	print(e)