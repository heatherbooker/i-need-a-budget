import psycopg2 as psy


# Create db (must be in autocommit mode)
conn = psy.connect(dbname='postgres')
conn.autocommit = True
cur = conn.cursor()

cur.execute('DROP DATABASE IF EXISTS test_budget')
cur.execute('CREATE DATABASE test_budget')

conn.close()


# Create schema
conn = psy.connect(dbname='test_budget')
cur = conn.cursor()

createtablesql = """
CREATE TABLE IF NOT EXISTS {name} (
  id SERIAL PRIMARY KEY,
  date DATE NOT NULL DEFAULT CURRENT_DATE,
  amount NUMERIC(2) NOT NULL,
  category VARCHAR NOT NULL,
  subcategory VARCHAR,
  details VARCHAR
)
"""

cur.execute(createtablesql.format(name='expenses'))
cur.execute(createtablesql.format(name='income'))

conn.commit()
conn.close()

