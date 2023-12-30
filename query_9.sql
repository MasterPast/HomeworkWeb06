--Знайти список курсів, які відвідує студент.
SELECT s.student_name, s2.subject_name FROM subjects AS s2
FULL JOIN marks AS m ON m.subject_id = s2.id 
FULL JOIN students AS s ON m.student_id = s.id 
WHERE s.student_name = '{}'
GROUP BY s2.subject_name;