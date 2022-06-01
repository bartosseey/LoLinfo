from riotwatcher import LolWatcher, ApiError

class LoLwatcher(): 
    lol_watcher = LolWatcher('RGAPI-41794bad-b047-4f0e-b38c-71ba0b7e659e')
    def __init__(self, region, name):
        self.region = region
        self.name = name
        
    @property
    def SummonerByName(self):
        return self.lol_watcher.summoner.by_name(self.region, self.name)

    @property
    def myRankedStats(self):
        return self.lol_watcher.league.by_summoner(self.region, self.SummonerByName['id'])

    @property
    def queueTypeInfo(self):
        self.soloq = "UNRANKED"
        self.flexq = "UNRANKED"
        for i in range(len(self.myRankedStats)):
            if self.myRankedStats[i]['queueType'] == "RANKED_FLEX_SR":
                self.flexq = self.myRankedStats[i]
            if self.myRankedStats[i]['queueType'] == "RANKED_SOLO_5x5":
                self.soloq = self.myRankedStats[i]

        

    @property
    def statisticsSolo(self):
        if self.soloq=="UNRANKED":
            return "solo rank: UNRANKED"


        if self.soloq:
            self.leaguePointsSolo = self.soloq['leaguePoints']
            self.tierSolo = self.soloq['tier']
            self.rankSolo = self.soloq['rank']
            self.winsSolo = self.soloq['wins']
            self.lossesSolo = self.soloq['losses']
            self.allGamesSolo = self.winsSolo+self.lossesSolo
            self.winratioSolo = (round(self.winsSolo/self.allGamesSolo,2))*100
            return "solo rank: {} {} {} LP \n wins: {} \n losses: {} \n winratio: {} %".format(self.tierSolo, self.rankSolo, self.leaguePointsSolo, self.winsSolo, self.lossesSolo, self.winratioSolo)

    @property
    def statisticsFlex(self):
        if self.flexq == "UNRANKED":
            return "flex rank: UNRANKED"
        if self.flexq:
            self.leaguePointsFlex = self.flexq['leaguePoints']
            self.tierFlex = self.flexq['tier']
            self.rankFlex = self.flexq['rank']
            self.winsFlex = self.flexq['wins']
            self.lossesFlex = self.flexq['losses']
            self.allGamesFlex = self.winsFlex+self.lossesFlex
            self.winratioFlex = (round(self.winsFlex/self.allGamesFlex,2))*100
            return "flex rank: {} {} {} LP \n wins: {} \n losses: {} \n winratio: {} %".format(self.tierFlex, self.rankFlex, self.leaguePointsFlex, self.winsFlex, self.lossesFlex, self.winratioFlex)

       
        