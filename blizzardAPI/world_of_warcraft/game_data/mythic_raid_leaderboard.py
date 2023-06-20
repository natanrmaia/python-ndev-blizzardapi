# BEGIN: abpxx6d04wxr
from typing import Dict, Optional
from ...api import API

class MythicRaidLeaderboard(API):
    
    def __init__(self, client_id, client_secret):
        super().__init__(client_id, client_secret)


    def get_mythic_raid_leaderboard(self, region: Optional[str], locale: Optional[str], raid: str, faction: str) -> Dict:
        """
        This function will return the details of a specific mythic raid leaderboard from the API.

        Requested API:
            /data/wow/leaderboard/hall-of-fame/{raid}/{faction}

        Args:
            region: The region of the API you want to access.
            locale: The locale of the API you want to access.
            raid: The name of the raid you want to retrieve the mythic raid leaderboard from.
            faction: The faction of the leaderboard you want to retrieve (alliance or horde).

        Returns:
            A dictionary of the mythic raid leaderboard details.
        """

        api = f'/data/wow/leaderboard/hall-of-fame/{raid}/{faction}'

        query_params = {
            'namespace': 'dynamic',
            'locale': locale,
        }

        return super().get_api(region, api, query_params)