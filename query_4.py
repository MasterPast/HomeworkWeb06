# Знайти середній бал на потоці (по всій таблиці оцінок).
import sqlite3
from query_funcs import sql_query_4


def execute_query(sql: str) -> list:

    with sqlite3.connect('univer_base.db') as con:
        cur = con.cursor()
        cur.execute(sql)

        return cur.fetchall()


print(f'Result of query >>> {execute_query(sql_query_4)[0][0]}')
