from tkinter import *

root = Tk()
label1 = Label(root, text="ChessMania")
label1.grid(row = 1, column = 20)


computerButton = Button(None, text = "Computer", fg = "White", bg = "Black")
computerButton.grid(row = 2, column = 20)

playerButton = Button(None, text = "Multiplayer", fg = "Black", bg = "White")
playerButton.grid(row = 3, column = 20)

timedButton = Button(None, text = "Timed game", fg = "White", bg = "Black")
timedButton.grid(row = 4, column = 20)

backButton = Button(None, text = "Back", fg = "Black", bg = "White")
backButton.grid(row = 5, column = 20)

root.geometry("200x200")

root.mainloop()
