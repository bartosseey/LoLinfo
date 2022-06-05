from riotwatcher import LolWatcher, ApiError

class LoLwatcher(): 
    lol_watcher = LolWatcher('RGAPI-9048a62b-72cd-4cd9-b737-fdf58063b789')
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
    def myMatches(self):
        my_matches = self.lol_watcher.match.matchlist_by_puuid(self.region, self.SummonerByName['puuid'])
        last_matches = []
        mypuuid = self.SummonerByName['puuid']
        print(mypuuid)
        for x in range(3):
            last_matches.append(my_matches[x])
        fullmatch_detail0 = self.lol_watcher.match.by_id(self.region, last_matches[0])
        fullmatch_detail1 = self.lol_watcher.match.by_id(self.region, last_matches[1])
        fullmatch_detail2 = self.lol_watcher.match.by_id(self.region, last_matches[2])

        match_detail0 = []
        match_detail1 = []
        match_detail2 = []


        for row in fullmatch_detail0['info']['participants']:
            
            participants_row = {}
            if row['puuid'] == mypuuid:
                participants_row['champion'] = row['championName']
                participants_row['win'] = row['win']
                participants_row['kills'] = row['kills']
                participants_row['deaths'] = row['deaths']
                participants_row['assists'] = row['assists']
                participants_row['totalDamageDealt'] = row['totalDamageDealt']
                participants_row['goldEarned'] = row['goldEarned']
                participants_row['champLevel'] = row['champLevel']
                participants_row['totalMinionsKilled'] = row['totalMinionsKilled']
                participants_row['item0'] = row['item0']
                participants_row['item1'] = row['item1']
                participants_row['item2'] = row['item2']
                participants_row['item3'] = row['item3']
                participants_row['item4'] = row['item4']
                participants_row['item5'] = row['item5']
                participants_row['item6'] = row['item6']
                match_detail0.append(participants_row)
        for row in fullmatch_detail1['info']['participants']:
            participants_row = {}
            if row['puuid'] == mypuuid:
                participants_row['champion'] = row['championName']
                participants_row['win'] = row['win']
                participants_row['kills'] = row['kills']
                participants_row['deaths'] = row['deaths']
                participants_row['assists'] = row['assists']
                participants_row['totalDamageDealt'] = row['totalDamageDealt']
                participants_row['goldEarned'] = row['goldEarned']
                participants_row['champLevel'] = row['champLevel']
                participants_row['totalMinionsKilled'] = row['totalMinionsKilled']
                participants_row['item0'] = row['item0']
                participants_row['item1'] = row['item1']
                participants_row['item2'] = row['item2']
                participants_row['item3'] = row['item3']
                participants_row['item4'] = row['item4']
                participants_row['item5'] = row['item5']
                participants_row['item6'] = row['item6']
                match_detail1.append(participants_row)
        for row in fullmatch_detail2['info']['participants']:
            participants_row = {}
            if row['puuid'] == mypuuid:
                participants_row['champion'] = row['championName']
                participants_row['win'] = row['win']
                participants_row['kills'] = row['kills']
                participants_row['deaths'] = row['deaths']
                participants_row['assists'] = row['assists']
                participants_row['totalDamageDealt'] = row['totalDamageDealt']
                participants_row['goldEarned'] = row['goldEarned']
                participants_row['champLevel'] = row['champLevel']
                participants_row['totalMinionsKilled'] = row['totalMinionsKilled']
                participants_row['item0'] = row['item0']
                participants_row['item1'] = row['item1']
                participants_row['item2'] = row['item2']
                participants_row['item3'] = row['item3']
                participants_row['item4'] = row['item4']
                participants_row['item5'] = row['item5']
                participants_row['item6'] = row['item6']
                match_detail2.append(participants_row)
        last3matches = []
        last3matches.append(match_detail0)
        last3matches.append(match_detail1)
        last3matches.append(match_detail2)
        return last3matches
        

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
