from typing import Optional, Dict, Any
from ...api import API

class CharacterStatistics(API):
    def __init__(self, client_id, client_secret):
        super().__init__(client_id, client_secret)

    def get_character_statistics_summary(self, realm_slug: str, character_name: str, **kwargs: Any) -> Dict:
        """
        Returns the character statistics summary from the API.

        Args:
            access_token: The access token of the API endpoint you want to use.
            realm_slug: The realm slug of the character you want to get the statistics summary from.
            character_name: The character name of the character you want to get the statistics summary from.

        Return:
            The character statistics summary.

        Raises:
            ValueError: If realm_slug is not provided.
            ValueError: If character_name is not provided.C
        """

        if realm_slug is None:
            raise ValueError('realm_slug is required')

        if character_name is None:
            raise ValueError('character_name is required')

        api = f'/profile/wow/character/{realm_slug}/{character_name}/statistics'

        query_params = {
            'namespace': 'profile',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)