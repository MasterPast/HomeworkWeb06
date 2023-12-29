# Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
import sqlite3

sql_query_1 = """
SELECT s.student_name, ROUND(AVG(m.mark), 3) FROM marks AS m
FULL JOIN students AS s ON m.student_id = s.id
GROUP BY s.student_name ORDER BY AVG(m.mark) DESC LIMIT 5
"""


def execute_query(sql: str) -> list:

    with sqlite3.connect('univer_base.db') as con:
        cur = con.cursor()
        cur.execute(sql)

        return cur.fetchall()


print(f'Result of query >>>{execute_query(sql_query_1)}')

