from typing import Optional, Dict, Any
from ...api import API

class PvPSeason(API):

    def __init__(self, client_id, client_secret):
        super().__init__(client_id, client_secret)

    def get_pvp_seasons_index(self, **kwargs: Any) -> Dict:
        """
        This function will return the index of PvP seasons from the API.

        Requested API:
            /data/wow/pvp-season/index

        Returns:
            A dictionary of the PvP seasons index.
        """

        api = '/data/wow/pvp-season/index'

        query_params = {
            'namespace': 'dynamic',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_pvp_season(self, pvp_season_id: int, **kwargs: Any) -> Dict:
        """
        This function retrieves information about a specific PvP season from the API.

        Requested API:
            /data/wow/pvp-season/{pvp_season_id}

        Args:
            pvp_season_id: The ID of the PvP season.

        Returns:
            A dictionary of the PvP season.

        Raises:
            ValueError: If pvp_season_id is not provided.
        """

        if pvp_season_id is None:
            raise ValueError('pvp_season_id is required')

        api = f'/data/wow/pvp-season/{pvp_season_id}'

        query_params = {
            'namespace': 'dynamic',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_pvp_leaderboards_index(self, pvp_season_id: int, **kwargs: Any) -> Dict:
        """
        This function will return the index of PvP leaderboards from the API.

        Requested API:
            /data/wow/pvp-season/{pvp_season_id}/pvp-leaderboard/index

        Args:
            pvp_season_id: The ID of the PvP season.

        Returns:
            A dictionary of the PvP leaderboards index.
        """

        api = f'/data/wow/pvp-season/{pvp_season_id}/pvp-leaderboard/index'

        query_params = {
            'namespace': 'dynamic',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_pvp_leaderboard(self, pvp_season_id: int, pvp_bracket: str, **kwargs: Any) -> Dict:
        """
        This function retrieves information about a specific PvP leaderboard from the API.

        Requested API:
            /data/wow/pvp-season/{pvp_season_id}/pvp-leaderboard/{pvp_bracket}

        Args:
            pvp_season_id: The ID of the PvP season.
            pvp_bracket: The bracket of the PvP leaderboard.

        Returns:
            A dictionary of the PvP leaderboard.

        Raises:
            ValueError: If pvp_season_id or pvp_bracket is not provided.
        """

        if pvp_season_id is None:
            raise ValueError('pvp_season_id is required')

        if pvp_bracket is None:
            raise ValueError('pvp_bracket is required')

        api = f'/data/wow/pvp-season/{pvp_season_id}/pvp-leaderboard/{pvp_bracket}'

        query_params = {
            'namespace': 'dynamic',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_pvp_rewards_index(self, pvp_season_id: int, **kwargs: Any) -> Dict:
        """
        This function will return the index of PvP rewards from the API.

        Requested API:
            /data/wow/pvp-season/{pvp_season_id}/pvp-reward/index

        Args:
            pvp_season_id: The ID of the PvP season.

        Returns:
            A dictionary of the PvP rewards index.
        """

        api = f'/data/wow/pvp-season/{pvp_season_id}/pvp-reward/index'

        query_params = {
            'namespace': 'dynamic',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)