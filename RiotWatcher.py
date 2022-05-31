from riotwatcher import LolWatcher, ApiError

class LoLwatcher(): 
    lol_watcher = LolWatcher('RGAPI-5347f8d2-e124-401e-bbad-0d52aef74900')
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
        if len(self.myRankedStats)==2:
            self.ranks = "both"
            self.flexq = self.myRankedStats[0]
            self.soloq = self.myRankedStats[1]
        elif len(self.myRankedStats)==1 and self.myRankedStats[0]['queueType']=="RANKED_FLEX_SR":
            self.ranks = "flex"
            self.flexq = self.myRankedStats[0]
            self.soloq = "UNRANKED"
        elif len(self.myRankedStats)==1 and self.myRankedStats[0]['queueType']=="RANKED_SOLO_5x5":
            self.ranks = "solo"
            self.soloq = self.myRankedStats[0]
            self.flexq = "UNRANKED"

    @property
    def statistics(self):
        if self.ranks == "both":
            self.leaguePointsFlex = self.myRankedStats[0]['leaguePoints']
            self.tierFlex = self.myRankedStats[0]['tier']
            self.rankFlex = self.myRankedStats[0]['rank']
            self.winsFlex = self.myRankedStats[0]['wins']
            self.lossesFlex = self.myRankedStats[0]['losses']
            self.allGamesFlex = self.winsFlex+self.lossesFlex
            self.winratioFlex = round(self.winsFlex/self.allGamesFlex,2)

            self.leaguePointsSolo = self.myRankedStats[1]['leaguePoints']
            self.tierSolo = self.myRankedStats[1]['tier']
            self.rankSolo = self.myRankedStats[1]['rank']
            self.winsSolo = self.myRankedStats[1]['wins']
            self.lossesSolo = self.myRankedStats[1]['losses']
            self.allGamesSolo = self.winsSolo+self.lossesSolo
            self.winratioSolo = round(self.winsSolo/self.allGamesSolo,2)
            return "flex rank: {} {} {} LP, wins: {}, losses: {}, winratio: {} \nsolo rank: {} {} {} LP, wins: {}, losses: {}, winratio: {}".format(self.tierFlex, self.rankFlex, self.leaguePointsFlex, self.winsFlex, self.lossesFlex, self.winratioFlex, self.tierSolo, self.rankSolo, self.leaguePointsSolo, self.winsSolo, self.lossesSolo, self.winratioSolo)
       
       
        elif self.ranks == "flex":
            self.leaguePointsFlex = self.myRankedStats[0]['leaguePoints']
            self.tierFlex = self.myRankedStats[0]['tier']
            self.rankFlex = self.myRankedStats[0]['rank']
            self.winsFlex = self.myRankedStats[0]['wins']
            self.lossesFlex = self.myRankedStats[0]['losses']
            self.allGamesFlex = self.winsFlex+self.lossesFlex
            self.winratioFlex = round(self.winsFlex/self.allGamesFlex,2)
            return "flex rank: {} {} {} LP, wins: {}, losses: {}, winratio: {} \nsolo rank: UNRANKED".format(self.tierFlex, self.rankFlex, self.leaguePointsFlex, self.winsFlex, self.lossesFlex, self.winratioFlex)

        elif self.ranks == "solo":
            self.leaguePointsSolo = self.myRankedStats[0]['leaguePoints']
            self.tierSolo = self.myRankedStats[0]['tier']
            self.rankSolo = self.myRankedStats[0]['rank']
            self.winsSolo = self.myRankedStats[0]['wins']
            self.lossesSolo = self.myRankedStats[0]['losses']
            self.allGamesSolo = self.winsSolo+self.lossesSolo
            self.winratioSolo = round(self.winsSolo/self.allGamesSolo,2)
            return "flex rank: UNRANKED \nsolo rank: {} {} {} LP, wins: {}, losses: {}, winratio: {}".format(self.tierSolo, self.rankSolo, self.leaguePointsSolo, self.winsSolo, self.lossesSolo, self.winratioSolo)
