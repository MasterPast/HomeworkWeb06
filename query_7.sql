--Знайти оцінки студентів у окремій групі з певного предмета.
SELECT g.group_name, s2.subject_name, s.student_name, m.date_mark, m.mark FROM marks AS m
FULL JOIN students AS s ON m.student_id = s.id
FULL JOIN subjects AS s2 ON m.subject_id = s2.id 
FULL JOIN groups AS g ON s.group_id = g.id 
WHERE g.group_name = '{}' AND s2.subject_name = '{}'
ORDER BY s.student_name, m.date_mark;