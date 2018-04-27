from psycopg2 import pool

# TALK TO DA DB
db = pool.SimpleConnectionPool(1, 10, dbname='postgres')

conn = db.getconn()
conn.autocommit = True # Must be in autocommit to create db
cur = conn.cursor()

cur.execute('DROP DATABASE IF EXISTS test_budget')
cur.execute('CREATE DATABASE test_budget')

db.putconn(conn)

conn = db.getconn()
conn.autocommit = False

cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS expenses (date DATE NOT NULL DEFAULT CURRENT_DATE)")

conn.commit()
conn.close()

