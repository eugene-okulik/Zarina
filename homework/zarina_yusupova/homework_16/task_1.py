import csv
import os
import dotenv
import pymysql
from pymysql.cursors import DictCursor

dotenv.load_dotenv()
db = pymysql.connect(
    user=os.getenv("DB_USER"),
    passwd=os.getenv("DB_PASSW"),
    host=os.getenv("DB_HOST"),
    port=int(os.getenv("DB_PORT")),
    database=os.getenv("DB_NAME"),
    cursorclass=DictCursor
)
cursor = db.cursor()
query = """
SELECT 
    s.name, 
    s.second_name, 
    g.title AS group_title, 
    b.title AS book_title, 
    sj.title AS subject_title, 
    l.title AS lesson_title, 
    m.value AS mark_value
FROM students s
JOIN `groups` g ON g.id = s.group_id
JOIN books b ON s.id = b.taken_by_student_id
JOIN marks m ON s.id = m.student_id
JOIN lessons l ON m.lesson_id = l.id
JOIN subjects sj ON l.subject_id = sj.id
WHERE s.name = %s 
AND s.second_name = %s 
AND g.title = %s 
AND b.title = %s 
AND sj.title = %s 
AND l.title = %s
AND m.value = %s
"""

homework_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
eugene_okulik_path = os.path.join(homework_path, "eugene_okulik", "Lesson_16", "hw_data", "data.csv")

with open(eugene_okulik_path, newline='') as csv_file:
    file_data = csv.DictReader(csv_file)
    not_in_database = []
    for row in file_data:
        cursor.execute(
            query,
            (
                row["name"],
                row["second_name"],
                row["group_title"],
                row["book_title"],
                row["subject_title"],
                row["lesson_title"],
                row["mark_value"]
            )
        )
        if cursor.fetchone() is None:
            not_in_database.append(row)
for row in not_in_database:
    print(row)
db.close()
