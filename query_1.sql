--Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
SELECT s.student_name, ROUND(AVG(m.mark), 3) FROM marks AS m
FULL JOIN students AS s ON m.student_id = s.id
GROUP BY s.student_name ORDER BY AVG(m.mark) DESC LIMIT 5;
