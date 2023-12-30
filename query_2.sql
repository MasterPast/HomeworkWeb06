-- Знайти студента із найвищим середнім балом з певного предмета.
SELECT s.student_name, s2.subject_name, AVG(m.mark) FROM marks AS m
FULL JOIN students AS s ON m.student_id = s.id
FULL JOIN subjects AS s2 ON m.subject_id = s2.id 
WHERE s2.subject_name = '{}'
GROUP BY s2.subject_name, s.student_name ORDER BY AVG(m.mark) DESC LIMIT 1;
