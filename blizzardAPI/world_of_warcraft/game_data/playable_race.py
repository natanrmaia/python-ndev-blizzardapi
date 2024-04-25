from typing import Dict, Optional, Any
from ...api import API

class PlayableRace(API):

    def __init__(self, client_id, client_secret):
        super().__init__(client_id, client_secret)

    def get_playable_races_index(self, **kwargs: Any) -> Dict:
        """
        This function will return the index of playable races from the API.

        Requested API:
            /data/wow/playable-race/index

        Returns:
            A dictionary of the playable races index.
        """

        api = '/data/wow/playable-race/index'


        query_params = {
            'namespace': 'static',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_playable_race(self, playable_race_id: int, **kwargs: Any) -> Dict:
        """
        This function will return the details of a specific playable race from the API.

        Requested API:
            /data/wow/playable-race/{playableRaceId}

        Args:
            playable_race_id: The ID of the playable race you want to retrieve.

        Returns:
            A dictionary of the playable race details.
        """

        api = f'/data/wow/playable-race/{playable_race_id}'

        query_params = {
            'namespace': 'static',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)