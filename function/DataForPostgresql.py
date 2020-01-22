from tkinter import *
from tkinter import messagebox
from ConnectToPostgresql import connect

def connectFrame():
    def leftClick():
        if connect(host_blank.get(), dataBaseName_blank.get(),
            port_blank.get(), user_blank.get(), password_blank.get()
            ):
            root.destroy()
        else:
            messagebox.showinfo('Bài Tập Tuần 2', 'Something wrong !! Check again')
    root = Tk()
    root.title('Bài Tập Tuần 2')
    root.geometry('400x150')

    host = Label(root, text="Host")
    dataBaseName = Label(root, text="Database")
    port = Label(root, text="Port")
    user = Label(root, text="User")
    password = Label(root, text="Password")

    host_blank = Entry(root, width=50)
    dataBaseName_blank = Entry(root, width=50)
    port_blank = Entry(root, width=50)
    user_blank = Entry(root, width=50)
    password_blank = Entry(root, width=50)

    host.grid(row=0)
    dataBaseName.grid(row=1)
    port.grid(row=2)
    user.grid(row=3)
    password.grid(row=4)


    host_blank.grid(row=0, column=2)
    dataBaseName_blank.grid(row=1, column=2)
    port_blank.grid(row=2, column=2)
    user_blank.grid(row=3, column=2)
    password_blank.grid(row=4, column=2)

    button1 = Button(root, text="Connect", command=leftClick)
    button1.grid(row=5, column=2)

    root.mainloop()

