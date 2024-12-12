from tkinter import *
from tkinter .font import Font
import messagebox
import tkinter
import login_page
import register
import page2
from sqlite_code import Database1
import os


class Login_Register:
    def __init__(self, main_page,db):
        self.main_page = main_page
        self.db = db
        self.main_page.title('صفحه ی ورود  ')
        # self.root = Tk()
        self.screen_w = self.main_page.winfo_screenwidth()
        self.screen_h = self.main_page.winfo_screenheight()
        w = 350
        h = 200
        x = self.screen_w / 2.7
        y = self.screen_h / 2.7
        self.main_page.geometry("%dx%d+%d+%d" %(w,h,x,y))
        self.main_page.config(bg='#790604')
        self.custom_font = Font(family='Roboto', size=12)
        self.custom_font_farsi = Font(family='2 Esfehan Bold', size=12)
        heading = Label(self.main_page, text="Register/Login ", font=self.custom_font, bg="#A3E4D7").pack()
        tkinter.Label(self.main_page, text="", bg="#790604").pack()
        tkinter.Label(self.main_page, text="", bg="#790604").pack()
        register_button =tkinter. Button(master=main_page, text='Register ', width='60', font=self.custom_font, bg='#A3E4D7',command=self.open_register).pack()
        tkinter.Label(self.main_page, text="", bg="#790604").pack()

        register_button = tkinter.Button(master=main_page, text='Login ', width='60', font=self.custom_font,bg='#A3E4D7', command=self.open_login).pack()
        tkinter.Label(self.main_page, text="", bg="#790604").pack()

    def open_login(self):
        new_page = tkinter.Tk()
        secoud = login_page.Login(new_page,db)
        self.main_page.destroy()

    def open_register(self):
        new_page = tkinter.Tk()
        secoud = register.Register(new_page, db)
        self.main_page.destroy()


if __name__ == '__main__':
    db = Database1("./mydatabasemain")
    window = tkinter.Tk()
    app = Login_Register(window,db)
    window.mainloop()
    db.close()
