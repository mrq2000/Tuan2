import psycopg2
import datetime
from tkinter import *

def connect(Host, Port, Database, User, Password):
    try:
        conn = psycopg2.connect(host=Host, port=Port, database=Database, user=User, password=Password)
        cur = conn.cursor()
        selectByName = 'SELECT * FROM "Trainee" ORDER BY full_name DESC'
        cur.execute(selectByName)
        data = cur.fetchall()
        print('{:<5}{:<30}{:^16}{:^10}{:^10}{:^10}{:^10}{:^10}'
            .format('STT', 'Tên đầy đủ', 'Ngày sinh', 'Giới tính', 'Lớp', 'IQ', 'GMath', 'English')
            )

        for i in range(len(data)):
            print('{:<5}{:<30}{:^16}{:^10}{:^10}{:^10}{:^10}{:^10}'
                .format(data[i][0], data[i][1], str(data[i][3]), data[i][2], data[i][7], data[i][5], data[i][6], data[i][4])
                )

        cur.close()
        conn.close()
        return 1
    except:
        return 0
