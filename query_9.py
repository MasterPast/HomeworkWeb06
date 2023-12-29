# Знайти список курсів, які відвідує студент.
import sqlite3
from query_funcs import choose, sql_choose_student

sql_query_9 = """
SELECT s.student_name, s2.subject_name FROM subjects AS s2
FULL JOIN marks AS m ON m.subject_id = s2.id 
FULL JOIN students AS s ON m.student_id = s.id 
WHERE s.student_name = '{}'
GROUP BY s2.subject_name 
"""


def execute_query(sql: str, student: str) -> list:

    with sqlite3.connect('univer_base.db') as con:
        cur = con.cursor()
        cur.execute(sql.format(student))

        return cur.fetchall()


student = choose(sql_choose_student)
print(f'Result of query >>> {execute_query(sql_query_9, student)}')
