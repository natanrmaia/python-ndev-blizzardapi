from typing import Optional, Dict, Any
from ...api import API


class Region(API):

    def __init__(self, client_id, client_secret):
        super().__init__(client_id, client_secret)

    def get_regions_index(self, **kwargs: Any) -> Dict:
        """
        This function will return the index of regions from the API.

        Requested API:
            /data/wow/region/index

        Args:
            locale: The locale of the API you want to access.

        Returns:
            A dictionary of the regions index.
        """

        api = '/data/wow/region/index'

        query_params = {
            'namespace': 'dynamic',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_region(self, region_id: int, **kwargs: Any) -> Dict:
        """
        This function retrieves information about a specific region from the API.

        Requested API:
            /data/wow/region/{region_id}

        Args:
            region_id: The ID of the region.
            locale: The locale of the API you want to access.

        Returns:
            A dictionary of the region.

        Raises:
            ValueError: If region_id is not provided.
        """

        if region_id is None:
            raise ValueError('region_id is required')

        api = f'/data/wow/region/{region_id}'

        query_params = {
            'namespace': 'dynamic',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)