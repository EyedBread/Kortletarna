from tkinter import *
#from stockChecker import *
#from webFuncs import *

root = Tk()
root.title('Kortletarna')
#root.iconbitmap()

# Creating a Label widget
rubrik = Label(root, text="Kortletarna")
status_log = Label(root, text="Status log:")
empty = Label(root, text=" ")

rubrik.grid(row=0,column=1)
status_log.grid(row=2,column=1)
empty.grid(row=1,column=1)

# Showing it onto the screen
#rubrik.pack()
#status_log.pack()

root.mainloop()