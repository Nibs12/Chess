from tkinter import *

root = Tk()
label1 = Label(root, text="ChessMania")
label1.grid(row = 1, column = 250)


playButton = Button(None, text = "Play", fg = "White", bg = "Black")
playButton.grid(row = 2, column = 250)

leaderboardButton = Button(None, text = "Leaderboard", fg = "Black", bg = "White")
leaderboardButton.grid(row = 3, column = 250)

optionsButton = Button(None, text = "Options", fg = "White", bg = "Black")
optionsButton.grid(row = 4, column = 250)

exitButton = Button(None, text = "Exit", fg = "Black", bg = "White")
exitButton.grid(row = 5, column = 250)

root.geometry("200x200")

root.mainloop()
