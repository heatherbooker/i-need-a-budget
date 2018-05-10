import calendar
from datetime import date
import psycopg2 as psy
import sys

which_db = 'test_budget'
if len(sys.argv) > 1 and sys.argv[1] == '--fo-real':
  which_db = 'budget'

print('Using db: `{}`; use arg `--fo-real` to use `budget`.'.format(which_db))
conn = psy.connect('dbname={}'.format(which_db))
cur = conn.cursor()

year = date.today().year

month = 0
while month not in range(1, 12):
    month = int(input('What month (1-12) in {0} do you want to update categories expenses for? (current month: {1})'.format(year, date.today().month)))

last_day = calendar.monthrange(year, month)[1]

# TODO: put this in a separate file, not tracked by git
categories = {
  'category': ('subcat', 'subcat2', 'subcat3', 'subcat4'),
  'othercategory': ('subcat5',)
}
data = {
  'subcat': {
    'amount': 12,
    'day': 1
  },
  'subcat2': {
    'amount': 22,
    'day': 19
  },
  'subcat3': {
    'amount': 3,
    'day': 19
  },
  'subcat4': {
    'amount': 20,
    'day': 15
  },
  'subcat5': {
    'amount': 400000,
    'day': last_day
  }
}
expenses_in_db = {}

base_sql = """
  SELECT subcategory, date, amount
  FROM expenses
  WHERE category = '{3}'
  AND subcategory in %s
  AND date between '{0}-{1}-01' and '{0}-{1}-{2}'
"""

for category in categories:
  sql = base_sql.format(year, str(month).zfill(2), str(last_day).zfill(2), category)
  cur.execute(sql, (categories[category],))
  for row in cur:
    expenses_in_db[row[0]] = row
  for subcat in categories[category]:
    if subcat in expenses_in_db:
      continue
    insert = raw_input('Would you like to insert for {0}?'.format(subcat))
    if insert.lower() in ('y', 'yes'):
      cur.execute("INSERT INTO expenses (date, amount, category, subcategory) VALUES ('{}-{}-{}', {}, '{}', '{}')".format(year, month, str(data[subcat]['day']).zfill(2), data[subcat]['amount'], category, subcat))

conn.commit()
conn.close()
