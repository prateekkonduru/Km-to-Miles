from tkinter import *

window=Tk()

def kmtomiles():
    miles = float(e1_value.get())*1.6
    t1.insert(END,miles)

b1 = Button(window,text="Excecute",command=kmtomiles)
b1.grid(row=3,column=2)

e2=Label(window,text="Km")
e2.grid(row=1,column=0)

e1_value = StringVar()
e1 = Entry(window,textvariable=e1_value)
e1.grid(row=1,column=1)

e3=Label(window,text="Miles")
e3.grid(row=1,column=2)

t1 = Text(window,height=1,width=20)
t1.grid(row=1,column=3)

window.mainloop()
