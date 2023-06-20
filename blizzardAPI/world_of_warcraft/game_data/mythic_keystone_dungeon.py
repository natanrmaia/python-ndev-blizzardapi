from typing import Dict, Optional
from ...api import API

class MythicKeystoneDungeon(API):
    def get_mythic_keystone_dungeons_index(self, region: Optional[str], locale: Optional[str]) -> Dict:
        """
        This function will return the index of mythic keystone dungeons from the API.

        Requested API:
            /data/wow/mythic-keystone/dungeon/index

        Args:
            region: The region of the API you want to access.
            locale: The locale of the API you want to access.

        Returns:
            A dictionary of the mythic keystone dungeons index.
        """

        api = '/data/wow/mythic-keystone/dungeon/index'

        query_params = {
            'namespace': 'dynamic',
            'locale': locale,
        }

        return super().get_api(region, api, query_params)

    def get_mythic_keystone_dungeon(self, region: Optional[str], locale: Optional[str], dungeon_id: int) -> Dict:
        """
        This function will return the details of a specific mythic keystone dungeon from the API.

        Requested API:
            /data/wow/mythic-keystone/dungeon/{dungeonId}

        Args:
            region: The region of the API you want to access.
            dungeon_id: The ID of the mythic keystone dungeon you want to retrieve.
            locale: The locale of the API you want to access.

        Returns:
            A dictionary of the mythic keystone dungeon details.
        """

        api = f'/data/wow/mythic-keystone/dungeon/{dungeon_id}'

        query_params = {
            'namespace': 'dynamic',
            'locale': locale,
        }

        return super().get_api(region, api, query_params)

    def get_mythic_keystone_index(self, region: Optional[str], locale: Optional[str]) -> Dict:
        """
        This function will return the index of mythic keystones from the API.

        Requested API:
            /data/wow/mythic-keystone/index

        Args:
            region: The region of the API you want to access.
            locale: The locale of the API you want to access.

        Returns:
            A dictionary of the mythic keystones index.
        """

        api = '/data/wow/mythic-keystone/index'

        query_params = {
            'namespace': 'dynamic',
            'locale': locale,
        }

        return super().get_api(region, api, query_params)

    def get_mythic_keystone_periods_index(self, region: Optional[str], locale: Optional[str]) -> Dict:
        """
        This function will return the index of mythic keystone periods from the API.

        Requested API:
            /data/wow/mythic-keystone/period/index

        Args:
            region: The region of the API you want to access.
            locale: The locale of the API you want to access.

        Returns:
            A dictionary of the mythic keystone periods index.
        """

        api = '/data/wow/mythic-keystone/period/index'

        query_params = {
            'namespace': 'dynamic',
            'locale': locale,
        }

        return super().get_api(region, api, query_params)

    def get_mythic_keystone_period(self, region: Optional[str], locale: Optional[str], period_id: int) -> Dict:
        """
        This function will return the details of a specific mythic keystone period from the API.

        Requested API:
            /data/wow/mythic-keystone/period/{periodId}

        Args:
            region: The region of the API you want to access.
            period_id: The ID of the mythic keystone period you want to retrieve.
            locale: The locale of the API you want to access.

        Returns:
            A dictionary of the mythic keystone period details.
        """

        api = f'/data/wow/mythic-keystone/period/{period_id}'

        query_params = {
            'namespace': 'dynamic',
            'locale': locale,
        }

        return super().get_api(region, api, query_params)

    def get_mythic_keystone_seasons_index(self, region: Optional[str], locale: Optional[str]) -> Dict:
        """
        This function will return the index of mythic keystone seasons from the API.

        Requested API:
            /data/wow/mythic-keystone/season/index

        Args:
            region: The region of the API you want to access.
            locale: The locale of the API you want to access.

        Returns:
            A dictionary of the mythic keystone seasons index.
        """

        api = '/data/wow/mythic-keystone/season/index'

        query_params = {
            'namespace': 'dynamic',
            'locale': locale,
        }

        return super().get_api(region, api, query_params)

    def get_mythic_keystone_season(self, region: Optional[str], locale: Optional[str], season_id: int) -> Dict:
        """
        This function will return the details of a specific mythic keystone season from the API.

        Requested API:
            /data/wow/mythic-keystone/season/{seasonId}

        Args:
            region: The region of the API you want to access.
            season_id: The ID of the mythic keystone season you want to retrieve.
            locale: The locale of the API you want to access.

        Returns:
            A dictionary of the mythic keystone season details.
        """

        api = f'/data/wow/mythic-keystone/season/{season_id}'

        query_params = {
            'namespace': 'dynamic',
            'locale': locale,
        }

        return super().get_api(region, api, query_params)

# END: 1a2b3c4d5e6f