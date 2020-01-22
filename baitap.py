import psycopg2
import datetime
from tkinter import *
from InputData import inputData

conn = psycopg2.connect(host="localhost", port = 5432, database="test", user="postgres", password="anhquoc")
cur = conn.cursor()
selectByName = 'SELECT * FROM "Trainee" ORDER BY full_name DESC'
cur.execute(selectByName)
data = cur.fetchall()
print('{:<5}{:<30}{:^16}{:^10}{:^10}{:^10}{:^10}{:^10}'
    .format('STT', 'Tên đầy đủ', 'Ngày sinh', 'Giới tính', 'Lớp', 'IQ', 'GMath', 'English')
    )

for i in range(len(data)):
    print('{:<5}{:<30}{:^16}{:^10}{:^10}{:^10}{:^10}{:^10}'
        .format(data[i][0], data[i][1], str(data[i][3]), data[i][2], data[i][4], data[i][5], data[i][6], data[i][7])
        )

cur.close()
conn.close()
