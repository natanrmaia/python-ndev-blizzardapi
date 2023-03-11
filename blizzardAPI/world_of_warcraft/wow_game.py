from ..api import API

class WorldOfWarcraft_Game(API):
    
    def __init__(self, client_id, client_secret):
        super().__init__(client_id, client_secret)