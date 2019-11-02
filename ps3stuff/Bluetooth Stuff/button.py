from tkinter import *

master = Tk()

def bye():
    print("bye")

button = Button(master, text="bye", command=bye)

button.pack()

mainloop()
