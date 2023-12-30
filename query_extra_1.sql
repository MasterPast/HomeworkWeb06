--Середній бал, який певний викладач ставить певному студентові.
SELECT t.teacher_name, s.student_name, ROUND(AVG(m.mark), 3) FROM marks AS m
FULL JOIN students AS s ON s.id = m.student_id 
FULL JOIN subjects AS s2 ON m.subject_id = s2.id
FULL JOIN teachers AS t ON t.id = s2.teacher_id 
WHERE t.teacher_name = '{}' AND s.student_name = '{}';
