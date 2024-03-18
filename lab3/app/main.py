import datetime
import time
import random

from sqlalchemy import create_engine
from sqlalchemy import text

db_name = 'database'
db_user = 'postgres'
db_pass = 'secret'
db_host = 'localhost'
db_port = '5432'

# Connecto to the database
db_string = 'postgresql://{}:{}@{}:{}/{}'.format(db_user, db_pass, db_host, db_port, db_name)
db = create_engine(db_string)


def add_new_row(n):
    # Insert a new number into the 'numbers' table.
    with db.engine.connect() as conn:
        conn.execute(text(f"""INSERT INTO numbers (number, clock) VALUES ({str(n)}, TIMESTAMP '{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=2)))}');"""))
        conn.commit()


def get_last_row():
    # Retrieve the last number inserted inside the 'numbers'
    query = "" + \
            "SELECT number " + \
            "FROM numbers " + \
            "WHERE clock >= (SELECT max(clock) FROM numbers)" + \
            "LIMIT 1"

    with db.engine.connect() as conn:
        result_set = conn.execute(text(query))
        conn.commit()
        for (r) in result_set:
            return r[0]


def get_all_row():
    query = """SELECT * From numbers"""

    with db.engine.connect() as conn:
        result_set = conn.execute(text(query))
        conn.commit()
        l = []
        for (r) in result_set:
            l.append(r)
        return l


if __name__ == '__main__':
    print('Application started')

    while True:
        # add_new_row(random.randint(1, 100000))
        # print('The last value insterted is: {}'.format(get_last_row()))
        for i in get_all_row():
            print(i)
        time.sleep(5)
        print('---------------------------------------------------------')
