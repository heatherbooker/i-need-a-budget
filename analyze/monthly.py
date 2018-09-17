import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

conn = psycopg2.connect('dbname=budget')

df = pd.read_sql("SELECT date, amount from expenses",
        conn, parse_dates=['date'], index_col='date')


# Sum by month and plot
df.resample("M").sum().plot()
plt.show()

