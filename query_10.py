# Список курсів, які певному студенту читає певний викладач.
import sqlite3
from query_funcs import choose, sql_choose_student, sql_choose_teacher

sql_query_10 = """
SELECT t.teacher_name, s.student_name, s2.subject_name FROM subjects AS s2
FULL JOIN teachers AS t ON t.id = s2.teacher_id 
FULL JOIN marks AS m ON m.subject_id = s2.id
FULL JOIN students AS s ON s.id = m.student_id 
WHERE t.teacher_name = '{}' AND s.student_name = '{}'
GROUP BY s2.subject_name
"""


def execute_query(sql: str, student: str, teacher: str) -> list:

    with sqlite3.connect('univer_base.db') as con:
        cur = con.cursor()
        cur.execute(sql.format(student, teacher))

        return cur.fetchall()


student = choose(sql_choose_student)
teacher = choose(sql_choose_teacher)
print(f'Result of query >>> {execute_query(sql_query_10, teacher, student)}')
