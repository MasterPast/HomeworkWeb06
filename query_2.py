# Знайти студента із найвищим середнім балом з певного предмета.
import sqlite3
from query_funcs import choose, sql_choose_subject, sql_query_2


def execute_query(sql: str, subject: str) -> list:

    with sqlite3.connect('univer_base.db') as con:
        cur = con.cursor()
        cur.execute(sql.format(subject))

        return cur.fetchall()


subject = choose(sql_choose_subject)
print(f'Result of query >>> {execute_query(sql_query_2, subject)}')
