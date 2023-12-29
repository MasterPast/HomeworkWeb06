import sqlite3

sql_choose_group = """
SELECT * FROM groups
"""

sql_choose_student = """
SELECT * FROM students
"""

sql_choose_subject = """
SELECT * FROM subjects
"""

sql_choose_teacher = """
SELECT * FROM teachers
"""


def choose(sql: str) -> str:

    with sqlite3.connect('univer_base.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        result = cur.fetchall()
        for res in result:
            print(res)
        subj = input('Choose >>> ')
        for res in result:
            if int(subj) in res:
                subject = res[1]

    return subject
