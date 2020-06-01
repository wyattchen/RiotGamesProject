import requests
import RiotConsts as Consts

class RiotAPI(object):


    def __init__(self, api_key, region=Consts.REGIONS['north_america']):

        self.api_key=api_key
        self.region=region


    def _request(self, api_url, params={}):

        args = {'api_key': self.api_key}

        for key, value in params.items():
            if key not in args:
                args[key] = value
                
        response = requests.get(
            Consts.URL['base'].format(
                proxy=self.region,
                url=api_url
                ),
            params=args
            )
        
        return response.json()

    def get_summoner_by_name(self, name):

        api_url = Consts.URL['summoner_by_name'].format(
            version=Consts.API_VERSIONS['summoner'],
            names=name
            )

        return self._request(api_url)

    def get_champion_mastery(self, name):
        dict1 = self.get_summoner_by_name(name)
        
        e_id=dict1['id']
        api_url = Consts.URL['champion_mastery'].format(
            version=Consts.API_VERSIONS['summoner'],
            encrypted_summoner_id = e_id
            )

        return self._request(api_url)

    def get_league_ranked(self, league, league_tier):

        
        api_url = Consts.URL['league_rank_solo'].format(
            version = Consts.API_VERSIONS['summoner'],
            league = league,
            league_tier = league_tier
            )

        return self._request(api_url)

        
            
        #"summonerName": "C9 ZVENNN",
        #"leaguePoints": 1658,


        
