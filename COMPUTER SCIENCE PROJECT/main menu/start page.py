import tkinter as tk

LARGE_FONT = ("Chiller", 30)
SMALL_FONT = ("Verdana", 15)

class SeaofBTCapp(tk.Tk):

    def __init__(self,*args,**kwargs):

        tk.Tk.__init__(self,*args,**kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill= "both", expand = True)

        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        self.frames = {}

        for F in (StartPage, Play, Leaderboard, Options, GameModes):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()



class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label1 = tk.Label(self, text="ChessMania", font = LARGE_FONT)
        label1.pack(pady=10, padx=10)

        playButton = tk.Button(self, text = "Play", fg = "White", bg = "Black",font = SMALL_FONT,
                               command= lambda: controller.show_frame(Play))
        playButton.pack(pady=10, padx=10)


        leaderboardButton = tk.Button(self, text = "Leaderboard", fg = "Black", bg = "White",font = SMALL_FONT,
                                      command= lambda: controller.show_frame(Leaderboard))
        leaderboardButton.pack(pady=10, padx=10)

        optionsButton = tk.Button(self, text = "Options", fg = "White", bg = "Black",font = SMALL_FONT,
                                  command= lambda: controller.show_frame(Options))
        optionsButton.pack(pady=10, padx=10)

        exitButton = tk.Button(self, text = "Exit", fg = "Black", bg = "White",font = SMALL_FONT)
        exitButton.pack(pady=10, padx=10)

class Play(tk.Frame):

    def __init__(self,parent, controller):
        tk.Frame.__init__(self,parent)
        label2 = tk.Label(self, text="ChessMania", font = LARGE_FONT)
        label2.pack(pady=10, padx=10)

        name = tk.Label(self, text="Enter your name:",font = SMALL_FONT)
        name.pack(pady=10, padx=10)

        entrySpace = tk.Entry(self)
        entrySpace.pack(pady=10, padx=10)

        confirmButton = tk.Button(self, text = "Confirm", fg = "White", bg = "Black",font = SMALL_FONT,
                                  command= lambda: controller.show_frame(GameModes))
        confirmButton.pack(pady=10, padx=10)

        back1Button = tk.Button(self, text = "Back", fg = "White", bg = "Black",font = SMALL_FONT,
                               command= lambda: controller.show_frame(StartPage))
        back1Button.pack()


class GameModes(tk.Frame):

    def __init__(self,parent, controller):
        tk.Frame.__init__(self,parent)
        label1 = tk.Label(self, text="ChessMania", font = LARGE_FONT)
        label1.pack(pady=10, padx=10)


        computerButton = tk.Button(self, text = "Computer", fg = "White", bg = "Black",font = SMALL_FONT)
        computerButton.pack(pady=10, padx=10)

        playerButton = tk.Button(self, text = "Multiplayer", fg = "Black", bg = "White",font = SMALL_FONT)
        playerButton.pack(pady=10, padx=10)

        timedButton = tk.Button(self, text = "Timed game", fg = "White", bg = "Black",font = SMALL_FONT)
        timedButton.pack(pady=10, padx=10)

        backButton =tk.Button(self, text = "Back", fg = "Black", bg = "White",font = SMALL_FONT,
                              command= lambda: controller.show_frame(Play))
        backButton.pack()


class Leaderboard(tk.Frame):

    def __init__(self,parent, controller):
        tk.Frame.__init__(self,parent)

        back2Button = tk.Button(self, text = "Back", fg = "White", bg = "Black",font = SMALL_FONT,
                               command= lambda: controller.show_frame(StartPage))
        back2Button.pack()

class Options(tk.Frame):

    def __init__(self,parent, controller):
        tk.Frame.__init__(self,parent)
        label3 = tk.Label(self, text="ChessMania", font = LARGE_FONT)
        label3.pack(pady=10, padx=10)

        musicButton = tk.Button(self, text = "Music ON/OFF", fg = "White", bg = "Black",font = SMALL_FONT)
        musicButton.pack(pady=10, padx=10)

        soundButton = tk.Button(self, text = "Sound ON/OFF", fg = "Black", bg = "White",font = SMALL_FONT)
        soundButton.pack(pady=10, padx=10)

        back3Button = tk.Button(self, text = "Back", fg = "White", bg = "Black",font = SMALL_FONT,
                               command= lambda: controller.show_frame(StartPage))
        back3Button.pack()


app = SeaofBTCapp()
app.mainloop()
