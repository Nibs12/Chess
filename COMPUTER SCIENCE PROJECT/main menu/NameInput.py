from tkinter import *

root = Tk()
label1 = Label(root, text="ChessMania")
label1.grid(row = 1, column = 20)

label2 = Label(root, text="Enter your name:")
label2.grid(row = 2, column = 20)

entrySpace = Entry(root)
entrySpace.grid(row = 3, column = 20)

confirmButton = Button(None, text = "Confirm", fg = "White", bg = "Black")
confirmButton.grid(row = 4, column = 20)

root.geometry("200x200")

root.mainloop()
