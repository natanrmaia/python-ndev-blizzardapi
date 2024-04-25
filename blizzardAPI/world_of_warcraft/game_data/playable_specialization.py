from typing import Dict, Optional, Any
from ...api import API

class PlayableSpecialization(API):

    def __init__(self, client_id, client_secret):
        super().__init__(client_id, client_secret)

    def get_playable_specializations_index(self, **kwargs: Any) -> Dict:
        """
        This function will return the index of playable specializations from the API.

        Requested API:
            /data/wow/playable-specialization/index

        Returns:
            A dictionary of the playable specializations index.
        """

        api = '/data/wow/playable-specialization/index'

        query_params = {
            'namespace': 'static',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_playable_specialization(self, spec_id: int, **kwargs: Any) -> Dict:
        """
        This function will return the details of a specific playable specialization from the API.

        Requested API:
            /data/wow/playable-specialization/{specId}

        Args:
            spec_id: The ID of the playable specialization you want to retrieve.

        Returns:
            A dictionary of the playable specialization details.
        """

        api = f'/data/wow/playable-specialization/{spec_id}'

        query_params = {
            'namespace': 'static',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_playable_specialization_media(self, spec_id: int,  **kwargs: Any) -> Dict:
        """
        This function will return the media of a specific playable specialization from the API.

        Requested API:
            /data/wow/media/playable-specialization/{specId}

        Args:
            spec_id: The ID of the playable specialization you want to retrieve.

        Returns:
            A dictionary of the playable specialization media.
        """

        api = f'/data/wow/media/playable-specialization/{spec_id}'

        query_params = {
            'namespace': 'static',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)