from typing import Optional, Dict, Any
from ...api import API

class AzeriteEssence(API):

    def __init__(self, client_id, client_secret):
        super().__init__(client_id, client_secret)

    def get_azerite_essences_index(self, **kwargs: Any) -> Dict:
        """
        This function will return the index of azerite essences from the API.

        Requested API:
            /data/wow/azerite-essence/index

        Returns:
            A dictionary of the azerite essences index.
        """

        api = '/data/wow/azerite-essence/index'

        query_params = {
            'namespace': 'static',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_azerite_essence(self, azerite_essence_id: int, **kwargs: Any) -> Dict:
        """
        This function will return the azerite essence from the API.

        Requested API:
            /data/wow/azerite-essence/{azerite_essence_id}

        Args:
            azerite_essence_id: The ID of the azerite essence.

        Returns:
            A dictionary of the azerite essence.

        Raises:
            ValueError: If azerite_essence_id is not provided.
        """

        if azerite_essence_id is None:
            raise ValueError('azerite_essence_id is required')

        api = f'/data/wow/azerite-essence/{azerite_essence_id}'

        query_params = {
            'namespace': 'static',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_azerite_essence_search(self, **kwargs: Any) -> Dict:
            """
            This function will return the azerite essence search from the API.

            Requested API:
                /data/wow/search/azerite-essence

            Returns:
                A dictionary of the azerite essence search.
            """

            api = '/data/wow/search/azerite-essence'

            query_params = {
                'namespace': 'static',
            }

            query_params.update(kwargs)

            return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_azerite_essence_media(self, azerite_essence_id: int, **kwargs: Any) -> Dict:
            """
            This function will return the azerite essence media from the API.

            Requested API:
                /data/wow/media/azerite-essence/{azerite_essence_id}

            Args:
                azerite_essence_id: The ID of the azerite essence.

            Returns:
                A dictionary of the azerite essence media.

            Raises:
                ValueError: If azerite_essence_id is not provided.

            """

            if azerite_essence_id is None:
                raise ValueError('azerite_essence_id is required')

            api = f'/data/wow/media/azerite-essence/{azerite_essence_id}'

            query_params = {
                'namespace': 'static',
            }

            query_params.update(kwargs)

            return super().get_api(api=api, query_params=query_params, **kwargs)