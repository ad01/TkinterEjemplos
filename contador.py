from tkinter import *

counter = 0
def count():
	global counter,label
	counter += 1
	label.config(text=str(counter))
	label.after(1000, count)

root = Tk()
root.title("Contando Segundos")
label = Label(root,fg="green")
label.pack()
count()
button = Button(root, text="Stop", width=25, command=root.destroy)
button.pack()
root.mainloop()

