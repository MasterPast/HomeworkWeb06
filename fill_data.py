import faker
from random import randint, randrange
import sqlite3

NUMBER_STUDENTS = randint(30, 50)
NUMBER_GROUPS = 3
NUMBER_TEACHERS = randint(3, 5)
NUMBER_SUBJECTS = randint(5, 8)
NUMBER_MARKS_ON_SUBJECT = randint(10, 20)


def generate_fake_data(num_stud, num_grp, num_tch, num_subj, num_mrk):

    fake_students = []
    fake_students_address = []
    fake_groups = []
    fake_teachers = []
    fake_subjects = []
    fake_marks = []
    fake_date_marks = []

    fake_data = faker.Faker(locale='uk_UA')

    for _ in range(num_stud):
        fake_students.append(fake_data.name())
        fake_students_address.append(fake_data.address())
    for num in range(num_grp):
        fake_groups.append(f'UNV-G{num+1}')
    for _ in range(num_tch):
        fake_teachers.append(fake_data.name().upper())
    for _ in range(num_subj):
        fake_subjects.append(fake_data.job())
    for _ in range(num_mrk * num_stud):
        fake_marks.append(randrange(1, 6))
        fake_date_marks.append(fake_data.date_between(
            start_date='-7d', end_date='today'))

    return fake_students, fake_students_address, fake_groups, fake_teachers, fake_subjects, fake_marks, fake_date_marks


def prepare_data(students, student_address, groups, teachers, subjects, marks, date_marks):

    students_db = []
    groups_db = []
    teachers_db = []
    subjects_db = []
    marks_db = []

    temp_db = []
    for _ in range(len(students)):
        temp_db.append(randint(1, len(groups)))
    students_db = list(zip(students, student_address, temp_db))

    for _ in groups:
        groups_db.append((_, ))

    for _ in teachers:
        teachers_db.append((_, ))

    for _ in subjects:
        subjects_db.append((_, randint(1, len(teachers))))


    temp_db = []
    temp_db2 = []
    for _ in range(len(marks)):
        temp_db.append(randint(1, len(subjects)))
        temp_db2.append(randint(1, len(students)))
    marks_db = list(zip(marks, date_marks, temp_db, temp_db2))

    return students_db, groups_db, teachers_db, subjects_db, marks_db


def insert_data_to_db(students, groups, teachers, subjects, marks) -> None:

    with sqlite3.connect('univer_base.db') as con:

        cur = con.cursor()
        sql_to_students = """INSERT INTO students(student_name, student_address, group_id)
                               VALUES (?, ?, ?)"""
        cur.executemany(sql_to_students, students)
        
        sql_to_groups = """INSERT INTO groups(group_name)
                               VALUES (?)"""
        cur.executemany(sql_to_groups, groups)
        
        sql_to_teachers = """INSERT INTO teachers(teacher_name)
                              VALUES (?)"""
        cur.executemany(sql_to_teachers, teachers)
        
        sql_to_subjects = """INSERT INTO subjects(subject_name, teacher_id)
                              VALUES (?, ?)"""
        cur.executemany(sql_to_subjects, subjects)
        
        sql_to_marks = """INSERT INTO marks(mark, date_mark, subject_id, student_id)
                              VALUES (?, ?, ?, ?)"""
        cur.executemany(sql_to_marks, marks)
        con.commit()


if __name__ == "__main__":
    
    insert_data_to_db(*prepare_data(*generate_fake_data(NUMBER_STUDENTS, NUMBER_GROUPS, 
                                                      NUMBER_TEACHERS, NUMBER_SUBJECTS, 
                                                      NUMBER_MARKS_ON_SUBJECT
                                                      )))
