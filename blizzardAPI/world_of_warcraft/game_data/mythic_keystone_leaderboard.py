from typing import Dict, Optional
from ...api import API

class MythicKeystoneLeaderboard(API):
    
    def __init__(self, client_id, client_secret):
        super().__init__(client_id, client_secret)

    def get_mythic_keystone_leaderboards_index(self, region: Optional[str], locale: Optional[str], connected_realm_id: int) -> Dict:
        """
        This function will return the index of mythic keystone leaderboards from the API.

        Requested API:
            /data/wow/connected-realm/{connectedRealmId}/mythic-leaderboard/index

        Args:
            region: The region of the API you want to access.
            locale: The locale of the API you want to access.
            connected_realm_id: The ID of the connected realm you want to retrieve the mythic keystone leaderboards index from.

        Returns:
            A dictionary of the mythic keystone leaderboards index.
        """

        api = f'/data/wow/connected-realm/{connected_realm_id}/mythic-leaderboard/index'

        query_params = {
            'namespace': 'dynamic',
            'locale': locale,
        }

        return super().get_api(region, api, query_params)

    def get_mythic_keystone_leaderboard(self, region: Optional[str], locale: Optional[str], connected_realm_id: int, dungeon_id: int, period: int) -> Dict:
        """
        This function will return the details of a specific mythic keystone leaderboard from the API.

        Requested API:
            /data/wow/connected-realm/{connectedRealmId}/mythic-leaderboard/{dungeonId}/period/{period}

        Args:
            region: The region of the API you want to access.
            locale: The locale of the API you want to access.
            connected_realm_id: The ID of the connected realm you want to retrieve the mythic keystone leaderboard from.
            dungeon_id: The ID of the dungeon you want to retrieve the mythic keystone leaderboard from.
            period: The ID of the period you want to retrieve the mythic keystone leaderboard from.

        Returns:
            A dictionary of the mythic keystone leaderboard details.
        """

        api = f'/data/wow/connected-realm/{connected_realm_id}/mythic-leaderboard/{dungeon_id}/period/{period}'

        query_params = {
            'namespace': 'dynamic',
            'locale': locale,
        }

        return super().get_api(region, api, query_params)