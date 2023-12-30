--Оцінки студентів у певній групі з певного предмета на останньому занятті.
SELECT s.student_name, g.group_name, s2.subject_name, m.mark, m.date_mark FROM marks AS m 
FULL JOIN students AS s ON s.id = m.student_id 
FULL JOIN subjects AS s2 ON m.subject_id = s2.id
FULL JOIN groups AS g ON s.group_id = g.id 
WHERE g.group_name = '{}' AND s2.subject_name = '{}' AND m.date_mark = (SELECT MAX(date_mark) FROM marks)
ORDER BY s.student_name""";