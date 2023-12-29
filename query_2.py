# Знайти студента із найвищим середнім балом з певного предмета.
import sqlite3
from query_funcs import choose, sql_choose_subject

sql_query_2 = """
SELECT s.student_name, s2.subject_name, AVG(m.mark) FROM marks AS m
FULL JOIN students AS s ON m.student_id = s.id
FULL JOIN subjects AS s2 ON m.subject_id = s2.id 
WHERE s2.subject_name = '{}'
GROUP BY s2.subject_name, s.student_name ORDER BY AVG(m.mark) DESC LIMIT 1
"""


def execute_query(sql: str, subject: str) -> list:

    with sqlite3.connect('univer_base.db') as con:
        cur = con.cursor()
        cur.execute(sql.format(subject))

        return cur.fetchall()


subject = choose(sql_choose_subject)
print(f'Result of query >>> {execute_query(sql_query_2, subject)}')
