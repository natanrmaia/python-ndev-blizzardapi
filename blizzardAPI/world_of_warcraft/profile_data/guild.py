from typing import Optional, Dict, Any
from ...api import API

class Guild(API):
    def __init__(self, client_id, client_secret):
        super().__init__(client_id, client_secret)

    def get_guild(self, realm_slug: str, guild_slug: str, **kwargs: Any) -> Dict:
        """
        Returns the guild from the API.

        Args:
            realm_slug: The realm slug of the guild you want to get.
            guild_slug: The guild name of the guild you want to get.

        Return:
            The guild.

        Raises:
            ValueError: If realm_slug is not provided.
            ValueError: If guild_slug is not provided.
        """

        if realm_slug is None:
            raise ValueError('realm_slug is required')

        if guild_slug is None:
            raise ValueError('guild_slug is required')

        api = f'/data/wow/guild/{realm_slug}/{guild_slug}'

        query_params = {
            'namespace': 'profile',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_guild_activity(self, realm_slug: str, guild_slug: str, **kwargs: Any) -> Dict:
        """
        Returns the guild activity from the API.

        Args:
            realm_slug: The realm slug of the guild you want to get the activity from.
            guild_slug: The guild name of the guild you want to get the activity from.

        Return:
            The guild activity.

        Raises:
            ValueError: If realm_slug is not provided.
            ValueError: If guild_slug is not provided.
        """

        if realm_slug is None:
            raise ValueError('realm_slug is required')

        if guild_slug is None:
            raise ValueError('guild_slug is required')

        api = f'/data/wow/guild/{realm_slug}/{guild_slug}/activity'

        query_params = {
            'namespace': 'profile',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_guild_achievements(self, realm_slug: str, guild_slug: str, **kwargs: Any) -> Dict:
        """
        Returns the guild achievements from the API.

        Args:
            realm_slug: The realm slug of the guild you want to get the achievements from.
            guild_slug: The guild name of the guild you want to get the achievements from.

        Return:
            The guild achievements.

        Raises:
            ValueError: If realm_slug is not provided.
            ValueError: If guild_slug is not provided.
        """

        if realm_slug is None:
            raise ValueError('realm_slug is required')

        if guild_slug is None:
            raise ValueError('guild_slug is required')

        api = f'/data/wow/guild/{realm_slug}/{guild_slug}/achievements'

        query_params = {
            'namespace': 'profile',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_guild_roster(self, realm_slug: str, guild_slug: str, **kwargs: Any) -> Dict:
        """
        Returns the guild roster from the API.

        Args:
            realm_slug: The realm slug of the guild you want to get the roster from.
            guild_slug: The guild name of the guild you want to get the roster from.

        Return:
            The guild roster.

        Raises:
            ValueError: If realm_slug is not provided.
            ValueError: If guild_slug is not provided.
        """

        if realm_slug is None:
            raise ValueError('realm_slug is required')

        if guild_slug is None:
            raise ValueError('guild_slug is required')

        api = f'/data/wow/guild/{realm_slug}/{guild_slug}/roster'

        query_params = {
            'namespace': 'profile',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)
