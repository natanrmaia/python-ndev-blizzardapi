from typing import Optional, Dict, Any
from ...api import API

class PowerType(API):

    def __init__(self, client_id, client_secret):
        super().__init__(client_id, client_secret)

    def get_power_type_index(self, **kwargs: Any) -> Dict:
        """
        This function will return the index of power types from the API.

        Requested API:
            /data/wow/power-type/index

        Returns:
            A dict of power types.
        """

        api = '/data/wow/power-type/index'

        query_params = {
            'namespace': 'static',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_power_type(self, power_type_id: int, **kwargs: Any) -> Dict:
        """
        This function will return the power type from the API.

        Requested API:
            /data/wow/power-type/{power_type_id}

        Args:
            power_type_id: The ID of the power type.

        Returns:
            A dict of the requested power type.

        Raises:
            ValueError: If power_type_id is not provided.
        """

        if power_type_id is None:
            raise ValueError('power_type_id is required')

        api = f'/data/wow/power-type/{power_type_id}'

        query_params = {
            'namespace': 'static',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)