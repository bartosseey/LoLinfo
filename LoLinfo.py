from tkinter import *
from typing import List
from riotwatcher import LolWatcher, ApiError
from PIL import ImageTk, Image
from os import *

import RiotWatcher


class Gui:
    def __init__(self, master):
        #myFrame = Frame(master)
        #myFrame.pack()

        nickname = StringVar()
        self.myLabel = Label(master, text="Enter your summoner name:")
        self.myLabel.configure(background='black', fg='white', font=("Roboto",14))
        self.myLabel.place(relx=0.5, rely=0, anchor='n')

        self.entry = Entry(master, textvariable= nickname)
        self.entry.configure(font=("Roboto, 17"), justify='center' )
        self.entry.place(relx=0.3, rely=0.05, anchor='n')
        regions = ["EUNE", "EUW", "NA"]
        regions_var = StringVar()
        regions_var.set(regions[0])

        self.list = OptionMenu(master, regions_var, *regions)
        self.list.configure(font=("Roboto, 10"))
        self.list.place(relx=0.61, rely=0.05, anchor='n')

        self.button = Button(master, text="View stats", command=lambda: self.display(nickname, regions_var))
        self.button.configure(font=("Roboto, 12"))
        self.button.place(relx=0.78, rely=0.05, anchor='n')

        self.iconLabel = Label(master)
        self.iconLabel.configure(background='black')
        self.iconLabel.place(relx=0.5, rely=0.1, anchor="n")

        self.nameLabel = Label(master)
        self.nameLabel.configure(background='black', fg='white', font=("Roboto",13))
        self.nameLabel.place(relx=0.5, rely=0.2, anchor="n")

        self.soloqLabel = Label(master)
        self.soloqLabel.configure(background='black', fg='white', font=("Roboto",11))
        self.soloqLabel.place(relx=0.7, rely=0.25, anchor="n")

        self.flexqLabel = Label(master)
        self.flexqLabel.configure(background='black', fg='white', font=("Roboto",11))
        self.flexqLabel.place(relx=0.3, rely=0.25, anchor="n")

        


    def display(self, nickname, regions_var):
        name = nickname.get()
        region = regions_var.get()
        regionDict = {"EUNE":"eun1", "EUW":"euw1", "NA":"na1"}
        me = RiotWatcher.LoLwatcher(regionDict[region], name)
        print(name)
        print(region)
        self.showStatsSolo(me)
        self.showStatsFlex(me)
        self.showProfile(me, name)
        self.showLastGames(me)


    def showProfile(self, me, name):
        iconID = me.SummonerByName['profileIconId']
        iconIDpath = "12.6.1\\img\\profileicon\\" + str(iconID)+".png"
        img = Image.open(iconIDpath)
        img = img.resize((80,80))
        test = ImageTk.PhotoImage(img)

        self.iconLabel.config(image=test)
        self.iconLabel.image = test

        self.nameLabel.config(text=name)

    def showStatsSolo(self, me):
        try:
            me.queueTypeInfo
            self.soloqLabel.config(text=me.statisticsSolo)
        except ApiError as err:
            if err.response.status_code == 429:
                self.soloqLabel.config(text="Too many requests. Try again later!")
                print('We should retry in {} seconds.'.format(err.headers['Retry-After']))
                print('this retry-after is handled by default by the RiotWatcher library')
                print('future requests wait until the retry-after time passes')
            elif err.response.status_code == 404:
                self.soloqLabel.config(text='Summoner with that ridiculous name not found.')
    
    
    def showStatsFlex(self, me):
        try:
            me.queueTypeInfo
            self.flexqLabel.config(text=me.statisticsFlex)
        except ApiError as err:
            if err.response.status_code == 429:
                self.flexqLabel.config(text="Too many requests. Try again later!")
                print('We should retry in {} seconds.'.format(err.headers['Retry-After']))
                print('this retry-after is handled by default by the RiotWatcher library')
                print('future requests wait until the retry-after time passes')
            elif err.response.status_code == 404:
                self.flexqLabel.config(text='Summoner with that ridiculous name not found.')

    def showLastGames(self, me):
        last3matches = me.myMatches
        print(last3matches)

    


if __name__=="__main__":
    root = Tk()
    root.title("LoLinfo")
    root.geometry("600x800")
    root.resizable(False, False)
    root.configure(bg="black")
    app = Gui(root)

    root.mainloop()