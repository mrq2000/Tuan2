from tkinter import *
from tkinter.ttk import *
# class inputData(data):
#     def __init__(self, arg):


root = Tk()
root.title('Bài Tập Tuần 2')
root.geometry('500x500')

fullName = Label(root, text="Tên đầy đủ")
birthDay = Label(root, text="Ngày sinh")
gender = Label(root, text="Giới Tính")
full_Name = Entry(root, width=50)
birth_Day = Entry(root, width=50)
gender_combo = Combobox(root)
gender_combo['values']= ("Nam", "Nữ")
gender_combo.current(0)
for i in range(10):


fullName.grid(row=0)
birthDay.grid(row=1)
gender.grid(row=2)

full_Name.grid(row=0, column=1)
birth_Day.grid(row=1, column=1)
gender_combo.grid(row=2, column=1)

root.mainloop()
