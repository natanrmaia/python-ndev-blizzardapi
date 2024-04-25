from typing import Dict, Optional, Any
from ...api import API

class PlayableClass(API):

    def __init__(self, client_id, client_secret):
        super().__init__(client_id, client_secret)

    def get_playable_classes_index(self, **kwargs: Any) -> Dict:
        """
        This function will return the index of playable classes from the API.

        Requested API:
            /data/wow/playable-class/index

        Returns:
            A dictionary of the playable classes index.
        """

        api = '/data/wow/playable-class/index'

        query_params = {
            'namespace': 'static',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_playable_class(self, class_id: int, **kwargs: Any) -> Dict:
        """
        This function will return the details of a specific playable class from the API.

        Requested API:
            /data/wow/playable-class/{classId}

        Args:
            class_id: The ID of the playable class you want to retrieve.

        Returns:
            A dictionary of the playable class details.
        """

        api = f'/data/wow/playable-class/{class_id}'

        query_params = {
            'namespace': 'static',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_playable_class_media(self, playable_class_id: int, **kwargs: Any) -> Dict:
        """
        This function will return the media of a specific playable class from the API.

        Requested API:
            /data/wow/media/playable-class/{playableClassId}

        Args:
            playable_class_id: The ID of the playable class you want to retrieve.

        Returns:
            A dictionary of the playable class media.
        """

        api = f'/data/wow/media/playable-class/{playable_class_id}'

        query_params = {
            'namespace': 'static',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_pvp_talent_slots(self, class_id: int, **kwargs: Any) -> Dict:
        """
        This function will return the PvP talent slots of a specific playable class from the API.

        Requested API:
            /data/wow/playable-class/{classId}/pvp-talent-slots

        Args:
            class_id: The ID of the playable class you want to retrieve.

        Returns:
            A dictionary of the PvP talent slots of the playable class.
        """

        api = f'/data/wow/playable-class/{class_id}/pvp-talent-slots'

        query_params = {
            'namespace': 'static',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)