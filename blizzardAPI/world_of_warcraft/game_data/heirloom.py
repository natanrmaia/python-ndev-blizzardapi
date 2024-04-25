from typing import Optional, Dict, Any
from ...api import API

class Heirloom(API):

    def __init__(self, client_id, client_secret):
        super().__init__(client_id, client_secret)

    def get_heirloom_index(self, **kwargs: Any) -> Dict:
        """
        This function will return the index of heirlooms from the API.

        Requested API:
            /data/wow/heirloom/index

        Returns:
            A dictionary of the heirloom index.
        """

        api = '/data/wow/heirloom/index'

        query_params = {
            'namespace': 'static',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_heirloom(self, heirloom_id: int, **kwargs: Any) -> Dict:
        """
        This function retrieves information about a specific heirloom in the World of Warcraft
        game.

        Requested API:
            /data/wow/heirloom/{heirloom_id}

        Args:
            heirloom_id: The ID of the heirloom.

        Returns:
            A dictionary of the heirloom.

        Raises:
            ValueError: If heirloom_id is not provided.
        """

        if heirloom_id is None:
            raise ValueError('heirloom_id is required')

        api = f'/data/wow/heirloom/{heirloom_id}'

        query_params = {
            'namespace': 'static',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)