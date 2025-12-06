import os
from datetime import datetime, timedelta

homework_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
eugene_okulik_path = os.path.join(homework_path, "eugene_okulik", "hw_13", "data.txt")

with open(eugene_okulik_path, 'r') as data_file:
    lines = data_file.readlines()
clear_lines = [line[:line.index(' -')] for line in lines]
for line in clear_lines:
    data = datetime.strptime(line[line.index('. ') + 2:], '%Y-%m-%d %H:%M:%S.%f')
    if line[:1] == '1':
        print(line[:2], data + timedelta(days=7))
    elif line[:1] == "2":
        print(line[:2], datetime.strftime(data, '%A'))
    elif line[:1] == "3":
        print(line[:2], (datetime.now() - data).days)
