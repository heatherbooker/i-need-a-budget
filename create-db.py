import psycopg2 as psy

conn = psy.connect('dbname=test_budget')
cur = conn.cursor()

operation = raw_input('create (c) or delete (d)?')

if operation == 'c':
  print('creating')
  cur.execute(
    """
    CREATE TABLE IF NOT EXISTS expenses (
      id SERIAL PRIMARY KEY,
      date DATE NOT NULL DEFAULT 'today',
      amount INT NOT NULL,
      category VARCHAR NOT NULL,
      subcategory VARCHAR,
      details VARCHAR
    )
    """
  )
  cur.execute(
    """
    CREATE TABLE IF NOT EXISTS income (
      id SERIAL PRIMARY KEY,
      date DATE NOT NULL DEFAULT 'today',
      amount INT NOT NULL,
      category VARCHAR(60) NOT NULL DEFAULT 'salary',
      subcategory VARCHAR(60) DEFAULT NULL,
      details VARCHAR(140) DEFAULT NULL
    )
    """
  )
  conn.commit()
elif operation == 'd':
  print('dropping')
  cur.execute(
    """
    DROP TABLE IF EXISTS expenses
    """,
    """
    DROP TABLE IF EXISTS income
    """
  )
  conn.commit()
else:
  print('input not recognized, you typed:')
  print(operation)


