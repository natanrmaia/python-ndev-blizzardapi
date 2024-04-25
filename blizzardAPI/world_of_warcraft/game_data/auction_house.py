from typing import Optional, Dict, Any
from ...api import API

class AuctionHouse(API):

    def __init__(self, client_id, client_secret):
        super().__init__(client_id, client_secret)

    def get_auctions(self, connected_realm_id: int, **kwargs: Any) -> Dict:
        """
        This function will return the auctions from the API.

        Requested API:
            /data/wow/connected-realm/{connected_realm_id}/auctions

        Args:
            connected_realm_id: The ID of the connected realm.

        Returns:
            A dict of the auctions.

        Raises:
            ValueError: If connected_realm_id is not provided.
        """

        if connected_realm_id is None:
            raise ValueError('connected_realm_id is required')

        api = f'/data/wow/connected-realm/{connected_realm_id}/auctions'

        query_params = {
            'namespace': 'dynamic',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_commodities(self, **kwargs: Any) -> Dict:
        """
        This function will return the commodities from the API.

        Requested API:
            /data/wow/auctions/commodities

        Returns:
            A dict of the commodities.
        """

        api = '/data/wow/auctions/commodities'

        query_params = {
            'namespace': 'dynamic',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)
