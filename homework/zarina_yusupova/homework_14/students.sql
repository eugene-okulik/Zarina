INSERT INTO students (name, second_name, group_id) VALUES ('Zarina', 'Yusupova', 1)
INSERT INTO books (title, taken_by_student_id) VALUES ('Anna Karenina', 21866)
INSERT INTO books (title, taken_by_student_id) VALUES ('War and Piece', 21866)
INSERT INTO books (title, taken_by_student_id) VALUES ('Master and Margarita', 21866)
INSERT INTO `groups` (title, start_date, end_date) 
VALUES ('Dream Team', 'dec 25', 'feb 26')
UPDATE students SET group_id = 21645 WHERE id = 21866
INSERT INTO subjects (title) VALUES ('Автоматизация тестирования')
INSERT INTO subjects (title) VALUES ('История России')
INSERT INTO subjects (title) VALUES ('История Китая')
INSERT INTO lessons (title, subject_id) VALUES ('Python', 13201)
INSERT INTO lessons (title, subject_id) VALUES ('SQL', 13201)
INSERT INTO lessons (title, subject_id) VALUES ('lesson1', 13202)
INSERT INTO lessons (title, subject_id) VALUES ('lesson2', 13202)
INSERT INTO lessons (title, subject_id) VALUES ('China1', 13203)
INSERT INTO lessons (title, subject_id) VALUES ('China2', 13203)
INSERT INTO marks (value, lesson_id, student_id) VALUES (5, 73805, 21866)
INSERT INTO marks (value, lesson_id, student_id) VALUES (4, 73806, 21866)
INSERT INTO marks (value, lesson_id, student_id) VALUES (5, 73807, 21866)
INSERT INTO marks (value, lesson_id, student_id) VALUES (4, 73808, 21866)
INSERT INTO marks (value, lesson_id, student_id) VALUES (5, 73809, 21866)
INSERT INTO marks (value, lesson_id, student_id) VALUES (5, 73810, 21866)
SELECT value FROM marks WHERE student_id = 21866
SELECT title FROM books WHERE taken_by_student_id = 21866
SELECT s.id, name, second_name, group_id, b.title, sj.title, l.title, m.value
FROM students s JOIN books b ON s.id = b.taken_by_student_id JOIN 
marks m ON s.id = m.student_id JOIN lessons l ON m.lesson_id = l.id JOIN
subjects sj ON l.subject_id = sj.id
WHERE s.id = 21866

