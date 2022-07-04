from tkinter import *

def clicked(): .#
    res = "Привет {}".format(txt.get())
    lbl.configure(text=res)

window = Tk()
window.geometry('800x400')
window.title("testwindow", )
lbl = Label(window, text="testtext  ", font=("Arial Bold", 50))
lbl.grid(column=0, row=0)
txt = Entry(window,width=100)
txt.grid(column=1, row=0)
btn = Button(window,text="dont click!", command=clicked)
btn.grid(column=3, row= 0)
window.mainloop()
