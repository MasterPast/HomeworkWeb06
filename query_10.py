# Список курсів, які певному студенту читає певний викладач.
import sqlite3
from query_funcs import choose, sql_choose_student, sql_choose_teacher, sql_query_10


def execute_query(sql: str, student: str, teacher: str) -> list:

    with sqlite3.connect('univer_base.db') as con:
        cur = con.cursor()
        cur.execute(sql.format(student))

        return cur.fetchall()


student = choose(sql_choose_student)
teacher = choose(sql_choose_teacher)
print(f'Result of query >>> {execute_query(sql_query_10, student, teacher)}')
