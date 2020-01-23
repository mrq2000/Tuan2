import psycopg2
def displayData():
    from Data import Host, Port, Database, User, Password
    try:
        conn = psycopg2.connect(host=Host, port=Port, database=Database, user=User, password=Password)
        cur = conn.cursor()
        command = """SELECT * FROM "Trainee" order by entry_iq+entry_gmath+entry_english desc limit 5"""
        cur.execute(command)
        data = cur.fetchall()
        print("--------------------DANH SÁCH 5 BẠN TỔNG 3 ĐIỂM CAO NHẤT--------------------")
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

