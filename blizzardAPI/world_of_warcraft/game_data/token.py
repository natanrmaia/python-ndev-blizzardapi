from typing import Optional, Dict, Any
from ...api import API

class Token(API):

    def __init__(self, client_id, client_secret):
        super().__init__(client_id, client_secret)

    def get_token_index(self, region: str, **kwargs: Any) -> Dict:
        """
        This function will return the index of tokens from the API.

        Requested API:
            /data/wow/token/index

        Args:
            region: The region of the API you want to access.
            **kwargs: Any additional query parameters to be passed to the API.

        Returns:
            A dict of WOW tokens prices.
        """

        api = '/data/wow/token/index'

        if region is None:
            raise ValueError('region is required')

        query_params = {
            'namespace': 'dynamic',
        }

        query_params.update(kwargs)

        return super().get_api(region=region, api=api, query_params=query_params, **kwargs)