from typing import Optional, Dict, Any
from ...api import API

class CharacterMythicKeystoneProfile(API):
    def __init__(self, client_id, client_secret):
        super().__init__(client_id, client_secret)

    def get_character_mythic_keystone_profile_index(self, realm_slug: str, character_name: str, **kwargs: Any) -> Dict:
        """
        Returns the character mythic keystone profile index from the API.

        Args:
            realm_slug: The realm slug of the character you want to get the mythic keystone profile index from.
            character_name: The character name of the character you want to get the mythic keystone profile index from.

        Return:
            The character mythic keystone profile index.

        Raises:
            ValueError: If realm_slug is not provided.
            ValueError: If character_name is not provided.
        """

        if realm_slug is None:
            raise ValueError('realm_slug is required')

        if character_name is None:
            raise ValueError('character_name is required')

        api = f'/profile/wow/character/{realm_slug}/{character_name}/mythic-keystone-profile'

        query_params = {
            'namespace': 'profile',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_character_mythic_keystone_season_details(self, realm_slug: str, character_name: str, season_id: int, **kwargs: Any) -> Dict:
        """
        Returns the character mythic keystone season details from the API.

        Args:
            realm_slug: The realm slug of the character you want to get the mythic keystone season details from.
            character_name: The character name of the character you want to get the mythic keystone season details from.
            season_id: The season id of the character you want to get the mythic keystone season details from.

        Return:
            The character mythic keystone season details.

        Raises:
            ValueError: If realm_slug is not provided.
            ValueError: If character_name is not provided.
            ValueError: If season_id is not provided.
        """

        if realm_slug is None:
            raise ValueError('realm_slug is required')

        if character_name is None:
            raise ValueError('character_name is required')

        if season_id is None:
            raise ValueError('season_id is required')

        api = f'/profile/wow/character/{realm_slug}/{character_name}/mythic-keystone-profile/season/{season_id}'

        query_params = {
            'namespace': 'profile',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)
