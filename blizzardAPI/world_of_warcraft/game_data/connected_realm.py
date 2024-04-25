from typing import Optional, Dict, Any
from ...api import API

class ConnectedRealm(API):

    def __init__(self, client_id, client_secret):
        super().__init__(client_id, client_secret)

    def get_connected_realms_index(self, **kwargs: Any) -> Dict:
        """
        This function will return the index of connected realms from the API.

        Requested API:
            /data/wow/connected-realm/index


        Returns:
            A dictionary of the connected realm index.
        """

        api = '/data/wow/connected-realm/index'

        query_params = {
            'namespace': 'dynamic',
        }

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_connected_realm(self, connected_realm_id: int, **kwargs: Any) -> Dict:
        """
        This function will return the connected realm from the API.

        Requested API:
            /data/wow/connected-realm/{connected_realm_id}

        Args:
            connected_realm_id: The ID of the connected realm.

        Returns:
            A dictionary of the connected realm.

        Raises:
            ValueError: If connected_realm_id is not provided.
        """

        if connected_realm_id is None:
            raise ValueError('connected_realm_id is required')

        api = f'/data/wow/connected-realm/{connected_realm_id}'

        query_params = {
            'namespace': 'dynamic',
        }

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_connected_realm_search(self, **kwargs: Any) -> Dict:
        """
        This function will return the connected realm search from the API.

        Requested API:
            /data/wow/search/connected-realm

        Returns:
            A dictionary of the connected realm search.

        Raises:
            ValueError: If connected_realm_id is not provided.
        """

        api = '/data/wow/search/connected-realm'

        query_params = {
            'namespace': 'dynamic',
        }

        return super().get_api(api=api, query_params=query_params, **kwargs)