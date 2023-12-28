# Знайти список курсів, які відвідує студент.
import sqlite3
from query_funcs import choose, sql_choose_student, sql_query_9


def execute_query(sql: str, student: str) -> list:

    with sqlite3.connect('univer_base.db') as con:
        cur = con.cursor()
        cur.execute(sql.format(student))

        return cur.fetchall()


student = choose(sql_choose_student)
print(f'Result of query >>> {execute_query(sql_query_9, student)}')
