import psycopg2
def addData(Data):
    from Data import Host, Port, Database, User, Password #Giữ nguyên vị trí, nếu để lên đầu sẽ chưa cập nhật data
    try:
        conn = psycopg2.connect(host=Host, port=Port, database=Database, user=User, password=Password)
        cur = conn.cursor()
        selectByName = """insert into public."Trainee"(full_name, gender, birthday, entry_iq, entry_gmath, entry_english, training_class_code) values('{}', '{}', '{}', {}, {} , {} , {});""".format(Data[0], Data[1], Data[2], Data[3], Data[4], Data[5], Data[6])
        cur.execute(selectByName)
        conn.commit() #Có commit mới lưu
        cur.close()
        conn.close()
        return 1
    except:
        return 0
