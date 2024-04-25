from typing import Dict, Optional, Any
from ...api import API

class MythicKeystoneLeaderboard(API):

    def __init__(self, client_id, client_secret):
        super().__init__(client_id, client_secret)

    def get_mythic_keystone_leaderboards_index(self, connected_realm_id: int,  **kwargs: Any) -> Dict:
        """
        This function will return the index of mythic keystone leaderboards from the API.

        Requested API:
            /data/wow/connected-realm/{connectedRealmId}/mythic-leaderboard/index

        Args:
            connected_realm_id: The ID of the connected realm you want to retrieve the mythic keystone leaderboards index from.

        Returns:
            A dictionary of the mythic keystone leaderboards index.
        """

        api = f'/data/wow/connected-realm/{connected_realm_id}/mythic-leaderboard/index'

        query_params = {
            'namespace': 'dynamic',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_mythic_keystone_leaderboard(self, connected_realm_id: int, dungeon_id: int, period: int, **kwargs: Any) -> Dict:
        """
        This function will return the details of a specific mythic keystone leaderboard from the API.

        Requested API:
            /data/wow/connected-realm/{connectedRealmId}/mythic-leaderboard/{dungeonId}/period/{period}

        Args:
            connected_realm_id: The ID of the connected realm you want to retrieve the mythic keystone leaderboard from.
            dungeon_id: The ID of the dungeon you want to retrieve the mythic keystone leaderboard from.
            period: The ID of the period you want to retrieve the mythic keystone leaderboard from.

        Returns:
            A dictionary of the mythic keystone leaderboard details.
        """

        api = f'/data/wow/connected-realm/{connected_realm_id}/mythic-leaderboard/{dungeon_id}/period/{period}'

        query_params = {
            'namespace': 'dynamic',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)