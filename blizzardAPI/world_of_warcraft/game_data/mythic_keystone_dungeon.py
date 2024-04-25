from typing import Dict, Optional, Any
from ...api import API

class MythicKeystoneDungeon(API):

    def __init__(self, client_id, client_secret):
        super().__init__(client_id, client_secret)

    def get_mythic_keystone_dungeons_index(self, **kwargs: Any) -> Dict:
        """
        This function will return the index of mythic keystone dungeons from the API.

        Requested API:
            /data/wow/mythic-keystone/dungeon/index

        Returns:
            A dictionary of the mythic keystone dungeons index.
        """

        api = '/data/wow/mythic-keystone/dungeon/index'

        query_params = {
            'namespace': 'dynamic',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_mythic_keystone_dungeon(self, dungeon_id: int,  **kwargs: Any) -> Dict:
        """
        This function will return the details of a specific mythic keystone dungeon from the API.

        Requested API:
            /data/wow/mythic-keystone/dungeon/{dungeonId}

        Args:
            dungeon_id: The ID of the mythic keystone dungeon you want to retrieve.

        Returns:
            A dictionary of the mythic keystone dungeon details.
        """

        api = f'/data/wow/mythic-keystone/dungeon/{dungeon_id}'

        query_params = {
            'namespace': 'dynamic',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_mythic_keystone_index(self, **kwargs: Any) -> Dict:
        """
        This function will return the index of mythic keystones from the API.

        Requested API:
            /data/wow/mythic-keystone/index

        Returns:
            A dictionary of the mythic keystones index.
        """

        api = '/data/wow/mythic-keystone/index'

        query_params = {
            'namespace': 'dynamic',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_mythic_keystone_period_index(self, **kwargs: Any) -> Dict:
        """
        This function will return the index of mythic keystone periods from the API.

        Requested API:
            /data/wow/mythic-keystone/period/index

        Returns:
            A dictionary of the mythic keystone periods index.
        """

        api = '/data/wow/mythic-keystone/period/index'

        query_params = {
            'namespace': 'dynamic',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_mythic_keystone_period(self, period_id: int, **kwargs: Any) -> Dict:
        """
        This function will return the details of a specific mythic keystone period from the API.

        Requested API:
            /data/wow/mythic-keystone/period/{periodId}

        Args:
            period_id: The ID of the mythic keystone period you want to retrieve.

        Returns:
            A dictionary of the mythic keystone period details.
        """

        api = f'/data/wow/mythic-keystone/period/{period_id}'

        query_params = {
            'namespace': 'dynamic',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_mythic_keystone_seasons_index(self, **kwargs: Any) -> Dict:
        """
        This function will return the index of mythic keystone seasons from the API.

        Requested API:
            /data/wow/mythic-keystone/season/index

        Returns:
            A dictionary of the mythic keystone seasons index.
        """

        api = '/data/wow/mythic-keystone/season/index'

        query_params = {
            'namespace': 'dynamic',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_mythic_keystone_season(self, season_id: int, **kwargs: Any) -> Dict:
        """
        This function will return the details of a specific mythic keystone season from the API.

        Requested API:
            /data/wow/mythic-keystone/season/{seasonId}

        Args:
            season_id: The ID of the mythic keystone season you want to retrieve.

        Returns:
            A dictionary of the mythic keystone season details.
        """

        api = f'/data/wow/mythic-keystone/season/{season_id}'

        query_params = {
            'namespace': 'dynamic',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)