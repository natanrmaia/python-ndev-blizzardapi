from typing import Optional, Dict
from ...api import API

class Heirloom(API):

    def __init__(self, client_id, client_secret):
        super().__init__(client_id, client_secret)

    def get_heirloom_index(self, region: Optional[str], locale: Optional[str]) -> Dict:
        """
        This function will return the index of heirlooms from the API.

        Requested API:
            /data/wow/item-class/index

        Args:
            region: The region of the API you want to access.
            locale: The locale of the API you want to access.

        Returns:
            A dictionary of the heirloom index.
        """

        api = '/data/wow/item-class/index'

        query_params = {
            'namespace': 'static',
            'locale': locale,
        }

        return super().get_api(region, api, query_params)
    
    def get_heirloom(self, region: Optional[str], locale: Optional[str], heirloom_id: int) -> Dict:
        """
        This function retrieves information about a specific heirloom in the World of Warcraft
        game.
        
        Requested API:
            /data/wow/item-class/{heirloom_id}

        Args:
            region: The region of the API you want to access.
            locale: The locale of the API you want to access.
            heirloom_id: The ID of the heirloom.
        
        Returns:
            A dictionary of the heirloom.

        Raises:
            ValueError: If heirloom_id is not provided.
        """

        if heirloom_id is None:
            raise ValueError('heirloom_id is required')

        api = '/data/wow/item-class/{}'

        query_params = {
            'namespace': 'static',
            'locale': locale,
        }

        return super().get_api(region, api.format(heirloom_id), query_params)