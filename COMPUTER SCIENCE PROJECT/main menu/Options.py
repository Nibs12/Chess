from tkinter import *

root = Tk()
label1 = Label(root, text="ChessMania")
label1.grid(row = 1, column = 20)


musicButton = Button(None, text = "Music ON/OFF", fg = "White", bg = "Black")
musicButton.grid(row = 2, column = 20)

soundButton = Button(None, text = "Sound ON/OFF", fg = "Black", bg = "White")
soundButton.grid(row = 3, column = 20)

backButton = Button(None, text = "Back", fg = "White", bg = "Black")
backButton.grid(row = 5, column = 20)

root.geometry("200x200")


root.mainloop()
