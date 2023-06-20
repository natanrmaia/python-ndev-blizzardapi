from typing import Optional, Dict
from ...api import API

class Media(API):

    def __init__(self, client_id, client_secret):
        super().__init__(client_id, client_secret)

    def get_media_search(self, region: Optional[str], locale: Optional[str], tag:  Optional[str], order_by: Optional[str], page: Optional[str]) -> Dict:
        """
        This function will return medias from the API.

        Requested API:
            /data/wow/media/search

        Args:
            region: The region of the API you want to access.
            locale: The locale of the API you want to access.
            tag: The tag of the media to search for.
            order_by: The field to order the media by.
            page: The page of the media to return.

        Returns:
            A dictionary of the media search.
        """

        api = '/data/wow/media/search'

        query_params = {
            'namespace': 'static',
            'locale': locale,
        }

        if tag is not None:
            query_params['tag'] = tag

        if order_by is not None:
            query_params['orderby'] = order_by

        if page is not None:
            query_params['page'] = page

        return super().get_api(region, api, query_params)
