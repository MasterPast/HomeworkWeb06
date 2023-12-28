# Знайти які курси читає певний викладач.
import sqlite3
from query_funcs import choose, sql_choose_teacher, sql_query_5


def execute_query(sql: str, teacher: str) -> list:

    with sqlite3.connect('univer_base.db') as con:
        cur = con.cursor()
        cur.execute(sql.format(teacher))

        return cur.fetchall()


teacher = choose(sql_choose_teacher)
print(f'Result of query >>> {execute_query(sql_query_5, teacher)}')
