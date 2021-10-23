from tkinter import *
import tkinter as tk
from tkinter import messagebox

mobi = Tk()
mobi.geometry("1500x1000")
mobi.title("Inventory management")

# MainFunct
def process():
    number = str(txtfield1.get())
    name = str(txtfield2.get())
    price = str(txtfield3.get())
    quantity = str(txtfield4.get())

    i = 0
    i = i + 1

    if len(number) == 5:
        check = open('emu.txt', 'a')
        check1 = open('emu.txt', 'r')
        test = check1.read()

        if number in test:
            messagebox.showwarning("title", "number already exists")
        else:
            check.write(f"{i}\t\t   {number}\t\t     {name}\t\t         {price}\t\t           {quantity}\n")
            messagebox.showinfo("Info", "number executed")

    elif number == str(number):
        messagebox.showwarning("Warning", "Enter the correct information")

        txtfield1.delete(0, END)

        txtfield2.delete(0, END)

        txtfield3.delete(0, END)

        txtfield4.delete(0, END)



def checking():
    check = open('emu.txt', 'r')
    rest = check.read()
    for a in rest[::-1]:
        text1.insert(0.0, a)


def clear():
    text1.delete(0.0, END)

Information = Label(mobi, text="Inventory management", font=("times roman now",14 , "bold"))
Information.place(x=10, y=30)

Label1 = Label(mobi, text="Enter id", fg="black", font=("times roman now", 16))
Label1.place(x=10, y=90)
txtfield1 = Entry(mobi, width=30, background="Lightgrey")
txtfield1.place(x=10, y=130)


Label2 = Label(mobi, text="Enter Name : ", fg="black", font=("times roman now", 16))
Label2.place(x=10, y=190)
txtfield2 = Entry(mobi , width=30, background="Lightgrey")
txtfield2.place(x=10, y=230)


Label3 = Label(mobi, text="Enter price : ", fg="black", font=("times roman now", 16))
Label3.place(x=10, y=290)
txtfield3 = Entry(mobi, width=30, background="Lightgrey")
txtfield3.place(x=10, y=330)

Label4 = Label(mobi, text="Enter Quantity : ", fg="black", font=("times roman now",16))
Label4.place(x=10, y=390)
txtfield4 = Entry(mobi, width=30, background="Lightgrey")
txtfield4.place(x=10, y=430)


text1 = tk.Text(mobi, height=22, width=85)
text1.place(x=250, y=90)


Information = Label(mobi, text="Item no", font=("times roman now", 16, "bold"))
Information.place(x=250, y=30)


Information = Label(mobi, text="Product id", font=("times roman now", 16, "bold"))
Information.place(x=400, y=30)


Information = Label(mobi, text="Name", font=("times roman now", 16, "bold"))
Information.place(x=550, y=30)


Information = Label(mobi, text="Selling price", font=("times roman now", 16, "bold"))
Information.place(x=700, y=30)


Information = Label(mobi, text="Quantity", font=("times roman now", 16, "bold"))
Information.place(x=850, y=30)


# sentence = Label(mobi, text="VIEW YOUR INFORMATION", font=("times roman now",14,"bold")).place(x=90,y=310)



submit = Button(mobi,text='Insert', bg='Grey', fg='black', command=process, font=("times roman now", 14, "bold")).place(x=10,y=460)

check = Button(mobi, text="Show", command=checking, background="Grey", fg="black", font=("times roman now", 14, "bold"))
check.place(x=100, y=460)

mobi.mainloop()
