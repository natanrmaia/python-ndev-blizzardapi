from typing import Optional, Dict, Any
from ...api import API


class PvPTier(API):

    def __init__(self, client_id, client_secret):
        super().__init__(client_id, client_secret)

    def get_pvp_tiers_index(self, **kwargs: Any) -> Dict:
        """
        This function will return the index of PvP tiers from the API.

        Requested API:
            /data/wow/pvp-tier/index

        Returns:
            A dictionary of the PvP tiers index.
        """

        api = '/data/wow/pvp-tier/index'

        query_params = {
            'namespace': 'static',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_pvp_tier(self, pvp_tier_id: int, **kwargs: Any) -> Dict:
        """
        This function retrieves information about a specific PvP tier from the API.

        Requested API:
            /data/wow/pvp-tier/{pvp_tier_id}

        Args:
            pvp_tier_id: The ID of the PvP tier.

        Returns:
            A dictionary of the PvP tier.

        Raises:
            ValueError: If pvp_tier_id is not provided.
        """

        if pvp_tier_id is None:
            raise ValueError('pvp_tier_id is required')

        api = f'/data/wow/pvp-tier/{pvp_tier_id}'

        query_params = {
            'namespace': 'static',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_pvp_tier_media(self, pvp_tier_id: int, **kwargs: Any) -> Dict:
        """
        This function retrieves media information about a specific PvP tier from the API.

        Requested API:
            /data/wow/media/pvp-tier/{pvp_tier_id}

        Args:
            pvp_tier_id: The ID of the PvP tier.

        Returns:
            A dictionary of the PvP tier media.

        Raises:
            ValueError: If pvp_tier_id is not provided.
        """

        if pvp_tier_id is None:
            raise ValueError('pvp_tier_id is required')

        api = f'/data/wow/media/pvp-tier/{pvp_tier_id}'

        query_params = {
            'namespace': 'static',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)