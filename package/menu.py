from InsertData import insertData
from DisplayData import displayData

def menu():
    while True:
        chucNang = input("Nhập 2 để thêm sinh viên, 1 để hiện 5 bạn có tổng chỉ số cao nhất , 0 để thoát: \n")
        if chucNang == "0":
            break
        elif chucNang == "2":
            insertData()
        elif chucNang == "1":
            displayData()
        else:
            print("Chức năng không phù hợp")

