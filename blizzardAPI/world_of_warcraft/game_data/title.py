from typing import Optional, Dict, Any
from ...api import API


class Title(API):

    def __init__(self, client_id, client_secret):
        super().__init__(client_id, client_secret)

    def get_titles_index(self, **kwargs: Any) -> Dict:
        """
        This function will return the index of titles from the API.

        Requested API:
            /data/wow/title/index

        Returns:
            A dictionary of the titles index.
        """

        api = '/data/wow/title/index'

        query_params = {
            'namespace': 'static',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_title(self, title_id: int, **kwargs: Any) -> Dict:
        """
        This function retrieves information about a specific title from the API.

        Requested API:
            /data/wow/title/{title_id}

        Args:
            title_id: The ID of the title.

        Returns:
            A dictionary of the title.

        Raises:
            ValueError: If title_id is not provided.
        """

        if title_id is None:
            raise ValueError('title_id is required')

        api = f'/data/wow/title/{title_id}'

        query_params = {
            'namespace': 'static',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)