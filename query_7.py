# Знайти оцінки студентів у окремій групі з певного предмета.
import sqlite3
from query_funcs import choose, sql_choose_group, sql_choose_subject, sql_query_7


def execute_query(sql: str, group: str, subject: str) -> list:

    with sqlite3.connect('univer_base.db') as con:
        cur = con.cursor()
        cur.execute(sql.format(group, subject))

        return cur.fetchall()


group = choose(sql_choose_group)
subject = choose(sql_choose_subject)
print(f'Result of query >>> {execute_query(sql_query_7, group, subject)}')
