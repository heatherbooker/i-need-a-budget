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

sharedcolumns = "id serial PRIMARY KEY, date DATE NOT NULL DEFAULT CURRENT_DATE, amount NUMERIC(2) NOT NULL, category TEXT NOT NULL"
createtablesql = "CREATE TABLE IF NOT EXISTS {name} ({cols})".format(name='{name}', cols=sharedcolumns + '{cols}')

cur.execute(createtablesql.format(name='expenses', cols=', subcategory TEXT, details TEXT'))
cur.execute(createtablesql.format(name='income', cols=''))

conn.commit()
conn.close()

