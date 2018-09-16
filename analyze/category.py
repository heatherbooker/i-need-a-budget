import psycopg2
import matplotlib.pyplot as plt 
from matplotlib import cm
import numpy as np
import sys

def omit(from_list):
    if len(sys.argv) > 1 and sys.argv[1] == '--omit':
        print('Omitting categories: {}.'.format(sys.argv[2:]))
        return tuple(set(from_list).difference(set(sys.argv[2:])))
    else:
        return from_list

# TALK TO DA DB
conn = psycopg2.connect('dbname=budget')
cur = conn.cursor()

cur.execute('SELECT DISTINCT category FROM expenses')
categories = cur.fetchall()
categories = map((lambda tupl: tupl[0]), categories)
categories = omit(categories)

amounts = []
for category in categories:
  cur.execute('SELECT SUM(amount) FROM expenses WHERE category = %s', (category,))
  total = cur.fetchone()
  amounts.append(total)

conn.close()


# SHOW ME THE MONEY (lol u so funny)
colors = cm.tab20b(np.linspace(0, 1, len(categories)))
plt.pie(amounts, labels=categories, colors=colors)
plt.axis('equal')
plt.show()

