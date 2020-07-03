import psycopg2
import matplotlib.pyplot as plt 
from matplotlib import cm
import numpy as np
import sys
import argparse

def parse():
    parser = argparse.ArgumentParser(description='analyze spending by category')
    exclusive = parser.add_mutually_exclusive_group()
    exclusive.add_argument('--omit', action='append', nargs='*', help='categories or subcategories to omit from analysis')
    exclusive.add_argument('--only', action='append', nargs='*', help='only analyze the specified categories or subcategories')
    return parser.parse_args()

def omit(from_list, args):
    if args.omit:
        print('Omitting categories: {}.'.format(args.omit[0]))
        return tuple(set(from_list).difference(set(args.omit[0])))
    elif args.only:
        print('Only analyzing categories: {}.'.format(args.only[0]))
        return tuple(set(from_list).intersection(set(args.only[0])))
    else:
        return from_list

def get_data(args):
    conn = psycopg2.connect('dbname=budget')
    cur = conn.cursor()

    cur.execute('SELECT DISTINCT category FROM expenses')
    categories = cur.fetchall()
    categories = map((lambda tupl: tupl[0]), categories)
    categories = omit(categories, args)

    amounts = []
    for category in categories:
      cur.execute('SELECT SUM(amount) FROM expenses WHERE category = %s', (category,))
      total = cur.fetchone()
      amounts.append(total)

    conn.close()

    return [categories, amounts]

def show_me_the_money(categories, amounts):
    colors = cm.tab20b(np.linspace(0, 1, len(categories)))
    plt.pie(amounts, labels=categories, colors=colors)
    plt.axis('equal')
    plt.show()

def gogogadgetbuget():
    args = parse()
    [categories, amounts] = get_data(args)
    show_me_the_money(categories, amounts)

gogogadgetbuget()
