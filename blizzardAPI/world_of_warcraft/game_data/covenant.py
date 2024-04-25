from typing import Optional, Dict, Any
from ...api import API

class Covenant(API):

    def __init__(self, client_id, client_secret):
        super().__init__(client_id, client_secret)

    def get_covenant_index(self, **kwargs: Any) -> Dict:
        """
        This function will return the index of covenants from the API.

        Requested API:
            /data/wow/covenant/index

        Returns:
            A dictionary of the covenant index.
        """

        api = '/data/wow/covenant/index'

        query_params = {
            'namespace': 'static',
        }

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_covenant(self, covenant_id: int, **kwargs: Any) -> Dict:
        """
        tThis function retrieves information about a specific covenant in the World of Warcraft from the API.

        Requested API:
            /data/wow/covenant/{covenant_id}

        Args:
            covenant_id: The ID of the covenant.

        Returns:
            A dictionary of the covenant.

        Raises:
            ValueError: If covenant_id is not provided.
        """

        if covenant_id is None:
            raise ValueError('covenant_id is required')

        api = f'/data/wow/covenant/{covenant_id}'

        query_params = {
            'namespace': 'static',
        }

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_covenant_media(self, covenant_id: int, **kwargs: Any) -> Dict:
        """
        This function retrieves media for a specific covenant in the World of Warcraft from the API.

        Requested API:
            /data/wow/media/covenant/{covenant_id}

        Args:
            covenant_id: The ID of the covenant.

        Returns:
            A dictionary of the covenant media.

        Raises:
            ValueError: If covenant_id is not provided.
        """

        if covenant_id is None:
            raise ValueError('covenant_id is required')

        api = f'/data/wow/media/covenant/{covenant_id}'

        query_params = {
            'namespace': 'static',
        }

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_soulbind_index(self, **kwargs: Any) -> Dict:
        """
        This function will return the index of soulbinds from the API.

        Requested API:
            /data/wow/covenant/soulbind/index

        Returns:
            A dictionary of the soulbind index.
        """

        api = '/data/wow/covenant/soulbind/index'

        query_params = {
            'namespace': 'static',
        }

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_soulbind(self, soulbind_id: int, **kwargs: Any) -> Dict:
        """
        This function retrieves information about a specific soulbind in the World of Warcraft from the API.

        Requested API:
            /data/wow/covenant/soulbind/{soulbind_id}

        Args:
            soulbind_id: The ID of the soulbind.

        Returns:
            A dictionary of the soulbind.

        Raises:
            ValueError: If soulbind_id is not provided.
        """

        if soulbind_id is None:
            raise ValueError('soulbind_id is required')

        api = f'/data/wow/covenant/soulbind/{soulbind_id}'

        query_params = {
            'namespace': 'static',
        }

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_conduit_index(self, **kwargs: Any) -> Dict:
        """
        This function will return the index of conduits from the API.

        Requested API:
            /data/wow/covenant/conduit/index

        Returns:
            A dictionary of the conduit index.
        """

        api = '/data/wow/covenant/conduit/index'

        query_params = {
            'namespace': 'static',
        }

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_conduit(self, conduit_id: int, **kwargs: Any) -> Dict:
        """
        This function retrieves information about a specific conduit in the World of Warcraft from the API.

        Requested API:
            /data/wow/covenant/conduit/{conduit_id}

        Args:
            conduit_id: The ID of the conduit.

        Returns:
            A dictionary of the conduit.

        Raises:
            ValueError: If conduit_id is not provided.
        """

        if conduit_id is None:
            raise ValueError('conduit_id is required')

        api = f'/data/wow/covenant/conduit/{conduit_id}'

        query_params = {
            'namespace': 'static',
        }

        return super().get_api(api=api, query_params=query_params, **kwargs)