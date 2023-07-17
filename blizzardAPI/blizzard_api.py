from typing import Optional, Dict, Any 
import os
from dotenv                     import load_dotenv

from .battlenet.battlenet_api   import BattleNetAPI
from .world_of_warcraft.wow_api import WoWAPI
# from .diablo3                   import D3API
# from .diablo4                   import D4API
# from .hearthstone               import HSAPI
# from .overwatch_league          import OWLAPI
# from .starcraft2                import SC2API



class BlizzardAPI:
    
    def __init__(self, client_id: Optional[Any] = None, client_secret: Optional[Any] = None):

        if client_id is None and client_secret is None:
            load_dotenv()
            client_id_env       = os.getenv('BLIZZARD_API_CLIENT_ID') or None
            client_secret_env   = os.getenv('BLIZZARD_API_CLIENT_SECRET') or None

            if client_id_env is None and client_secret_env is None:
                raise ValueError('client_id and client_secret are required')
            else:
                client_id       = client_id_env
                client_secret   = client_secret_env

        elif client_id is None and client_secret is not None:
            raise ValueError('client_id is required')
            
        elif client_id is not None and client_secret is None:
            raise ValueError('client_secret is required')        

        self.bnet   = BattleNetAPI(client_id, client_secret)
        self.wow    = WoWAPI(client_id, client_secret)