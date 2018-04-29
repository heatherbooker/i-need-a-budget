import calendar
from datetime import date
import psycopg2

conn = psycopg2.connect('dbname=testbudget')
cur = conn.cursor()

year = date.today().year
month = input('What month (1-12) in {0} do you want to update recurring expenses for?'.format(year))
last_day = calendar.monthrange(2018, int(month))[1]

recurring = {
  'category': ('subcat', 'subcategory', 'subcategorino', 'lastbeans'),
  'othercategory': ('typeofthing'),
  'thirdcat': ('abcdef'),
  'somecateg': ('moreotherthing')
}
categories = tuple(recurring.keys())

cur.execute("SELECT date, subcategory FROM expenses WHERE category in {3} and date between '{0}-{1}-01' and '{0}-{1}-{2}'".format(year, month, last_day, categories))
bills = cur.fetchall()

print('Bills for {0}-{1}:'.format(year, month))
print(bills)

cur.execute("INSERT INTO expenses (date, amount, category, subcategory) VALUES ('{}-{}-01', 725, 'bills', 'rent')".format(year, month))
