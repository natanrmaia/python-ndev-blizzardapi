from typing import Optional, Dict, Any
from ...api import API

class Reputation(API):

    def __init__(self, client_id, client_secret):
        super().__init__(client_id, client_secret)

    def get_reputation_factions_index(self, **kwargs: Any) -> Dict:
        """
        This function will return the index of reputation factions from the API.

        Requested API:
            /data/wow/reputation-faction/index

        Returns:
            A dictionary of the reputation factions index.
        """

        api = '/data/wow/reputation-faction/index'

        query_params = {
            'namespace': 'static',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_reputation_faction(self, reputation_faction_id: int, **kwargs: Any) -> Dict:
        """
        This function retrieves information about a specific reputation faction from the API.

        Requested API:
            /data/wow/reputation-faction/{reputation_faction_id}

        Args:
            reputation_faction_id: The ID of the reputation faction.

        Returns:
            A dictionary of the reputation faction.

        Raises:
            ValueError: If reputation_faction_id is not provided.
        """

        if reputation_faction_id is None:
            raise ValueError('reputation_faction_id is required')

        api = f'/data/wow/reputation-faction/{reputation_faction_id}'

        query_params = {
            'namespace': 'static',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_reputation_tiers_index(self, **kwargs: Any) -> Dict:
        """
        This function will return the index of reputation tiers from the API.

        Requested API:
            /data/wow/reputation-tiers/index

        Returns:
            A dictionary of the reputation tiers index.
        """

        api = '/data/wow/reputation-tiers/index'

        query_params = {
            'namespace': 'static',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_reputation_tiers(self, reputation_tiers_id: int, **kwargs: Any) -> Dict:
        """
        This function retrieves information about a specific reputation tier from the API.

        Requested API:
            /data/wow/reputation-tiers/{reputation_tiers_id}

        Args:
            reputation_tiers_id: The ID of the reputation tier.

        Returns:
            A dictionary of the reputation tier.

        Raises:
            ValueError: If reputation_tiers_id is not provided.
        """

        if reputation_tiers_id is None:
            raise ValueError('reputation_tiers_id is required')

        api = f'/data/wow/reputation-tiers/{reputation_tiers_id}'

        query_params = {
            'namespace': 'static',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)