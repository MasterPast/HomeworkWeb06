--Знайти список студентів у певній групі.
SELECT s.student_name, g.group_name FROM students as s
FULL JOIN groups AS g ON g.id = s.group_id 
WHERE g.group_name = '{}'
ORDER BY g.group_name;
