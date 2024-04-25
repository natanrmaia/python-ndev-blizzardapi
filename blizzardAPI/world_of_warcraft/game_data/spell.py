from typing import Optional, Dict, Any
from ...api import API


class Spell(API):

    def __init__(self, client_id, client_secret):
        super().__init__(client_id, client_secret)

    def get_spell(self, spell_id: int, **kwargs: Any) -> Dict:
        """
        This function retrieves information about a specific spell from the API.

        Requested API:
            /data/wow/spell/{spellId}

        Args:
            spell_id: The ID of the spell.

        Returns:
            A dictionary of the spell.

        Raises:
            ValueError: If spell_id is not provided.
        """

        if spell_id is None:
            raise ValueError('spell_id is required')

        api = f'/data/wow/spell/{spell_id}'

        query_params = {
            'namespace': 'static',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_spell_media(self, spell_id: int, **kwargs: Any) -> Dict:
        """
        This function retrieves media information about a specific spell from the API.

        Requested API:
            /data/wow/media/spell/{spellId}

        Args:
            spell_id: The ID of the spell.

        Returns:
            A dictionary of the spell media.

        Raises:
            ValueError: If spell_id is not provided.
        """

        if spell_id is None:
            raise ValueError('spell_id is required')

        api = f'/data/wow/media/spell/{spell_id}'

        query_params = {
            'namespace': 'static',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_spell_search(self, **kwargs: Any) -> Dict:
        """
        This function searches for spells from the API.

        Requested API:
            /data/wow/search/spell

        Args:
            search: The search query.

        Returns:
            A dictionary of the search results.
        """

        api = '/data/wow/search/spell'

        query_params = {
            'namespace': 'static',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)