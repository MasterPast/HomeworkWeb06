--Список курсів, які певному студенту читає певний викладач.
SELECT t.teacher_name, s.student_name, s2.subject_name FROM subjects AS s2
FULL JOIN teachers AS t ON t.id = s2.teacher_id 
FULL JOIN marks AS m ON m.subject_id = s2.id
FULL JOIN students AS s ON s.id = m.student_id 
WHERE t.teacher_name = '{}' AND s.student_name = '{}'
GROUP BY s2.subject_name;