from .game_data     import Game
from .profile_data  import Profile

class WoWAPI:
    """
    This is the main class for the World Of Warcraft API. It is used to call the other APIs.

    Attributes:
        :param client_id: The client ID you received from Blizzard
        :param client_secret: The client secret you received from Blizzard
    """

    def __init__(self, client_id, client_secret):

        self.game       = Game(client_id, client_secret)
        self.profile    = Profile(client_id, client_secret)