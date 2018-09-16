import calendar
from datetime import date
import psycopg2 as psy
import sys
import yaml

BASE_SQL = """
  SELECT subcategory, date, amount
  FROM expenses
  WHERE category = '{3}'
  AND subcategory in %s
  AND date between '{0}-{1}-01' and '{0}-{1}-{2}'
"""

def connect_to_db():
  which_db = 'test_budget'
  if len(sys.argv) > 1 and sys.argv[1] == '--fo-real':
    which_db = 'budget'

  print('Using db: `{}`; use arg `--fo-real` to use `budget`.'.format(which_db))
  conn = psy.connect('dbname={}'.format(which_db))
  return conn


def get_dates():
  year = date.today().year

  month = 0
  while month not in range(1, 12):
      month = int(input('What month (1-12) in {0} do you want to update categories expenses for? (current month: {1})'.format(year, date.today().month)))

  last_day = str(calendar.monthrange(year, month)[1]).zfill(2)

  return { 'year': year, 'month': str(month).zfill(2), 'last_day': last_day }

def insert_recurring(categories, details, dates, cur):
  expenses_in_db = {}
  year = dates['year']
  month = dates['month']
  last_day = dates['last_day']

  for category in categories:
    sql = BASE_SQL.format(year, month, last_day, category)
    cur.execute(sql, (tuple(categories[category]),))
    for row in cur:
      expenses_in_db[row[0]] = row
    for subcat in categories[category]:
      if subcat in expenses_in_db:
        continue
      insert = raw_input('Would you like to insert for {0}?'.format(subcat))
      if insert.lower() in ('y', 'yes'):
        print('Inserting for {0}'.format(subcat))
        raw_day = details[subcat]['day']
        if raw_day == 'last_day':
            day = last_day
        else:
            day = str(raw_day).zfill(2)
        amount = details[subcat]['amount']
        cur.execute("INSERT INTO expenses (date, amount, category, subcategory) VALUES ('{}-{}-{}', {}, '{}', '{}')".format(year, month, day, amount, category, subcat))

def close_db(conn):
  conn.commit()
  conn.close()

with open('data.yml', 'r') as stream:
  info = yaml.load(stream)
  details = info['details']
  categories = info['categories']

  conn = connect_to_db()
  cur = conn.cursor()

  dates = get_dates()

  insert_recurring(categories, details, dates, cur)

  close_db(conn)
