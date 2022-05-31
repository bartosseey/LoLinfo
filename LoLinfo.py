from tkinter import *
from typing import List
from riotwatcher import LolWatcher, ApiError

import RiotWatcher


class Gui:
    def __init__(self, master):
        myFrame = Frame(master)
        myFrame.pack()

        nickname = StringVar()
        self.myLabel = Label(master, text="Enter your summoner name:")
        self.myLabel.configure(background='black', fg='white')
        self.myLabel.pack(pady=5)

        self.entry = Entry(master, textvariable= nickname)
        self.entry.pack(pady=5)
        regions = ["EUNE", "EUW", "NA"]
        regions_var = StringVar()
        regions_var.set(regions[0])

        self.list = OptionMenu(master, regions_var, *regions)
        self.list.pack(pady=5)

        self.button = Button(master, text="View info", command=lambda: self.display(nickname, regions_var))
        self.button.pack(pady=5)

        self.statLabel = Label(master)
        self.statLabel.configure(background='black', fg='white')
        self.statLabel.pack(pady=5)


    def display(self, nickname, regions_var):
        name = nickname.get()
        region = regions_var.get()
        regionDict = {"EUNE":"eun1", "EUW":"euw1", "NA":"na1"}
        try:
            me = RiotWatcher.LoLwatcher(regionDict[region], name)
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
            else:
                raise

        print(name)
        print(region)

if __name__=="__main__":
    root = Tk()
    root.title("LoLinfo")
    root.geometry("600x800")
    root.configure(bg="black")
    app = Gui(root)

    root.mainloop()