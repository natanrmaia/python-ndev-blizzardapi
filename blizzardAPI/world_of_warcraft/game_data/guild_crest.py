from typing import Optional, Dict, Any
from ...api import API

class GuildCrest(API):

    def __init__(self, client_id, client_secret):
        super().__init__(client_id, client_secret)

    def get_guild_crest_components_index(self, **kwargs: Any) -> Dict:
        """
        This function will return the index of guild crest media from the API.

        Requested API:
            /data/wow/guild-crest/index

        Returns:
            A dictionary of the guild crest media index.
        """

        api = '/data/wow/guild-crest/index'

        query_params = {
            'namespace': 'static',
        }

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_guild_crest_border_media(self, border_id: int, **kwargs: Any) -> Dict:
        """
        This function retrieves information about a specific guild crest border from the API.

        Requested API:
           /data/wow/media/guild-crest/border/{border_id}

        Args:
            border_id: The ID of the guild crest border.

        Returns:
            A dictionary of the guild crest border.

        Raises:
            ValueError: If border_id is not provided.
        """

        if border_id is None:
            raise ValueError('border_id is required')

        api = f'/data/wow/media/guild-crest/border/{border_id}'

        query_params = {
            'namespace': 'static',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_guild_crest_emblem_media(self, emblem_id: int, **kwargs: Any) -> Dict:
        """
        This function retrieves information about a specific guild crest emblem from the API.

        Requested API:
            /data/wow/media/guild-crest/emblem/{emblem_id}

        Args:
            emblem_id: The ID of the guild crest emblem.

        Returns:
            A dictionary of the guild crest emblem.

        Raises:
            ValueError: If emblem_id is not provided.
        """

        if emblem_id is None:
            raise ValueError('emblem_id is required')

        api = f'/data/wow/media/guild-crest/emblem/{emblem_id}'

        query_params = {
            'namespace': 'static',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)