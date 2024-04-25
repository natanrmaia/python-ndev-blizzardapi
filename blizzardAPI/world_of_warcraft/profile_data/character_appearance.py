from typing import Optional, Dict, Any
from ...api import API

class CharacterAppearance(API):

    def __init__(self, client_id, client_secret):
        super().__init__(client_id, client_secret)

    def get_character_appearance_summary(self, realm_slug: str, character_name: str, **kwargs: Any) -> Dict:
        """
        Returns the character appearance summary from the API.
        Because this endpoint provides data about the current logged-in user's World of Warcraft account, it requires an access token with the wow.profile scope acquired via the Authorization Code Flow.

        Args:
            access_token: The access token of the API endpoint you want to use.
            realm_slug: The realm slug of the character you want to get the appearance summary from.
            character_name: The character name of the character you want to get the appearance summary from.

        Return:
            The character appearance summary.

        Raises:
            ValueError: If access_token is not provided.
            ValueError: If realm_slug is not provided.
            ValueError: If character_name is not provided.
        """

        if realm_slug is None:
            raise ValueError('realm_slug is required')

        if character_name is None:
            raise ValueError('character_name is required')

        api = f'/profile/wow/character/{realm_slug}/{character_name}/appearance'

        query_params = {
            'namespace': 'profile',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)