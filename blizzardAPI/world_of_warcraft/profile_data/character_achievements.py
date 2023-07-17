from typing import Optional, Dict, Any
from ...api import API

class CharacterAchievements(API):

    def __init__(self, client_id, client_secret):
        super().__init__(client_id, client_secret)

    def get_character_achievements_summary(self, access_token: Any, realm_slug: str, character_name: str, **kwargs: Any) -> Dict:
        """
        Returns the character achievements summary from the API.
        Because this endpoint provides data about a World of Warcraft character, it requires an access token with the wow.profile scope acquired via the Authorization Code Flow.

        Args:
            access_token: The access token of the API endpoint you want to use.
            realm_slug: The realm slug of the character you want to get the achievements summary from.
            character_name: The character name of the character you want to get the achievements summary from.

        Return:
            The character achievements summary.

        Raises:
            ValueError: If access_token is not provided.
            ValueError: If realm_slug is not provided.
            ValueError: If character_name is not provided.
        """

        api = f'/profile/wow/character/{realm_slug}/{character_name}/achievements'

        if access_token is None:
            raise ValueError('access_token is required')
        
        if realm_slug is None:
            raise ValueError('realm_slug is required')
        
        if character_name is None:
            raise ValueError('character_name is required')

        query_params = {
            'namespace': 'profile',
            'access_token': access_token,
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, kwargs=kwargs)
    
    def get_character_achievements_statistics(self, access_token: Any, realm_slug: str, character_name: str, **kwargs: Any) -> Dict:

        api = f'/profile/wow/character/{realm_slug}/{character_name}/achievements/statistics'

        if access_token is None:
            raise ValueError('access_token is required')
        
        if realm_slug is None:
            raise ValueError('realm_slug is required')
        
        if character_name is None:
            raise ValueError('character_name is required')

        query_params = {
            'namespace': 'profile',
            'access_token': access_token,
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, kwargs=kwargs)