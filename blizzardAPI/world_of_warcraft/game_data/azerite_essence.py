from typing import Optional, Dict
from ...api import API

class AzeriteEssence(API):

    def __init__(self, client_id, client_secret):
        super().__init__(client_id, client_secret)

    def get_azerite_essences_index(self, region: Optional[str], locale: Optional[str]) -> Dict:
        """
        This function will return the index of azerite essences from the API.

        Requested API:
            /data/wow/azerite-essence/index

        Args:
            region: The region of the API you want to access.
            locale: The locale of the API you want to access.

        Returns:
            A dictionary of the azerite essences index.
        """

        api = '/data/wow/azerite-essence/index'

        query_params = {
            'namespace': 'static',
            'locale': locale,
        }

        return super().get_api(region, api, query_params)
    
    def get_azerite_essence(self, region: Optional[str], locale: Optional[str], azerite_essence_id: int) -> Dict:

        """
        This function will return the azerite essence from the API.

        Requested API:
            /data/wow/azerite-essence/{azerite_essence_id}

        Args:
            region: The region of the API you want to access.
            locale: The locale of the API you want to access.
            azerite_essence_id: The ID of the azerite essence.

        Returns:
            A dictionary of the azerite essence.

        Raises:
            ValueError: If azerite_essence_id is not provided.
        """

        if azerite_essence_id is None:
            raise ValueError('azerite_essence_id is required')

        api = '/data/wow/azerite-essence/{}'

        query_params = {
            'namespace': 'static',
            'locale': locale,
        }

        return super().get_api(region, api, query_params)
    
    def get_azerite_essence_search(self, region: Optional[str], locale: Optional[str], allowed_specializations_id: Optional[int], order_by: Optional[str], page: Optional[int]) -> Dict:
            
            """
            This function will return the azerite essence search from the API.
    
            Requested API:
                /data/wow/search/azerite-essence

            Args:
                region: The region of the API you want to access.
                locale: The locale of the API you want to access.
                allowed_specializations_id: The ID of the allowed specializations.
                order_by: The order of the API you want to access.
                page: The page of the API you want to access.

            Returns:
                A dictionary of the azerite essence search.
            """

            api = '/data/wow/search/azerite-essence'

            query_params = {
                'namespace': 'static',
                'locale': locale,
            }

            if allowed_specializations_id is not None:
                query_params['allowed_specializations.id'] = allowed_specializations_id

            if order_by is not None:
                query_params['orderby'] = order_by

            if page is not None:
                query_params['page'] = page

            return super().get_api(region, api, query_params)
    
    def get_azerite_essence_media(self, region: Optional[str], locale: Optional[str], azerite_essence_id: int) -> Dict:
            
            """
            This function will return the azerite essence media from the API.
    
            Requested API:
                /data/wow/media/azerite-essence/{azerite_essence_id}

            Args:
                region: The region of the API you want to access.
                locale: The locale of the API you want to access.
                azerite_essence_id: The ID of the azerite essence.

            Returns:
                A dictionary of the azerite essence media.

            Raises:
                ValueError: If azerite_essence_id is not provided.

            """

            if azerite_essence_id is None:
                raise ValueError('azerite_essence_id is required')

            api = '/data/wow/media/azerite-essence/{}'

            query_params = {
                'namespace': 'static',
                'locale': locale,
            }

            return super().get_api(region, api, query_params)