import psycopg2
import matplotlib.pyplot as plt 
from matplotlib import cm
import numpy as np

# TALK TO DA DB
conn = psycopg2.connect('dbname=budget')
cur = conn.cursor()

cur.execute('SELECT SUM(amount) FROM expenses')
expenses = cur.fetchone()[0]
cur.execute('SELECT SUM(amount) FROM income')
income = cur.fetchone()[0]

conn.close()


# SHOW ME THE MONEY (lol u so funny)
slices = 2
colors = cm.tab20b(np.linspace(0, 1, slices))
plt.pie([expenses, income], labels=['expenses', 'income'], colors=colors)
plt.axis('equal')
plt.show()

