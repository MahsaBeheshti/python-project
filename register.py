import tkinter
from tkinter import messagebox
#===============main===================
from project import g
import second_page


class Register:
    def __init__(self, root,db):
        self.root = root
        self.db = db
        self.root.geometry("400x300")
        self.root.title("register page")
        self.root.config(bg="#faaa60")
        # Label
        self.label_info = tkinter.Label(root,text="Please enter the details below\nin the given empty fields",bg="#F9E79F")
        self.label_info.place(x=130,y=0)
        self.label_username = tkinter.Label(master=root, text="username", bg="#008B8B")
        self.label_username.place(x=160, y=50)
        self.label_password = tkinter.Label(master=root, text="password", bg="#008B8B")
        self.label_password.place(x=160, y=110)
        self.label_password2 = tkinter.Label(master=root, text="password2", bg="#008B8B")
        self.label_password2.place(x=160, y=180)
        # self.result_label = tkinter.Label(root,)
        # entry
        self.entry_username = tkinter.Entry(master= root,width= 15 )
        self.entry_username.place (x=150,y=80)
        self.entry_password = tkinter.Entry(master=root, width=15)
        self.entry_password.place(x=150, y=150)
        self.entry_password2 = tkinter.Entry(master=root, width=15)
        self.entry_password2.place(x=150, y=210)
        # button
        self.button1 = tkinter.Button(root,text="register",width=15 , bg='#F9E79F',command=self.get_register)
        self.button1.place(x=140,y=250)


    def get_register(self):
        username1 = self.entry_username.get()
        password1 = self.entry_password.get()
        password2 = self.entry_password2.get()

        if len(username1) == 0 or len(password1) == 0 or len(password2) == 0:
            messagebox.showinfo('warning','fill out every singlr entry')
        else:
            if password2 != password1:
                messagebox.showinfo('warning','password do not mach')
            else:
                res = self.db.insert_to_db(username1,password1)
                messagebox.showinfo('yes','you can create your account')
                new_page = tkinter.Tk()
                secoud = second_page.BMI(new_page)
                self.root.destroy()


if __name__ == '__main__':
    db = g.Database('./mydatabasemain.db')
    # db = ('./database.db')
    window = tkinter.Tk()
    app = Register(window, db)
    window.mainloop()
    db.close()