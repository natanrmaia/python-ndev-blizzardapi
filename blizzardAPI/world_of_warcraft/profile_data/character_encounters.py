from typing import Optional, Dict, Any
from ...api import API

class CharacterEncounters(API):
    def __init__(self, client_id, client_secret):
        super().__init__(client_id, client_secret)

    def get_character_encounters_summary(self, realm_slug: str, character_name: str, **kwargs: Any) -> Dict:
        """
        Returns the character encounters summary from the API.

        Args:
            access_token: The access token of the API endpoint you want to use.
            realm_slug: The realm slug of the character you want to get the encounters summary from.
            character_name: The character name of the character you want to get the encounters summary from.

        Return:
            The character encounters summary.

        Raises:
            ValueError: If realm_slug is not provided.
            ValueError: If character_name is not provided.
        """

        if realm_slug is None:
            raise ValueError('realm_slug is required')

        if character_name is None:
            raise ValueError('character_name is required')

        api = f'/profile/wow/character/{realm_slug}/{character_name}/encounters'

        query_params = {
            'namespace': 'profile',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_character_dungeons(self, realm_slug: str, character_name: str, **kwargs: Any) -> Dict:
        """
        Returns the character dungeons from the API.

        Args:
            realm_slug: The realm slug of the character you want to get the dungeons from.
            character_name: The character name of the character you want to get the dungeons from.

        Return:
            The character dungeons.

        Raises:
            ValueError: If realm_slug is not provided.
            ValueError: If character_name is not provided.
        """

        if realm_slug is None:
            raise ValueError('realm_slug is required')

        if character_name is None:
            raise ValueError('character_name is required')

        api = f'/profile/wow/character/{realm_slug}/{character_name}/encounters/dungeons'

        query_params = {
            'namespace': 'profile',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_character_raids(self, realm_slug: str, character_name: str, **kwargs: Any) -> Dict:
        """
        Returns the character raids from the API.

        Args:
            realm_slug: The realm slug of the character you want to get the raids from.
            character_name: The character name of the character you want to get the raids from.

        Return:
            The character raids.

        Raises:
            ValueError: If realm_slug is not provided.
            ValueError: If character_name is not provided.
        """

        if realm_slug is None:
            raise ValueError('realm_slug is required')

        if character_name is None:
            raise ValueError('character_name is required')

        api = f'/profile/wow/character/{realm_slug}/{character_name}/encounters/raids'

        query_params = {
            'namespace': 'profile',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)