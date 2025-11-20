import datetime

date1 = "Jan 15, 2023 - 12:05:33"
date_python = datetime.datetime.strptime(date1, "%b %d, %Y - %H:%M:%S")
print(date_python.strftime("%B"))
print(date_python.strftime("%d.%m.%Y, %H:%M"))
