from typing import Optional, Dict, Any
from ...api import API

class Media(API):

    def __init__(self, client_id, client_secret):
        super().__init__(client_id, client_secret)

    def get_media_search(self, **kwargs: Any) -> Dict:
        """
        This function will return medias from the API.

        Requested API:
            /data/wow/search/media

        Returns:
            A dictionary of the media search.
        """

        api = '/data/wow/search/media'

        query_params = {
            'namespace': 'static',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)