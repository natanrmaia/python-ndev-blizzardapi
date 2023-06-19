from typing import Optional, Dict
from ...api import API

class AuctionHouse(API):

    def __init__(self, client_id, client_secret):
        super().__init__(client_id, client_secret)

    def get_auctions(self, region: Optional[str], locale: Optional[str], connected_realm_id: int) -> Dict:
        """
        This function will return the auctions from the API.

        Requested API:
            /data/wow/connected-realm/{connected_realm_id}/auctions

        Args:
            region: The region of the API you want to access.
            locale: The locale of the API you want to access.
            connected_realm_id: The ID of the connected realm.

        Returns:
            A dict of the auctions.

        Raises:
            ValueError: If connected_realm_id is not provided.
        """

        if connected_realm_id is None:
            raise ValueError('connected_realm_id is required')

        api = '/data/wow/connected-realm/{}/auctions'

        query_params = {
            'namespace': 'dynamic',
            'locale': locale,
        }

        return super().get_api(region, api.format(connected_realm_id), query_params)

    def get_commodities(self, region: Optional[str], locale: Optional[str]) -> Dict:
        """
        This function will return the commodities from the API.

        Requested API:
            /data/wow/commodity/index

        Args:
            region: The region of the API you want to access.
            locale: The locale of the API you want to access.

        Returns:
            A dict of the commodities.
        """

        api = '/data/wow/commodity/index'

        query_params = {
            'namespace': 'dynamic',
            'locale': locale,
        }

        return super().get_api(region, api, query_params)
