# MA BUDGIE

- Track cashflow
- Ooh and ahh at charts of cashflow
- Modify cashflow ~~(code not required, just me brain)~~ u can use code for dis now! :scream:

Python + PSQL + Pandas; Using the classic matplotlib with psycopg2.

### Installation

Dependencies: python2, virtualenv, the stuff in requirements.txt. Also a postgres DB called budget.

```bash
$ source ENV/bin/activate
$ pip install -r requirements.txt
```

### Usage

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
$ python analyze/monthly.py --category <potato>  # to see line chart of expenses for a category
```

Update recurring expenses:

Step 1. Copy data.yml.example to data.yml and modify its contents.

Step 2: (`--fo-real` to modify budget `budget` instead of `test_budget`)
```bash
$ python manipulate/update.py --fo-real

```

### TO DO

- handle CLI category names with spaces
- handle subcategories within categories
- add pgdump instructos to skirt disaster
- handle analyzing income per category/month

#### analyze/category/py
- be smarter about pie graph labels not overlapping

#### analyze/monthly.py
- crashes on 0 and >1 category arguments
- crashes on nonexistent categories
- accept --omit and --only like in categories.py
- enter 0 (instead of stopping the line) in months with no entries

#### Wild ambitions
- receipt OCR (date, amount)
