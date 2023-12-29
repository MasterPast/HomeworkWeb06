# Середній бал, який певний викладач ставить певному студентові.
import sqlite3
from query_funcs import choose, sql_choose_student, sql_choose_teacher

sql_query_extra_1 = """
SELECT t.teacher_name, s.student_name, ROUND(AVG(m.mark), 3) FROM marks AS m
FULL JOIN students AS s ON s.id = m.student_id 
FULL JOIN subjects AS s2 ON m.subject_id = s2.id
FULL JOIN teachers AS t ON t.id = s2.teacher_id 
WHERE t.teacher_name = '{}' AND s.student_name = '{}'

"""


def execute_query(sql: str, student: str, teacher: str) -> list:

    with sqlite3.connect('univer_base.db') as con:
        cur = con.cursor()
        cur.execute(sql.format(student, teacher))

        return cur.fetchall()


student = choose(sql_choose_student)
teacher = choose(sql_choose_teacher)
print(f'Result of query >>> {execute_query(sql_query_extra_1, teacher, student)}')
