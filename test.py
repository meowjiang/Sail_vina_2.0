from tkinter import *


class Main(object):
    def __init__(self):
        self.root = Tk()
        e = StringVar()
        entry = Entry(self.root, textvariable=e)
        e.set('Enter your text here!')
        entry.pack()


root = Main()
root.root.mainloop()
