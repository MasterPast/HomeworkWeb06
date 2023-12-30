--Знайти які курси читає певний викладач.
SELECT t.teacher_name, s.subject_name FROM subjects AS s
FULL JOIN teachers AS t ON s.teacher_id = t.id
WHERE t.teacher_name = '{}'
ORDER BY s.subject_name;
