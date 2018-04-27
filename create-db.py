import psycopg2

# TALK TO DA DB
conn = psycopg2.connect(dbname='postgres')
conn.autocommit = True # Commit the changes we make
cur = conn.cursor()

# create or remove?
while True:
    create_or_drop = raw_input('create db or drop db?')
    if create_or_drop in ('c', 'create'):
        cur.execute('CREATE DATABASE IF NOT EXISTS test_budget')
        conn.autocommit = False
        cur.execute("CREATE TABLE IF NOT EXISTS expenses (date DATE NOT NULL DEFAULT 'today')")
        break
    elif create_or_drop in ('d', 'drop'):
        cur.execute('DROP DATABASE test_budget')
        break
    else:
        print 'nah son, try "create" or "drop"'

conn.close()

