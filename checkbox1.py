from tkinter import *
root = Tk()
var1 = IntVar()
Checkbutton(root, text="hombre",variable=var1).grid(row=0,sticky=W)
var2 = IntVar()
Checkbutton(root,text="mujer",variable=var2).grid(row=1,sticky=W)
root.mainloop()