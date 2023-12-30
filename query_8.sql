--Знайти середній бал, який ставить певний викладач зі своїх предметів.
SELECT t.teacher_name, s.subject_name, ROUND(AVG(m.mark), 3) FROM marks AS m
FULL JOIN subjects AS s ON m.subject_id = s.id 
FULL JOIN teachers AS t ON s.teacher_id = t.id
WHERE t.teacher_name = '{}'
GROUP BY s.subject_name;
