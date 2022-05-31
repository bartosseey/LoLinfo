from tkinter import *
from typing import List

import RiotWatcher


class Gui:
    def __init__(self, master):
        myFrame = Frame(master)
        myFrame.pack()

        nickname = StringVar()
        self.myLabel = Label(master, text="Enter your summoner name:")
        self.myLabel.pack()

        self.entry = Entry(master, textvariable= nickname)
        self.entry.pack()
        regions = ["EUNE", "EUW", "NA"]
        regions_var = StringVar()
        regions_var.set(regions[0])

        self.list = OptionMenu(master, regions_var, *regions)
        self.list.pack()

        self.button = Button(master, text="View info", command=lambda: self.display(nickname, regions_var))
        self.button.pack()

        self.statLabel = Label(master)
        self.statLabel.pack()


    def display(self, nickname, regions_var):
        name = nickname.get()
        region = regions_var.get()
        me = RiotWatcher.LoLwatcher("eun1", name)
        me.queueTypeInfo
        self.statLabel.config(text=me.statistics)

        print(name)
        print(region)

if __name__=="__main__":
    root = Tk()
    root.title("LoLinfo")
    root.geometry("600x800")
    app = Gui(root)

    root.mainloop()