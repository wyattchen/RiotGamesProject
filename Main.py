from RiotAPI import RiotAPI

def main():

    api=RiotAPI('RGAPI-d7235ad7-1bb9-4176-a8ff-e1a41454dd7c')

    #r= api.get_champion_mastery('eggsdeeeee')

    rankList= api.get_league_ranked('SILVER', 'III')

    i=1
    for rankDict in rankList:
        print(i,": ",rankDict['summonerName'])
        print("points: ",rankDict['leaguePoints'])
        if i==50:
            break
        
        i+=1

if __name__ == "__main__":
    main()
