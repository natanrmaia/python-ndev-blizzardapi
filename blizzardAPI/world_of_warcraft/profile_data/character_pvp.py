from typing import Optional, Dict, Any
from ...api import API

class CharacterPvP(API):
    def __init__(self, client_id, client_secret):
        super().__init__(client_id, client_secret)

    def get_character_pvp_bracket_statistics(self, realm_slug: str, character_name: str, bracket: int, **kwargs: Any) -> Dict:
        """
        Returns the character pvp bracket statistics from the API.

        Args:
            access_token: The access token of the API endpoint you want to use.
            realm_slug: The realm slug of the character you want to get the pvp bracket statistics from.
            character_name: The character name of the character you want to get the pvp bracket statistics from.
            bracket: The pvp bracket you want to get the statistics from.

        Return:
            The character pvp bracket statistics.

        Raises:
            ValueError: If realm_slug is not provided.
            ValueError: If character_name is not provided.
            ValueError: If bracket is not provided.
        """

        if realm_slug is None:
            raise ValueError('realm_slug is required')

        if character_name is None:
            raise ValueError('character_name is required')

        if bracket is None:
            raise ValueError('bracket is required')

        api = f'/profile/wow/character/{realm_slug}/{character_name}/pvp-bracket/{bracket}'

        query_params = {
            'namespace': 'profile',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_character_pvp_summary(self, realm_slug: str, character_name: str, **kwargs: Any) -> Dict:
        """
        Returns the character pvp summary from the API.

        Args:
            access_token: The access token of the API endpoint you want to use.
            realm_slug: The realm slug of the character you want to get the pvp summary from.
            character_name: The character name of the character you want to get the pvp summary from.

        Return:
            The character pvp summary.

        Raises:
            ValueError: If realm_slug is not provided.
            ValueError: If character_name is not provided.
        """

        if realm_slug is None:
            raise ValueError('realm_slug is required')

        if character_name is None:
            raise ValueError('character_name is required')

        api = f'/profile/wow/character/{realm_slug}/{character_name}/pvp-summary'

        query_params = {
            'namespace': 'profile',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)