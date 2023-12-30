-- Знайти середній бал у групах з певного предмета.
SELECT g.group_name, s2.subject_name, ROUND(AVG(m.mark), 3) FROM marks AS m
FULL JOIN students AS s ON m.student_id = s.id
FULL JOIN subjects AS s2 ON m.subject_id = s2.id 
FULL JOIN groups AS g ON s.group_id = g.id 
WHERE s2.subject_name = '{}'
GROUP BY g.group_name;