from typing import Optional, Dict
from ...api import API

class Token(API):

    def __init__(self, client_id, client_secret):
        super().__init__(client_id, client_secret)

    def get_token_index(self, region: Optional[str], locale: Optional[str]) -> Dict:
        """
        This function will return the index of tokens from the API.

        Requested API:
            /data/wow/token/index

        Args:
            region: The region of the API you want to access.
            locale: The locale of the API you want to access.

        Returns:
            A dict of WOW tokens prices.
        """

        api = '/data/wow/token/index'

        query_params = {
            'namespace': 'dynamic',
            'locale': locale,
        }

        return super().get_api(region, api, query_params)