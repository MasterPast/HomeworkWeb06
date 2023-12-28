# Знайти список студентів у певній групі.
import sqlite3
from query_funcs import choose, sql_choose_group, sql_query_6


def execute_query(sql: str, group: str) -> list:

    with sqlite3.connect('univer_base.db') as con:
        cur = con.cursor()
        cur.execute(sql.format(group))

        return cur.fetchall()


group = choose(sql_choose_group)
print(f'Result of query >>> {execute_query(sql_query_6, group)}')
