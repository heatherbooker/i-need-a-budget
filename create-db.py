import psycopg2


# Create db (must be in autocommit mode)
conn = psycopg2.connect(dbname='postgres')
conn.autocommit = True
cur = conn.cursor()

cur.execute('DROP DATABASE IF EXISTS test_budget')
cur.execute('CREATE DATABASE test_budget')

conn.close()


# Create schema
conn = psycopg2.connect(dbname='test_budget')
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS expenses (date DATE NOT NULL DEFAULT CURRENT_DATE)")

conn.commit()
conn.close()

