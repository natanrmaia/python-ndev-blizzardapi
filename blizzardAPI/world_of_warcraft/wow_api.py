from .wow_game import WorldOfWarcraft_Game
from .wow_profile import WorldOfWarcraft_Profile


class WoWAPI:
    """
    This is the main class for the World Of Warcraft API. It is used to call the other APIs.

    Attributes:
        :param client_id: The client ID you received from Blizzard
        :param client_secret: The client secret you received from Blizzard
    """

    def __init__(self, client_id, client_secret):
        self.game       = WorldOfWarcraft_Game(client_id, client_secret)
        self.profile    = WorldOfWarcraft_Profile(client_id, client_secret)