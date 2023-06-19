from typing import Optional, Dict
from ...api import API


class Covenant(API):

    def __init__(self, client_id, client_secret):
        super().__init__(client_id, client_secret)

    def get_covenant_index(self, region: Optional[str], locale: Optional[str]) -> Dict:
        """
        This function will return the index of covenants from the API.

        Requested API:
            /data/wow/covenant/index

        Args:
            region: The region of the API you want to access.
            locale: The locale of the API you want to access.

        Returns:
            A dictionary of the covenant index.
        """

        api = '/data/wow/covenant/index'

        query_params = {
            'namespace': 'static',
            'locale': locale,
        }

        return super().get_api(region, api, query_params)

    def get_covenant(self, region: Optional[str], locale: Optional[str], covenant_id: int) -> Dict:
        """
        tThis function retrieves information about a specific covenant in the World of Warcraft from the API.

        Requested API:
            /data/wow/covenant/{covenant_id}

        Args:
            region: The region of the API you want to access.
            locale: The locale of the API you want to access.
            covenant_id: The ID of the covenant.

        Returns:
            A dictionary of the covenant.

        Raises:
            ValueError: If covenant_id is not provided.
        """

        if covenant_id is None:
            raise ValueError('covenant_id is required')

        api = '/data/wow/covenant/{}'

        query_params = {
            'namespace': 'static',
            'locale': locale,
        }

        return super().get_api(region, api, query_params)

    def get_covenant_media(self, region: Optional[str], locale: Optional[str], covenant_id: int) -> Dict:
        """
        This function retrieves media for a specific covenant in the World of Warcraft from the API.

        Requested API:
            /data/wow/media/covenant/{covenant_id}

        Args:
            region: The region of the API you want to access.
            locale: The locale of the API you want to access.
            covenant_id: The ID of the covenant.

        Returns:
            A dictionary of the covenant media.

        Raises:
            ValueError: If covenant_id is not provided.
        """

        if covenant_id is None:
            raise ValueError('covenant_id is required')

        api = '/data/wow/media/covenant/{}'

        query_params = {
            'namespace': 'static',
            'locale': locale,
        }

        return super().get_api(region, api, query_params)

    def get_soulbind_index(self, region: Optional[str], locale: Optional[str]) -> Dict:
        """
        This function will return the index of soulbinds from the API.

        Requested API:
            /data/wow/covenant/soulbind/index

        Args:
            region: The region of the API you want to access.
            locale: The locale of the API you want to access.

        Returns:
            A dictionary of the soulbind index.
        """

        api = '/data/wow/covenant/soulbind/index'

        query_params = {
            'namespace': 'static',
            'locale': locale,
        }

        return super().get_api(region, api, query_params)

    def get_soulbind(self, region: Optional[str], locale: Optional[str], soulbind_id: int) -> Dict:
        """
        This function retrieves information about a specific soulbind in the World of Warcraft from the API.

        Requested API:
            /data/wow/covenant/soulbind/{soulbind_id}

        Args:
            region: The region of the API you want to access.
            locale: The locale of the API you want to access.
            soulbind_id: The ID of the soulbind.

        Returns:
            A dictionary of the soulbind.

        Raises:
            ValueError: If soulbind_id is not provided.
        """


        if soulbind_id is None:
            raise ValueError('soulbind_id is required')

        api = '/data/wow/covenant/soulbind/{}'

        query_params = {
            'namespace': 'static',
            'locale': locale,
        }

        return super().get_api(region, api, query_params)

    def get_conduit_index(self, region: Optional[str], locale: Optional[str]) -> Dict:
        """
        This function will return the index of conduits from the API.

        Requested API:
            /data/wow/covenant/conduit/index

        Args:
            region: The region of the API you want to access.
            locale: The locale of the API you want to access.

        Returns:
            A dictionary of the conduit index.
        """

        api = '/data/wow/covenant/conduit/index'

        query_params = {
            'namespace': 'static',
            'locale': locale,
        }

        return super().get_api(region, api, query_params)

    def get_conduit(self, region: Optional[str], locale: Optional[str], conduit_id: int) -> Dict:
        """
        This function retrieves information about a specific conduit in the World of Warcraft from the API.

        Requested API:
            /data/wow/covenant/conduit/{conduit_id}

        Args:
            region: The region of the API you want to access.
            locale: The locale of the API you want to access.
            conduit_id: The ID of the conduit.

        Returns:
            A dictionary of the conduit.

        Raises:
            ValueError: If conduit_id is not provided.
        """

        if conduit_id is None:
            raise ValueError('conduit_id is required')

        api = '/data/wow/covenant/conduit/{}'

        query_params = {
            'namespace': 'static',
            'locale': locale,
        }

        return super().get_api(region, api, query_params)