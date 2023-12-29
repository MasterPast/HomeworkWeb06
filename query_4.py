# Знайти середній бал на потоці (по всій таблиці оцінок).
import sqlite3

sql_query_4 = """
SELECT ROUND(AVG(mark),3) FROM marks
"""


def execute_query(sql: str) -> list:

    with sqlite3.connect('univer_base.db') as con:
        cur = con.cursor()
        cur.execute(sql)

        return cur.fetchall()


print(f'Result of query >>> {execute_query(sql_query_4)[0][0]}')
