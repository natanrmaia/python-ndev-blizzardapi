from .battlenet.battlenet_api   import BattleNetAPI
from .diablo3                   import D3API
from .diablo4                   import D4API
from .hearthstone               import HSAPI
from .overwatch_league          import OWLAPI
from .starcraft2                import SC2API
from .world_of_warcraft         import WoWAPI

class BlizzardAPI:
    
    def __init__(self, client_id, client_secret):

        self.bnet   = BattleNetAPI(client_id, client_secret)
        # self.wow    = WoWAPI(client_id, client_secret)
        # self.sc2    = SC2API(client_id, client_secret)
        # self.d3     = D3API(client_id, client_secret)
        # self.wtcg   = WTCGAPI(client_id, client_secret)