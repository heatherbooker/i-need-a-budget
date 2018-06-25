# MA BUDGIE

- Track cashflow
- Ooh and ahh at charts of cashflow
- Modify cashflow ~~(code not required, just me brain)~~ u can use code for dis now! :scream:

Python + PSQL; Using the classic matplotlib with psycopg2.

Dependencies: python2, virtualenv, the stuff in requirements.txt.

LMK via issue if you see anything that itches for improvement; I am just beginning to explore python + psql + matplotlib!

### Installation

```bash
$ source ENV/bin/activate
$ pip install -r requirements.txt
```

#### Usage

First always activate virtual env:

```bash
$ source ENV/bin/activate
```

Create db for testing (called test_budget) and schema:
```bash
$ python manipulate/create-db.py
```

Analyze data:
```bash
$ python analyze/category.py  # to see pie chart of expenses by category
$ python analyze/pipeline.py  # to see pie chart of income v. expenses
```

Update recurring expenses:

Step 1. Copy data.yml.example to data.yml and modify its contents.

Step 2: (`--fo-real` to modify budget `budget` instead of `test_budget`)
```bash
$ python manipulate/update.py --fo-real

```
