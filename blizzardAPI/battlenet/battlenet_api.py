from .battlenet_oauth import BattleNetAPI_OAuth

class BattleNetAPI:
    """
    This is the main class for the Battle.net API. It is used to call the other APIs.

    Attributes:
        :param client_id: The client ID you received from Blizzard
        :param client_secret: The client secret you received from Blizzard
    """

    def __init__(self, client_id, client_secret):
        self.oauth = BattleNetAPI_OAuth(client_id, client_secret)