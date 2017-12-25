import psycopg2
import matplotlib.pyplot as plt 
from matplotlib import cm
import numpy as np

# TALK TO DA DB
conn = psycopg2.connect('dbname=budget')
cur = conn.cursor()

cur.execute('SELECT DISTINCT category FROM expenses')
categories = cur.fetchall()
categories = map((lambda tupl: tupl[0]), categories)

amounts = []
for category in categories:
  cur.execute('SELECT SUM(amount) FROM expenses WHERE category = %s', (category,))
  total = cur.fetchone()
  amounts.append(total)

conn.close()


# SHOW ME THE MONEY (lol u so funny)
colors=cm.tab20b(np.linspace(0, 1, len(categories)))
plt.pie(amounts, labels=categories, colors=colors)
plt.axis('equal')
plt.show()

