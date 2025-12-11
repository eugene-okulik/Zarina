import pymysql
from pymysql.cursors import DictCursor

db = pymysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl',
    cursorclass=DictCursor
)

cursor = db.cursor()
cursor.execute("INSERT INTO students (name, second_name) VALUES ('Zarina', 'Yusupova')")
student_id = cursor.lastrowid
query = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"
values = [
    ('Anna Karenina', student_id),
    ('War and Piece', student_id),
    ('Master and Margarita', student_id)
]
cursor.executemany(query, values)
cursor.execute("INSERT INTO `groups` (title, start_date, end_date) VALUES ('Dream Team', 'dec 25', 'feb 26')")
group_id = cursor.lastrowid
query2 = "UPDATE students SET group_id = %s WHERE id = %s"
cursor.execute(query2, (group_id, student_id))
query3 = "INSERT INTO subjects (title) VALUES (%s)"
values3 = ['Автоматизация тестирования', 'История России', 'История Китая']
cursor.executemany(query3, values3)
sj_id = cursor.lastrowid
query4 = "INSERT INTO lessons (title, subject_id) VALUES ('Python', %s)"
cursor.execute(query4, sj_id)
lesson1 = cursor.lastrowid
query5 = "INSERT INTO lessons (title, subject_id) VALUES ('SQL', %s)"
cursor.execute(query5, sj_id)
lesson2 = cursor.lastrowid
query6 = "INSERT INTO lessons (title, subject_id) VALUES ('lesson1', %s)"
cursor.execute(query6, sj_id + 1)
lesson3 = cursor.lastrowid
query7 = "INSERT INTO lessons (title, subject_id) VALUES ('lesson2', %s)"
cursor.execute(query7, sj_id + 1)
lesson4 = cursor.lastrowid
query8 = "INSERT INTO lessons (title, subject_id) VALUES ('China1', %s)"
cursor.execute(query8, sj_id + 2)
lesson5 = cursor.lastrowid
query9 = "INSERT INTO lessons (title, subject_id) VALUES ('China2', %s)"
cursor.execute(query9, sj_id + 2)
lesson6 = cursor.lastrowid
query10 = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)"
values10 = [
    (5, lesson1, student_id),
    (4, lesson2, student_id),
    (5, lesson3, student_id),
    (4, lesson4, student_id),
    (5, lesson5, student_id),
    (5, lesson6, student_id)
]
cursor.executemany(query10, values10)
mark_id = cursor.lastrowid
query11 = "SELECT value FROM marks WHERE student_id = %s"
cursor.execute(query11, student_id)
marks = cursor.fetchall()
print(marks)
query12 = "SELECT title FROM books WHERE taken_by_student_id = %s"
cursor.execute(query12, student_id)
books = cursor.fetchall()
print(books)
query13 = '''
SELECT s.id, name, second_name, group_id, b.title, sj.title, l.title, m.value
FROM students s JOIN books b ON s.id = b.taken_by_student_id 
JOIN marks m ON s.id = m.student_id JOIN lessons l ON m.lesson_id = l.id 
JOIN subjects sj ON l.subject_id = sj.id
WHERE s.id = %s
'''
cursor.execute(query13, student_id)
info_of_student = cursor.fetchall()
for row in info_of_student:
    print(row)
db.commit()
db.close()
