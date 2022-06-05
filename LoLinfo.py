from cProfile import label
from re import L
from tkinter import *
from turtle import back
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

        self.champion1IconLabel=Label(master)
        self.champion1IconLabel.configure(background='black')
        self.champion1IconLabel.place(relx=0.05, rely=0.45, anchor='w')

        self.champion2IconLabel=Label(master)
        self.champion2IconLabel.configure(background='black')
        self.champion2IconLabel.place(relx=0.05, rely=0.65, anchor='w')

        self.champion3IconLabel=Label(master)
        self.champion3IconLabel.configure(background='black')
        self.champion3IconLabel.place(relx=0.05, rely=0.85, anchor='w')


        self.championName1Label = Label(master)
        self.championName1Label.configure(background='black', fg='white', font=("Roboto",15))
        self.championName1Label.place(relx=0.19, rely=0.41, anchor='w')

        self.championName2Label = Label(master)
        self.championName2Label.configure(background='black', fg='white', font=("Roboto",15))
        self.championName2Label.place(relx=0.19, rely=0.61, anchor='w')

        self.championName3Label = Label(master)
        self.championName3Label.configure(background='black', fg='white', font=("Roboto",15))
        self.championName3Label.place(relx=0.19, rely=0.81, anchor='w')


        self.winOrLoseLabel1 = Label(master)
        self.winOrLoseLabel1.configure(background='black', fg='white', font=("Roboto",14))
        self.winOrLoseLabel1.place(relx=0.08, rely=0.51, anchor='w')

        self.winOrLoseLabel2 = Label(master)
        self.winOrLoseLabel2.configure(background='black', fg='white', font=("Roboto",14))
        self.winOrLoseLabel2.place(relx=0.08, rely=0.71, anchor='w')

        self.winOrLoseLabel3 = Label(master)
        self.winOrLoseLabel3.configure(background='black', fg='white', font=("Roboto",14))
        self.winOrLoseLabel3.place(relx=0.08, rely=0.91, anchor='w')


        self.kda1Label = Label(master)
        self.kda1Label.configure(background='black', fg='white', font=("Roboto",15))
        self.kda1Label.place(relx=0.19, rely=0.44, anchor='w')

        self.kda2Label = Label(master)
        self.kda2Label.configure(background='black', fg='white', font=("Roboto",15))
        self.kda2Label.place(relx=0.19, rely=0.64, anchor='w')

        self.kda3Label = Label(master)
        self.kda3Label.configure(background='black', fg='white', font=("Roboto",15))
        self.kda3Label.place(relx=0.19, rely=0.84, anchor='w')

        self.kda1RatioLabel = Label(master)
        self.kda1RatioLabel.configure(background='black', fg='white', font=("Roboto",13))
        self.kda1RatioLabel.place(relx=0.19, rely=0.465, anchor='w')

        self.kda2RatioLabel = Label(master)
        self.kda2RatioLabel.configure(background='black', fg='white', font=("Roboto",13))
        self.kda2RatioLabel.place(relx=0.19, rely=0.665, anchor='w')

        self.kda3RatioLabel = Label(master)
        self.kda3RatioLabel.configure(background='black', fg='white', font=("Roboto",13))
        self.kda3RatioLabel.place(relx=0.19, rely=0.865, anchor='w')

        self.cs1Label = Label(master)
        self.cs1Label.configure(background='black', fg='white', font=("Roboto",12))
        self.cs1Label.place(relx=0.82, rely=0.42, anchor='e')
        
        self.cs2Label = Label(master)
        self.cs2Label.configure(background='black', fg='white', font=("Roboto",12))
        self.cs2Label.place(relx=0.82, rely=0.62, anchor='e')

        self.cs3Label = Label(master)
        self.cs3Label.configure(background='black', fg='white', font=("Roboto",12))
        self.cs3Label.place(relx=0.82, rely=0.82, anchor='e')


        self.time1Label = Label(master)
        self.time1Label.configure(background='black', fg='white', font=("Roboto",12))
        self.time1Label.place(relx=0.95, rely=0.42, anchor='e')

        self.time2Label = Label(master)
        self.time2Label.configure(background='black', fg='white', font=("Roboto",12))
        self.time2Label.place(relx=0.95, rely=0.62, anchor='e')

        self.time3Label = Label(master)
        self.time3Label.configure(background='black', fg='white', font=("Roboto",12))
        self.time3Label.place(relx=0.95, rely=0.82, anchor='e')

        self.totalDMG1Label = Label(master) 
        self.totalDMG1Label.configure(background='black', fg='white', font=("Roboto",12)) 
        self.totalDMG1Label.place(relx=0.82, rely=0.445, anchor='e')

        self.totalDMG2Label = Label(master) 
        self.totalDMG2Label.configure(background='black', fg='white', font=("Roboto",12)) 
        self.totalDMG2Label.place(relx=0.82, rely=0.645, anchor='e')

        self.totalDMG3Label = Label(master) 
        self.totalDMG3Label.configure(background='black', fg='white', font=("Roboto",12)) 
        self.totalDMG3Label.place(relx=0.82, rely=0.845, anchor='e')


        self.totalGold1Label = Label(master)
        self.totalGold1Label.configure(background='black', fg='white', font=("Roboto",12))
        self.totalGold1Label.place(relx=0.82, rely=0.47, anchor='e')

        self.totalGold2Label = Label(master)
        self.totalGold2Label.configure(background='black', fg='white', font=("Roboto",12))
        self.totalGold2Label.place(relx=0.82, rely=0.67, anchor='e')

        self.totalGold3Label = Label(master)
        self.totalGold3Label.configure(background='black', fg='white', font=("Roboto",12))
        self.totalGold3Label.place(relx=0.82, rely=0.87, anchor='e')

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
        self.showChampionIcon(last3matches)
        self.showChampionName(last3matches)
        self.winLose(last3matches)
        self.showKDA(last3matches)
        self.showCS(last3matches)
        self.showTime(last3matches)
        self.showDMG(last3matches)
        self.showGold(last3matches)
        


    def showChampionIcon(self, last3matches):
        championIcon0="12.6.1\\img\\champion\\" + last3matches[0][0]['champion']+".png"
        championIcon1="12.6.1\\img\\champion\\" + last3matches[1][0]['champion']+".png"
        championIcon2="12.6.1\\img\\champion\\" + last3matches[2][0]['champion']+".png"

        img0 = Image.open(championIcon0)
        img0 = img0.resize((80,80))
        test0 = ImageTk.PhotoImage(img0)
        img1 = Image.open(championIcon1)
        img1 = img1.resize((80,80))
        test1 = ImageTk.PhotoImage(img1)
        img2 = Image.open(championIcon2)
        img2 = img2.resize((80,80))
        test2 = ImageTk.PhotoImage(img2)

        self.champion1IconLabel.config(image=test0)
        self.champion1IconLabel.image = test0

        self.champion2IconLabel.config(image=test1)
        self.champion2IconLabel.image = test1

        self.champion3IconLabel.config(image=test2)
        self.champion3IconLabel.image = test2

    def showChampionName(self, last3matches):
        champion1 = last3matches[0][0]['champion']
        champion2 = last3matches[1][0]['champion']
        champion3 = last3matches[2][0]['champion']

        self.championName1Label.configure(text=champion1)
        self.championName2Label.configure(text=champion2)
        self.championName3Label.configure(text=champion3)


    def winLose(self, last3matches):
        win1 = last3matches[0][0]['win']
        win2 = last3matches[1][0]['win']
        win3 = last3matches[2][0]['win']

        if win1 == True:
            self.winOrLoseLabel1.configure(text='WIN', fg="green")
        else:
            self.winOrLoseLabel1.configure(text='LOSE',fg="red")
            
        if win2 == True:
            self.winOrLoseLabel2.configure(text='WIN', fg="green")
        else:
            self.winOrLoseLabel2.configure(text='LOSE',fg="red")

        if win3 == True:
            self.winOrLoseLabel3.configure(text='WIN',fg="green")
        else:
            self.winOrLoseLabel3.configure(text='LOSE',fg="red")

    def showKDA(self, last3matches):
        kda1 = str(last3matches[0][0]['kills']) + "/"+ str(last3matches[0][0]['deaths']) + "/" + str(last3matches[0][0]['assists'])
        kda2 = str(last3matches[1][0]['kills']) + "/"+ str(last3matches[1][0]['deaths']) + "/" + str(last3matches[1][0]['assists'])
        kda3 = str(last3matches[2][0]['kills']) + "/"+ str(last3matches[2][0]['deaths']) + "/" + str(last3matches[2][0]['assists'])

        self.kda1Label.configure(text=kda1)
        self.kda2Label.configure(text=kda2)
        self.kda3Label.configure(text=kda3)

        kda1Ratio = str(round((last3matches[0][0]['kills']+last3matches[0][0]['assists'])/last3matches[0][0]['deaths'],2)) + " KDA"
        kda2Ratio = str(round((last3matches[1][0]['kills']+last3matches[1][0]['assists'])/last3matches[1][0]['deaths'],2)) + " KDA"
        kda3Ratio = str(round((last3matches[2][0]['kills']+last3matches[2][0]['assists'])/last3matches[2][0]['deaths'],2)) + " KDA"

        self.kda1RatioLabel.configure(text=kda1Ratio)
        self.kda2RatioLabel.configure(text=kda2Ratio)
        self.kda3RatioLabel.configure(text=kda3Ratio)
    
    def showCS(self, last3matches):
        cs1 = str(last3matches[0][0]['totalMinionsKilled']) + " CS"
        cs2 = str(last3matches[1][0]['totalMinionsKilled'])+ " CS"
        cs3 = str(last3matches[2][0]['totalMinionsKilled'])+ " CS"

        self.cs1Label.configure(text=cs1)
        self.cs2Label.configure(text=cs2)
        self.cs3Label.configure(text=cs3)

    def showTime(self, last3matches):
        time1=last3matches[0][0]['time']
        time2=last3matches[1][0]['time']
        time3=last3matches[2][0]['time']

        self.time1Label.configure(text=time1)
        self.time2Label.configure(text=time2)
        self.time3Label.configure(text=time3)

    def showDMG(self, last3matches):
        dmg1=str(last3matches[0][0]['totalDamageDealtToChampions'])+" DMG"
        dmg2=str(last3matches[1][0]['totalDamageDealtToChampions'])+" DMG"
        dmg3=str(last3matches[2][0]['totalDamageDealtToChampions'])+" DMG"

        self.totalDMG1Label.configure(text=dmg1)
        self.totalDMG2Label.configure(text=dmg2)
        self.totalDMG3Label.configure(text=dmg3)

    def showGold(self, last3matches):
        gold1=str(last3matches[0][0]['goldEarned']) + " gold"
        gold2=str(last3matches[1][0]['goldEarned']) + " gold"
        gold3=str(last3matches[2][0]['goldEarned']) + " gold"

        self.totalGold1Label.configure(text= gold1)
        self.totalGold2Label.configure(text= gold2)
        self.totalGold3Label.configure(text= gold3)

if __name__=="__main__":
    root = Tk()
    root.title("LoLinfo")
    root.geometry("600x800")
    root.resizable(False, False)
    root.configure(bg="black")
    app = Gui(root)

    root.mainloop()