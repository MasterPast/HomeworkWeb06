# Знайти оцінки студентів у окремій групі з певного предмета.
import sqlite3
from query_funcs import choose, sql_choose_group, sql_choose_subject

sql_query_7 = """
SELECT g.group_name, s2.subject_name, s.student_name, m.date_mark, m.mark FROM marks AS m
FULL JOIN students AS s ON m.student_id = s.id
FULL JOIN subjects AS s2 ON m.subject_id = s2.id 
FULL JOIN groups AS g ON s.group_id = g.id 
WHERE g.group_name = '{}' AND s2.subject_name = '{}'
ORDER BY s.student_name, m.date_mark 
"""


def execute_query(sql: str, group: str, subject: str) -> list:

    with sqlite3.connect('univer_base.db') as con:
        cur = con.cursor()
        cur.execute(sql.format(group, subject))

        return cur.fetchall()


group = choose(sql_choose_group)
subject = choose(sql_choose_subject)
print(f'Result of query >>> {execute_query(sql_query_7, group, subject)}')
