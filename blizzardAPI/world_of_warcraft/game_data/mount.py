from typing import Dict, Optional
from ...api import API

class Mount(API):
    
    def __init__(self, client_id, client_secret):
        super().__init__(client_id, client_secret)

    def get_mounts_index(self, region: Optional[str], locale: Optional[str]) -> Dict:
        """
        This function will return the index of mounts from the API.

        Requested API:
            /data/wow/mount/index

        Args:
            region: The region of the API you want to access.
            locale: The locale of the API you want to access.

        Returns:
            A dictionary of the mounts index.
        """

        api = '/data/wow/mount/index'

        query_params = {
            'namespace': 'static',
            'locale': locale,
        }

        return super().get_api(region, api, query_params)

    def get_mount(self, region: Optional[str], locale: Optional[str], mount_id: int) -> Dict:
        """
        This function will return the details of a specific mount from the API.

        Requested API:
            /data/wow/mount/{mountId}

        Args:
            region: The region of the API you want to access.
            mount_id: The ID of the mount you want to retrieve.
            locale: The locale of the API you want to access.

        Returns:
            A dictionary of the mount details.
        """

        api = f'/data/wow/mount/{mount_id}'

        query_params = {
            'namespace': 'static',
            'locale': locale,
        }

        return super().get_api(region, api, query_params)

    def search_mounts(self, region: Optional[str], locale: Optional[str], name_en: Optional[str], order_by: Optional[str], page: Optional[int]) -> Dict:
        """
        This function will search for mounts that match the given search query.

        Requested API:
            /data/wow/search/mount

        Args:
            region: The region of the API you want to access.
            name: The search query to use.
            locale: The locale of the API you want to access.
            orderby: The field to order the results by.
            _page: The page number of the results to return.
            **kwargs: Additional query parameters to include in the request.

        Returns:
            A dictionary of the search results.
        """

        api = '/data/wow/search/mount'

        query_params = {
            'namespace': 'static',
            'locale': locale,
        }

        if name_en is not None:
            query_params['name.en_US'] = name_en

        if order_by is not None:
            query_params['orderby'] = order_by

        if page is not None:
            query_params['_page'] = page

        return super().get_api(region, api, query_params)