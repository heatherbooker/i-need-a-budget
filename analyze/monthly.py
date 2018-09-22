import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
import sys

conn = psycopg2.connect('dbname=budget')

def get_df():
    if len(sys.argv) > 1 and sys.argv[1] == '--category':
        args = tuple(map((lambda x: x.replace('_', ' ')), sys.argv[2:]))
        return pd.read_sql("SELECT date, amount FROM expenses WHERE category in (%s)", conn, params=args, parse_dates=['date'], index_col='date')
    else:
        return pd.read_sql("SELECT date, amount FROM expenses",
                    conn, parse_dates=['date'], index_col='date')


df = get_df()

# Sum by month and plot
df.resample("M").sum().plot()
plt.show()

