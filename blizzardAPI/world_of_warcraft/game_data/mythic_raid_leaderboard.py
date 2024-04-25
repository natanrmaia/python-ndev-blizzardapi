# BEGIN: abpxx6d04wxr
from typing import Dict, Optional, Any
from ...api import API

class MythicRaidLeaderboard(API):

    def __init__(self, client_id, client_secret):
        super().__init__(client_id, client_secret)


    def get_mythic_raid_leaderboard(self, raid: str, faction: str, **kwargs: Any) -> Dict:
        """
        This function will return the details of a specific mythic raid leaderboard from the API.

        Requested API:
            /data/wow/leaderboard/hall-of-fame/{raid}/{faction}

        Args:
            raid: The name of the raid you want to retrieve the mythic raid leaderboard from.
            faction: The faction of the leaderboard you want to retrieve (alliance or horde).

        Returns:
            A dictionary of the mythic raid leaderboard details.
        """

        if raid is None:
            raise ValueError('raid is required')

        if faction is None:
            raise ValueError('faction is required')

        api = f'/data/wow/leaderboard/hall-of-fame/{raid}/{faction}'

        query_params = {
            'namespace': 'dynamic',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)