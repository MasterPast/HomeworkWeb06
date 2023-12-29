# Оцінки студентів у певній групі з певного предмета на останньому занятті.
import sqlite3
from query_funcs import choose, sql_choose_group, sql_choose_subject

pre_sql_query = """
SELECT MAX(m.date_mark) FROM marks AS m 
FULL JOIN students AS s ON s.id = m.student_id 
FULL JOIN subjects AS s2 ON m.subject_id = s2.id
FULL JOIN groups AS g ON s.group_id = g.id 
WHERE g.group_name = '{}' AND s2.subject_name = '{}'
"""

sql_query_extra_2 = """
SELECT s.student_name, g.group_name, s2.subject_name, m.mark, m.date_mark FROM marks AS m 
FULL JOIN students AS s ON s.id = m.student_id 
FULL JOIN subjects AS s2 ON m.subject_id = s2.id
FULL JOIN groups AS g ON s.group_id = g.id 
WHERE g.group_name = '{}' AND s2.subject_name = '{}' AND m.date_mark = '{}'
"""


def execute_query(presql:str, sql: str, group: str, subject: str) -> list:

    with sqlite3.connect('univer_base.db') as con:

        cur = con.cursor()
        date_mark = cur.execute(presql.format(group, subject)).fetchall()[0][0]
        cur.execute(sql.format(group, subject, date_mark))

        return cur.fetchall()


group = choose(sql_choose_group)
subject = choose(sql_choose_subject)
print(f'Result of query >>> {execute_query(pre_sql_query, sql_query_extra_2, group, subject)}')
