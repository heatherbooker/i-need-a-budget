import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
import sys
import argparse

conn = psycopg2.connect('dbname=budget')

def parse():
    parser = argparse.ArgumentParser(description='analyze spending by month')
    parser.add_argument('--category', nargs='*', help='specify which categories to analyze')
    return parser.parse_args()

def get_df(args):
    if args.category:
        categories = tuple(map((lambda x: x.replace('_', ' ')), args.category))
        return pd.read_sql("SELECT date, amount FROM expenses WHERE category in (%s)", conn, params=categories, parse_dates=['date'], index_col='date')
    else:
        return pd.read_sql("SELECT date, amount FROM expenses",
                    conn, parse_dates=['date'], index_col='date')

args = parse()
df = get_df(args)

# Sum by month and plot
df.resample("M").sum().plot()
plt.show()

