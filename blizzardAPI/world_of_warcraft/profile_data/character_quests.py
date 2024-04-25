from typing import Optional, Dict, Any
from ...api import API

class CharacterQuests(API):
    def __init__(self, client_id, client_secret):
        super().__init__(client_id, client_secret)

    def get_character_quests(self, realm_slug: str, character_name: str, **kwargs: Any) -> Dict:
        """
        Returns the character quests from the API.

        Args:
            access_token: The access token of the API endpoint you want to use.
            realm_slug: The realm slug of the character you want to get the quests from.
            character_name: The character name of the character you want to get the quests from.

        Return:
            The character quests.

        Raises:
            ValueError: If realm_slug is not provided.
            ValueError: If character_name is not provided.
        """

        if realm_slug is None:
            raise ValueError('realm_slug is required')

        if character_name is None:
            raise ValueError('character_name is required')

        api = f'/profile/wow/character/{realm_slug}/{character_name}/quests'

        query_params = {
            'namespace': 'profile',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_character_completed_quests(self, realm_slug: str, character_name: str, **kwargs: Any) -> Dict:
        """
        Returns the character completed quests from the API.

        Args:
            access_token: The access token of the API endpoint you want to use.
            realm_slug: The realm slug of the character you want to get the completed quests from.
            character_name: The character name of the character you want to get the completed quests from.

        Return:
            The character completed quests.

        Raises:
            ValueError: If realm_slug is not provided.
            ValueError: If character_name is not provided.
        """

        if realm_slug is None:
            raise ValueError('realm_slug is required')

        if character_name is None:
            raise ValueError('character_name is required')

        api = f'/profile/wow/character/{realm_slug}/{character_name}/quests/completed'

        query_params = {
            'namespace': 'profile',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)