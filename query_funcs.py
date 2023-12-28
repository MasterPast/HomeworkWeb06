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

sql_query_1 = """
SELECT s.student_name, ROUND(AVG(m.mark), 3) FROM marks AS m
FULL JOIN students AS s ON m.student_id = s.id
GROUP BY s.student_name ORDER BY AVG(m.mark) DESC LIMIT 5
"""

sql_query_2 = """
SELECT s.student_name, s2.subject_name, AVG(m.mark) FROM marks AS m
FULL JOIN students AS s ON m.student_id = s.id
FULL JOIN subjects AS s2 ON m.subject_id = s2.id 
WHERE s2.subject_name = '{}'
GROUP BY s2.subject_name, s.student_name ORDER BY AVG(m.mark) DESC LIMIT 1
"""

sql_query_3 = """
SELECT g.group_name, s2.subject_name, ROUND(AVG(m.mark), 3) FROM marks AS m
FULL JOIN students AS s ON m.student_id = s.id
FULL JOIN subjects AS s2 ON m.subject_id = s2.id 
FULL JOIN groups AS g ON s.group_id = g.id 
WHERE s2.subject_name = '{}'
GROUP BY g.group_name 
"""
sql_query_4 = """
SELECT ROUND(AVG(mark),3) FROM marks
"""

sql_query_5 = """
SELECT t.teacher_name, s.subject_name FROM subjects AS s
FULL JOIN teachers AS t ON s.teacher_id = t.id
WHERE t.teacher_name = '{}'
ORDER BY s.subject_name
"""

sql_query_6 = """
SELECT s.student_name, g.group_name FROM students as s
FULL JOIN groups AS g ON g.id = s.group_id 
WHERE g.group_name = '{}'
ORDER BY g.group_name
"""

sql_query_7 = """
SELECT g.group_name, s2.subject_name, s.student_name, m.date_mark, m.mark FROM marks AS m
FULL JOIN students AS s ON m.student_id = s.id
FULL JOIN subjects AS s2 ON m.subject_id = s2.id 
FULL JOIN groups AS g ON s.group_id = g.id 
WHERE g.group_name = '{}' AND s2.subject_name = '{}'
ORDER BY s.student_name, m.date_mark 
"""

sql_query_8 = """
SELECT t.teacher_name, s.subject_name, ROUND(AVG(m.mark), 3) FROM marks AS m
FULL JOIN subjects AS s ON m.subject_id = s.id 
FULL JOIN teachers AS t ON s.teacher_id = t.id
WHERE t.teacher_name = '{}'
GROUP BY s.subject_name 
"""

sql_query_9 = """
SELECT s.student_name, s2.subject_name FROM subjects AS s2
FULL JOIN marks AS m ON m.subject_id = s2.id 
FULL JOIN students AS s ON m.student_id = s.id 
WHERE s.student_name = '{}'
GROUP BY s2.subject_name 
"""

sql_query_10 = """

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
