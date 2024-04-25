from typing import Optional, Dict, Any
from ...api import API


class Realm(API):

    def __init__(self, client_id, client_secret):
        super().__init__(client_id, client_secret)

    def get_realms_index(self, **kwargs: Any) -> Dict:
        """
        This function will return the index of realms from the API.

        Requested API:
            /data/wow/realm/index

        Returns:
            A dictionary of the realms index.
        """

        api = '/data/wow/realm/index'

        query_params = {
            'namespace': 'dynamic',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_realm(self, realm_slug: str, **kwargs: Any) -> Dict:
        """
        This function retrieves information about a specific realm from the API.

        Requested API:
            /data/wow/realm/{realmSlug}

        Args:
            realm_slug: The slug of the realm.

        Returns:
            A dictionary of the realm.

        Raises:
            ValueError: If realm_slug is not provided.
        """

        if realm_slug is None:
            raise ValueError('realm_slug is required')

        api = f'/data/wow/realm/{realm_slug}'

        query_params = {
            'namespace': 'dynamic',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_realm_search(self, search: str, **kwargs: Any) -> Dict:
        """
        This function retrieves information about a specific realm from the API.

        Requested API:
            /data/wow/search/realm

        Args:
            search: The search query.

        Returns:
            A dictionary of the realm search results.

        Raises:
            ValueError: If search is not provided.
        """

        if search is None:
            raise ValueError('search is required')

        api = '/data/wow/search/realm'

        query_params = {
            'namespace': 'dynamic',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)