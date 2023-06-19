from typing import Optional, Dict
from ...api import API

class PowerType(API):

    def __init__(self, client_id, client_secret):
        super().__init__(client_id, client_secret)

    def get_power_type_index(self, region: Optional[str], locale: Optional[str]) -> Dict:
        """
        This function will return the index of power types from the API.

        Requested API:
            /data/wow/power-type/index

        Args:
            region: The region of the API you want to access.
            locale: The locale of the API you want to access.

        Returns:
            A dict of power types.
        """

        api = '/data/wow/power-type/index'

        query_params = {
            'namespace': 'static',
            'locale': locale,
        }

        return super().get_api(region, api, query_params)

    def get_power_type(self, region: Optional[str], locale: Optional[str], power_type_id: int) -> Dict:
        """
        This function will return the power type from the API.

        Requested API:
            /data/wow/power-type/{power_type_id}

        Args:
            region: The region of the API you want to access.
            locale: The locale of the API you want to access.
            power_type_id: The ID of the power type.
        
        Returns:
            A dict of the requested power type.

        Raises:
            ValueError: If power_type_id is not provided.
        """

        if power_type_id is None:
            raise ValueError('power_type_id is required')

        api = '/data/wow/power-type/{}'

        query_params = {
            'namespace': 'static',
            'locale': locale,
        }

        return super().get_api(region, api.format(power_type_id), query_params)