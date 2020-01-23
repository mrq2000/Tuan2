from tkinter import *
from tkinter.ttk import *
from AddData import addData
from tkinter import messagebox
import datetime
def insertData():
    def ADD():
        data = [full_Name.get(),
                gender_combo.get(),
                birth_Day.get(),
                entry_iq_blank.get(),
                entry_english_blank.get(),
                entry_gmath_blank.get(),
                classCode_blank.get()
                ]
        if addData(data):
            root.destroy()
        else:
            checkDay = birth_Day.get().split("-")
            try:
                datetime.datetime(int(checkDay[2]),int(checkDay[0]),int(checkDay[1]))
                messagebox.showinfo('Bài Tập Tuần 2', 'Something wrong !! Check again')
            except:
                messagebox.showinfo('Bài Tập Tuần 2', 'Nhập Tháng-Ngày-Năm cách nhau bởi dấu "-"')
    root = Tk()
    root.title('Bài Tập Tuần 2')
    root.geometry('400x200')

    fullName = Label(root, text="Tên đầy đủ")
    birthDay = Label(root, text="Ngày sinh")
    gender = Label(root, text="Giới Tính")
    classCode = Label(root, text="Lớp")
    entry_english = Label(root, text="Entry English")
    entry_iq = Label(root, text="Entry Iq")
    entry_gmath = Label(root, text="Entry Gmath")

    full_Name = Entry(root, width=50)
    birth_Day = Entry(root, width=50)
    classCode_blank = Entry(root, width=50)
    entry_english_blank = Entry(root, width=50)
    entry_iq_blank = Entry(root, width=50)
    entry_gmath_blank = Entry(root, width=50)
    gender_combo = Combobox(root)
    gender_combo['values']= ("Nam", "Nữ")
    gender_combo.current(0)


    fullName.grid(row=0)
    birthDay.grid(row=1)
    gender.grid(row=2)
    classCode.grid(row=3)
    entry_english.grid(row=4)
    entry_iq.grid(row=5)
    entry_gmath.grid(row=6)


    full_Name.grid(row=0, column=1)
    birth_Day.grid(row=1, column=1)
    gender_combo.grid(row=2, column=1)
    classCode_blank.grid(row=3, column=1)
    entry_english_blank.grid(row=4, column=1)
    entry_iq_blank.grid(row=5, column=1)
    entry_gmath_blank.grid(row=6, column=1)

    button1 = Button(root, text="ADD", command=ADD)
    button1.grid(row=7, column=1)

    root.mainloop()
