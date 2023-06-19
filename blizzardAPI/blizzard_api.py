from .battlenet.battlenet_api   import BattleNetAPI
from .world_of_warcraft.wow_api import WoWAPI
# from .diablo3                   import D3API
# from .diablo4                   import D4API
# from .hearthstone               import HSAPI
# from .overwatch_league          import OWLAPI
# from .starcraft2                import SC2API

class BlizzardAPI:
    
    def __init__(self, client_id, client_secret):

        self.bnet   = BattleNetAPI(client_id, client_secret)
        self.wow    = WoWAPI(client_id, client_secret)