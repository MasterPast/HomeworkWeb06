# Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
import sqlite3
from query_funcs import sql_query_1

def execute_query(sql: str) -> list:

    with sqlite3.connect('univer_base.db') as con:
        cur = con.cursor()
        cur.execute(sql)

        return cur.fetchall()


print(f'Result of query >>>{execute_query(sql_query_1)}')

