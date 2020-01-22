import psycopg2
import datetime
from tkinter import *

def connect(host1, port1, database1, user1, password1):
    try:
        conn = psycopg2.connect(host=host1, port=port1, database=database1, user=user1, password=password1)
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
        return 1
    except:
        return 0
