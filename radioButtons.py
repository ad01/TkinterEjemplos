from tkinter import *
root = Tk()
v = IntVar()
v.set(1)
lenguajes = [
	("Python",1),
	("Perl",2),
	("Java",3),
	("C++",4),
	("C",5)
]
def ShowChoice():
	print(v.get())

label = Label(root,text="Escoge un lenguaje de programación",justify = LEFT,padx = 20)
label.pack()
for lenguaje in lenguajes:
	Radiobutton(root,text=lenguaje[0],padx=20,variable=v,value=lenguaje[1],command=ShowChoice).pack(anchor=W)
#Radiobutton(root,text="Perl",padx=20,variable=v,value=2).pack(anchor=W)	
root.mainloop()