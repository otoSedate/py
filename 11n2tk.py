'''
Created on 19 дек. 2017 г.

@author: Andrey
'''

import math
from tkinter import *
def s():
    x = float(nav.get())
    sv1.config(text=str(3 * (math.log(x)) ** 5))
    sv2.config(text=str(x ** 9))
    sv3.config(text=str(math.cos(x)))
    sv4.config(text=str((3 * (math.log(x)) ** 5) - (x ** 9) - (math.cos(x))))


root = Tk()
root.title('Линейные алгоритмы')
root.resizable(0, 0)
lab1 = Label(root, text="x", font="Arial 18", width=20)
nav = Entry(root, width=20)

st1 = Label(root, text="3ln^5(x)", font="Arial 18", width=20)
st2 = Label(root, text="x^9", font="Arial 18", width=20)
st3 = Label(root, text="cos(x)", font="Arial 18", width=20)
st4 = Label(root, text="y", font="Arial 18", width=20)
sv1 = Label(root, text="", font="Arial 18", width=20)
sv2 = Label(root, text="", font="Arial 18", width=20)
sv3 = Label(root, text="", font="Arial 18", width=20)
sv4 = Label(root, text="", font="Arial 18", width=20)
pick = Button(root,
          text="click",
          width=20,
          height=5,
          bg="black", fg="green", command=s)


lab1.grid(row=0, column=0)
nav.grid(row=0, column=1)

pick.grid(row=0, column=2)
st1.grid(row=1, column=0)
st2.grid(row=1, column=1)
st3.grid(row=1, column=2)
st4.grid(row=1, column=3)
sv1.grid(row=2, column=0)
sv2.grid(row=2, column=1)
sv3.grid(row=2, column=2)
sv4.grid(row=2, column=3)
root.mainloop()
