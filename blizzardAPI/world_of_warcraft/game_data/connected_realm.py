from typing import Optional, Dict
from ...api import API

class ConnectedRealm(API):

    def __init__(self, client_id, client_secret):
        super().__init__(client_id, client_secret)

    def get_connected_realms_index(self, region: Optional[str], locale: Optional[str]) -> Dict:
        """
        This function will return the index of connected realms from the API.

        Requested API:
            /data/wow/connected-realm/index

        Args:
            region: The region of the API you want to access.
            locale: The locale of the API you want to access.

        Returns:
            A dictionary of the connected realm index.
        """

        api = '/data/wow/connected-realm/index'

        query_params = {
            'namespace': 'dynamic',
            'locale': locale,
        }

        return super().get_api(region, api, query_params)
    
    def get_connected_realm(self, region: Optional[str], locale: Optional[str], connected_realm_id: int) -> Dict:
        """
        This function will return the connected realm from the API.

        Requested API:
            /data/wow/connected-realm/{connected_realm_id}

        Args:
            region: The region of the API you want to access.
            locale: The locale of the API you want to access.
            connected_realm_id: The ID of the connected realm.

        Returns:
            A dictionary of the connected realm.

        Raises:
            ValueError: If connected_realm_id is not provided.
        """

        if connected_realm_id is None:
            raise ValueError('connected_realm_id is required')

        api = '/data/wow/connected-realm/{}'

        query_params = {
            'namespace': 'dynamic',
            'locale': locale,
        }

        return super().get_api(region, api.format(connected_realm_id), query_params)