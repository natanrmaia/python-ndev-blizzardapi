from typing import Dict, Optional
from ...api import API

class PlayableClass(API):

    def __init__(self, client_id, client_secret):
        super().__init__(client_id, client_secret)

    def get_playable_classes_index(self, region: Optional[str], locale: Optional[str]) -> Dict:
        """
        This function will return the index of playable classes from the API.

        Requested API:
            /data/wow/playable-class/index

        Args:
            region: The region of the API you want to access.
            locale: The locale of the API you want to access.

        Returns:
            A dictionary of the playable classes index.
        """

        api = '/data/wow/playable-class/index'

        query_params = {
            'namespace': 'static',
            'locale': locale,
        }

        return super().get_api(region, api, query_params)

    def get_playable_class(self, region: Optional[str], locale: Optional[str], class_id: int) -> Dict:
        """
        This function will return the details of a specific playable class from the API.

        Requested API:
            /data/wow/playable-class/{classId}

        Args:
            region: The region of the API you want to access.
            class_id: The ID of the playable class you want to retrieve.
            locale: The locale of the API you want to access.

        Returns:
            A dictionary of the playable class details.
        """

        api = f'/data/wow/playable-class/{class_id}'

        query_params = {
            'namespace': 'static',
            'locale': locale,
        }

        return super().get_api(region, api, query_params)

    def get_playable_class_media(self, region: Optional[str], locale: Optional[str], playable_class_id: int) -> Dict:
        """
        This function will return the media of a specific playable class from the API.

        Requested API:
            /data/wow/media/playable-class/{playableClassId}

        Args:
            region: The region of the API you want to access.
            playable_class_id: The ID of the playable class you want to retrieve.
            locale: The locale of the API you want to access.

        Returns:
            A dictionary of the playable class media.
        """

        api = f'/data/wow/media/playable-class/{playable_class_id}'

        query_params = {
            'namespace': 'static',
            'locale': locale,
        }

        return super().get_api(region, api, query_params)

    def get_pvp_talent_slots(self, region: Optional[str], locale: Optional[str], class_id: int) -> Dict:
        """
        This function will return the PvP talent slots of a specific playable class from the API.

        Requested API:
            /data/wow/playable-class/{classId}/pvp-talent-slots

        Args:
            region: The region of the API you want to access.
            class_id: The ID of the playable class you want to retrieve.
            locale: The locale of the API you want to access.

        Returns:
            A dictionary of the PvP talent slots of the playable class.
        """

        api = f'/data/wow/playable-class/{class_id}/pvp-talent-slots'

        query_params = {
            'namespace': 'static',
            'locale': locale,
        }

        return super().get_api(region, api, query_params)