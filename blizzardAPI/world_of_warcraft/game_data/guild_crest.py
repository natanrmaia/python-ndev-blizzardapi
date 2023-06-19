from typing import Optional, Dict
from ...api import API

class GuildCrest(API):

    def __init__(self, client_id, client_secret):
        super().__init__(client_id, client_secret)

    def get_guild_crest_components_index(self, region: Optional[str], locale: Optional[str]) -> Dict:
        """
        This function will return the index of guild crest media from the API.

        Requested API:
            /data/wow/guild-crest/index

        Args:
            region: The region of the API you want to access.
            locale: The locale of the API you want to access.

        Returns:
            A dictionary of the guild crest media index.
        """

        api = '/data/wow/guild-crest/index'

        query_params = {
            'namespace': 'static',
            'locale': locale,
        }

        return super().get_api(region, api, query_params)

    def get_guild_crest_border_media(self, region: Optional[str], locale: Optional[str], border_id: int) -> Dict:
        """
        This function retrieves information about a specific guild crest border from the API.

        Requested API:
            /data/wow/guild-crest/border/{border_id}

        Args:
            region: The region of the API you want to access.
            locale: The locale of the API you want to access.
            border_id: The ID of the guild crest border.

        Returns:
            A dictionary of the guild crest border.

        Raises:
            ValueError: If border_id is not provided.
        """

        if border_id is None:
            raise ValueError('border_id is required')

        api = '/data/wow/guild-crest/border/{}'

        query_params = {
            'namespace': 'static',
            'locale': locale,
        }

        return super().get_api(region, api.format(border_id), query_params)

    def get_guild_crest_emblem_media(self, region: Optional[str], locale: Optional[str], emblem_id: int) -> Dict:
        """
        This function retrieves information about a specific guild crest emblem from the API.

        Requested API:
            /data/wow/guild-crest/emblem/{emblem_id}

        Args:
            region: The region of the API you want to access.
            locale: The locale of the API you want to access.
            emblem_id: The ID of the guild crest emblem.

        Returns:
            A dictionary of the guild crest emblem.

        Raises:
            ValueError: If emblem_id is not provided.
        """

        if emblem_id is None:
            raise ValueError('emblem_id is required')

        api = '/data/wow/guild-crest/emblem/{}'

        query_params = {
            'namespace': 'static',
            'locale': locale,
        }

        return super().get_api(region, api.format(emblem_id), query_params)