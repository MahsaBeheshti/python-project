import tkinter
import messagebox


class BMI:
    def __init__(self, secound):

        self.secound = secound
        # self.secound = tkinter.Tk()
        self.secound.title('bmi')
        self.secound.geometry('420x360')
        self.secound.config(bg='#008B8B')
        # button
        self.label_height = tkinter.Label(master=secound, text='height')
        self.label_height.place(x=100, y=100)
        self.label_weight = tkinter.Label(master=secound, text='weight')
        self.label_weight.place(x=100, y=150)
        self.entry_height = tkinter.Entry(master=secound, width=18)
        self.entry_height.place(x=160, y=102)
        self.entry_weight = tkinter.Entry(master=secound, width=18)
        self.entry_weight.place(x=160, y=152)
        self.button_calculate_bmi = tkinter.Button(master=secound, text='calculate',
         width=25, command=self.calculate_bmi)
        self.button_calculate_bmi.place(x=100, y=210)
        self.button_guide = tkinter.Button(master=secound, text='راهنما', width=10,command=self.guide)
        self.button_guide.place(x=150, y=270)
        self.button_guide.config(bg='#00d1d1')

    def guide(self):
        messagebox.showinfo('راهنما', '''         لطفا قد را به متر را به متر 
        و وزن را به کیلوگرم وارد کنید            ''')

    def calculate_bmi(self):
        height = float(self.entry_height.get())
        weight = float(self.entry_weight.get())
        bmi = weight / (height ** 2)
        bmi = int(bmi*10000)
        if bmi < 18.5:
            messagebox.showinfo('bmi category', f'the number your bmi is:   {bmi}    and you are thin')
        elif 18.5 <= bmi <= 24.9:
            messagebox.showinfo('bmi category', f'the number your bmi is:   {bmi}    and you are normal')
        elif 25 < bmi <= 29.9:
            messagebox.showinfo('bmi category', f'the number your bmi is:   {bmi}    and you are over eight')
        elif 30 < bmi <= 34.9:
            messagebox.showinfo('bmi category', f'the number your bmi is:   {bmi}    and you are obese ')
        elif 35 < bmi:
            messagebox.showinfo('bmi category', f'the number your bmi is:   {bmi}    and you are extremely obese ')



if __name__ == "__main__":
    window = tkinter.Tk()
    app = BMI(window)
    window.mainloop()
