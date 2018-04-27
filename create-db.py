import psycopg2

# TALK TO DA DB
conn = psycopg2.connect(dbname='postgres')
conn.autocommit = True # Must be in autocommit to create db
autocommitcur = conn.cursor()

autocommitcur.execute('DROP DATABASE IF EXISTS test_budget')
autocommitcur.execute('CREATE DATABASE test_budget')
conn.autocommit = False

cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS expenses (date DATE NOT NULL DEFAULT CURRENT_DATE)")

conn.commit()
conn.close()

