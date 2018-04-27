# goal: easily add recurring expenses
# interface: cli lists expenses to be added for review
# user accepts or edits
# on accept, expenses are added to db

recurring = (
    ('categroy', 1, 'subcat'),
    ('type', 1, 'stuff')
)

import sys, tempfile, os
from subprocess import call

while True:
    print recurring
    confirm = raw_input('Would you like to add all of these expenses to the db?')
    if confirm.lower() in ('y', 'yes'):
        break
    else:
        with tempfile.mkstemp(suffix=".tmp") as tf:
            formattedrecurring = map(lambda tup: '{0}'.format(tup), recurring)
            tf.write('\n'.join(formattedrecurring))
            tf.flush()
            call(['vim', tf.name])

            tf.seek(0)
            editedrecurring = tf.read()
            print(editedrecurring.decode('utf-8'))
            break
#insertall()
