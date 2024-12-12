import tkinter
from tkinter import messagebox
from project import g


#===============main=====================
class Login:
    def __init__(self, root , db):
        self.root = root
        self.db = db
        self.root.geometry("400x300")
        self.root.title("login page")
        self.root.config(bg="#faaa60")
        # Label
        self.label_username = tkinter.Label(master=root, text="username", bg="#008B8B")
        self.label_username.place(x=160, y=50)
        self.label_password = tkinter.Label(master=root, text="password", bg="#008B8B")
        self.label_password.place(x=160, y=120)
        # entry
        self.entry_username = tkinter.Entry(master= root,width= 15 )
        self.entry_username.place (x=150,y=80)
        self.entry_password = tkinter.Entry(master=root, width=15)
        self.entry_password.place(x=150, y=150)
        # button
        self.button1 = tkinter.Button(root,text="login",width=15 , bg='#F9E79F',command=self.get_username)
        self.button1.place(x=140,y=200)

    def get_username(self):
        username1 = self.entry_username.get()
        password1 = self.entry_password.get()
        # res = g.select_table(username=username1)
        db = self.db.select_table(username=username1)
        # print(db)
        if db is None:
            messagebox.showinfo("info","user not found")
        else:
            if db[2] == password1:
                messagebox.showinfo("info", "Login Successfull!!")
            else:
                messagebox.showinfo("info", "please write your usename and password")


if __name__ == '__main__':
    db = g.Database('./mydatabasemain.db')
    # db = './mydatabase3.db'
    window = tkinter.Tk()
    app = Login(window , db)
    window.mainloop()
    db.close()