# Знайти середній бал, який ставить певний викладач зі своїх предметів.
import sqlite3
from query_funcs import choose, sql_choose_teacher

sql_query_8 = """
SELECT t.teacher_name, s.subject_name, ROUND(AVG(m.mark), 3) FROM marks AS m
FULL JOIN subjects AS s ON m.subject_id = s.id 
FULL JOIN teachers AS t ON s.teacher_id = t.id
WHERE t.teacher_name = '{}'
GROUP BY s.subject_name 
"""


def execute_query(sql: str, teacher: str) -> list:

    with sqlite3.connect('univer_base.db') as con:
        cur = con.cursor()
        cur.execute(sql.format(teacher))

        return cur.fetchall()


teacher = choose(sql_choose_teacher)
print(f'Result of query >>> {execute_query(sql_query_8, teacher)}')
