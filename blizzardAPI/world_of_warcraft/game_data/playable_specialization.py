from typing import Dict, Optional
from ...api import API

class PlayableSpecialization(API):

    def __init__(self, client_id, client_secret):
        super().__init__(client_id, client_secret)

    def get_playable_specializations_index(self, region: Optional[str], locale: Optional[str]) -> Dict:
        """
        This function will return the index of playable specializations from the API.

        Requested API:
            /data/wow/playable-specialization/index

        Args:
            region: The region of the API you want to access.
            locale: The locale of the API you want to access.

        Returns:
            A dictionary of the playable specializations index.
        """

        api = '/data/wow/playable-specialization/index'

        query_params = {
            'namespace': 'static',
            'locale': locale,
        }

        return super().get_api(region, api, query_params)

    def get_playable_specialization(self, region: Optional[str], locale: Optional[str], spec_id: int) -> Dict:
        """
        This function will return the details of a specific playable specialization from the API.

        Requested API:
            /data/wow/playable-specialization/{specId}

        Args:
            region: The region of the API you want to access.
            spec_id: The ID of the playable specialization you want to retrieve.
            locale: The locale of the API you want to access.

        Returns:
            A dictionary of the playable specialization details.
        """

        api = f'/data/wow/playable-specialization/{spec_id}'

        query_params = {
            'namespace': 'static',
            'locale': locale,
        }

        return super().get_api(region, api, query_params)

    def get_playable_specialization_media(self, region: Optional[str], locale: Optional[str], spec_id: int) -> Dict:
        """
        This function will return the media of a specific playable specialization from the API.

        Requested API:
            /data/wow/media/playable-specialization/{specId}

        Args:
            region: The region of the API you want to access.
            spec_id: The ID of the playable specialization you want to retrieve.
            locale: The locale of the API you want to access.

        Returns:
            A dictionary of the playable specialization media.
        """

        api = f'/data/wow/media/playable-specialization/{spec_id}'

        query_params = {
            'namespace': 'static',
            'locale': locale,
        }

        return super().get_api(region, api, query_params)