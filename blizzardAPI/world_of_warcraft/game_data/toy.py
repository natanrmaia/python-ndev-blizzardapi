# BEGIN: 8d4f5g6h7j8k
from typing import Optional, Dict, Any
from ...api import API

class Toy(API):

    def __init__(self, client_id, client_secret):
        super().__init__(client_id, client_secret)

    def get_toy_index(self, **kwargs: Any) -> Dict:
        """
        This function retrieves the index of all Toys from the API.

        Requested API:
            /data/wow/toy/index

        Args:
            **kwargs: Any additional query parameters to be passed to the API.

        Returns:
            A dictionary of the Toy index.
        """

        api = '/data/wow/toy/index'

        query_params = {
            'namespace': 'static',
        }
        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params)

    def get_toy(self, toy_id: int, **kwargs) -> Dict:
        """
        This function retrieves information about a specific Toy from the API.

        Requested API:
            /data/wow/toy/{toy_id}

        Args:
            toy_id: The ID of the Toy.
            **kwargs: Any additional query parameters to be passed to the API.

        Returns:
            A dictionary of the Toy.

        Raises:
            ValueError: If toy_id is not provided.
        """

        if toy_id is None:
            raise ValueError('toy_id is required')

        api = f'/data/wow/toy/{toy_id}'

        query_params = {
            'namespace': 'static',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params)
