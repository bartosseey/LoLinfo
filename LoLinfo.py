from tkinter import *
from typing import List
from riotwatcher import LolWatcher, ApiError
from PIL import ImageTk, Image
from os import *

import RiotWatcher


class Gui:
    def __init__(self, master):
        myFrame = Frame(master)
        myFrame.pack()

        nickname = StringVar()
        self.myLabel = Label(master, text="Enter your summoner name:")
        self.myLabel.configure(background='black', fg='white', font=("Roboto",12) )
        self.myLabel.pack(pady=5)

        self.entry = Entry(master, textvariable= nickname)
        self.entry.configure(font=("Roboto, 10"))
        self.entry.pack(pady=5)
        regions = ["EUNE", "EUW", "NA"]
        regions_var = StringVar()
        regions_var.set(regions[0])

        self.list = OptionMenu(master, regions_var, *regions)
        self.list.pack(pady=5)

        self.button = Button(master, text="View info", command=lambda: self.display(nickname, regions_var))
        self.button.pack(pady=5)

        self.iconLabel = Label(master)
        self.iconLabel.configure(background='black')
        self.iconLabel.pack(pady=5)

        self.nameLabel = Label(master)
        self.nameLabel.configure(background='black', fg='white', font=("Roboto",13))
        self.nameLabel.pack()

        self.statLabel = Label(master)
        self.statLabel.configure(background='black', fg='white', font=("Roboto",13))
        self.statLabel.pack(pady=5)

        


    def display(self, nickname, regions_var):
        name = nickname.get()
        region = regions_var.get()
        regionDict = {"EUNE":"eun1", "EUW":"euw1", "NA":"na1"}
        me = RiotWatcher.LoLwatcher(regionDict[region], name)
        print(name)
        print(region)
        self.showStats(me, region)
        self.showProfile(me, name)


    def showProfile(self, me, name):
        iconID = me.SummonerByName['profileIconId']
        iconIDpath = "12.6.1\\img\\profileicon\\" + str(iconID)+".png"
        img = Image.open(iconIDpath)
        img = img.resize((80,80))
        test = ImageTk.PhotoImage(img)

        self.iconLabel.config(image=test)
        self.iconLabel.image = test

        self.nameLabel.config(text=name)

    def showStats(self, me, region):
        try:
            me.queueTypeInfo
            self.statLabel.config(text=me.statistics)
        except ApiError as err:
            if err.response.status_code == 429:
                self.statLabel.config(text="Too many requests. Try again later!")
                print('We should retry in {} seconds.'.format(err.headers['Retry-After']))
                print('this retry-after is handled by default by the RiotWatcher library')
                print('future requests wait until the retry-after time passes')
            elif err.response.status_code == 404:
                self.statLabel.config(text='Summoner with that ridiculous name not found.')



if __name__=="__main__":
    root = Tk()
    root.title("LoLinfo")
    root.geometry("600x800")
    root.configure(bg="black")
    app = Gui(root)

    root.mainloop()