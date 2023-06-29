from typing import Dict, Any
from ...api import API

class Mount(API):

    def __init__(self, client_id, client_secret):
        super().__init__(client_id, client_secret)

    def get_mounts_index(self, **kwargs: Any) -> Dict:
        """
        This function will return the index of mounts from the API.

        Requested API:
            /data/wow/mount/index

        Returns:
            A dictionary of the mounts index.
        """

        api = '/data/wow/mount/index'

        query_params = {
            'namespace': 'static',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, kwargs=kwargs)

    def get_mount(self, mount_id: int, **kwargs: Any) -> Dict:
        """
        This function will return the details of a specific mount from the API.

        Requested API:
            /data/wow/mount/{mountId}

        Args:
            locale: The locale of the API you want to access.

        Returns:
            A dictionary of the mount details.
        """

        api = f'/data/wow/mount/{mount_id}'

        query_params = {
            'namespace': 'static',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, kwargs=kwargs)

    def get_mount_search(self, **kwargs: Any) -> Dict:
        """
        This function will search for mounts that match the given search query.

        Requested API:
            /data/wow/search/mount

        Returns:
            A dictionary of the search results.
        """

        api = '/data/wow/search/mount'

        query_params = {
            'namespace': 'static',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, kwargs=kwargs)