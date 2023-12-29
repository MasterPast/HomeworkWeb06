# Знайти середній бал у групах з певного предмета.
import sqlite3
from query_funcs import choose, sql_choose_subject

sql_query_3 = """
SELECT g.group_name, s2.subject_name, ROUND(AVG(m.mark), 3) FROM marks AS m
FULL JOIN students AS s ON m.student_id = s.id
FULL JOIN subjects AS s2 ON m.subject_id = s2.id 
FULL JOIN groups AS g ON s.group_id = g.id 
WHERE s2.subject_name = '{}'
GROUP BY g.group_name 
"""


def execute_query(sql: str, subject: str) -> list:

    with sqlite3.connect('univer_base.db') as con:
        cur = con.cursor()
        cur.execute(sql.format(subject))

        return cur.fetchall()


subject = choose(sql_choose_subject)
print(f'Result of query >>> {execute_query(sql_query_3, subject)}')
