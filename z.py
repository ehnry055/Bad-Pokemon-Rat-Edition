
# import everything from tkinter module
from tkinter import *
  
root = Tk()
  
root.geometry('430x300')
  
title = Label(root, text="Geeksforgeeks", bg="green", font=("bold", 30))
title.pack()
c = Canvas(root, width=330, height=200, bg="red")
c.place(x=50, y=50)
btn = Button(root, text='Welcome to Tkinter!', width=40,
             height=5, bd='10', command=root.destroy)
  
btn.place(x=65, y=100)
  
root.mainloop()