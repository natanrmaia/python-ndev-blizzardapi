from typing import Dict, Optional
from ...api import API

class PlayableRace(API):

    def __init__(self, client_id, client_secret):
        super().__init__(client_id, client_secret)

    def get_playable_races_index(self, region: Optional[str], locale: Optional[str]) -> Dict:
        """
        This function will return the index of playable races from the API.

        Requested API:
            /data/wow/playable-race/index

        Args:
            region: The region of the API you want to access.
            locale: The locale of the API you want to access.

        Returns:
            A dictionary of the playable races index.
        """

        api = '/data/wow/playable-race/index'

        query_params = {
            'namespace': 'static',
            'locale': locale,
        }

        return super().get_api(region, api, query_params)

    def get_playable_race(self, region: Optional[str], locale: Optional[str], playable_race_id: int) -> Dict:
        """
        This function will return the details of a specific playable race from the API.

        Requested API:
            /data/wow/playable-race/{playableRaceId}

        Args:
            region: The region of the API you want to access.
            playable_race_id: The ID of the playable race you want to retrieve.
            locale: The locale of the API you want to access.

        Returns:
            A dictionary of the playable race details.
        """

        api = f'/data/wow/playable-race/{playable_race_id}'

        query_params = {
            'namespace': 'static',
            'locale': locale,
        }

        return super().get_api(region, api, query_params)