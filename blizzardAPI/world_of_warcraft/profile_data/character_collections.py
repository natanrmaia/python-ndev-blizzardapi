from typing import Optional, Dict, Any
from ...api import API

class CharacterCollections(API):
    def __init__(self, client_id, client_secret):
        super().__init__(client_id, client_secret)

    def get_character_collections_index(self, realm_slug: str, character_name: str, **kwargs: Any) -> Dict:
        """
        Returns an index of collection types for a character.

        Args:
            realm_slug: The realm slug of the character you want to get the collections index from.
            character_name: The character name of the character you want to get the collections index from.

        Return:
            The character collections index.

        Raises:
            ValueError: If realm_slug is not provided.
            ValueError: If character_name is not provided.
        """

        api = f'/profile/wow/character/{realm_slug}/{character_name}/collections'

        query_params = {
            'namespace': 'profile',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_character_mounts_collection_summary(self, realm_slug: str, character_name: str, **kwargs: Any) -> Dict:
        """
        Returns a summary of the mounts a character has obtained.

        Args:
            realm_slug: The realm slug of the character you want to get the mounts collection summary from.
            character_name: The character name of the character you want to get the mounts collection summary from.

        Return:
            The character mounts collection summary.

        Raises:
            ValueError: If realm_slug is not provided.
            ValueError: If character_name is not provided.
        """

        api = f'/profile/wow/character/{realm_slug}/{character_name}/collections/mounts'

        query_params = {
            'namespace': 'profile',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_character_pets_collection_summary(self, realm_slug: str, character_name: str, **kwargs: Any) -> Dict:
        """
        Returns a summary of the pets a character has obtained.

        Args:
            realm_slug: The realm slug of the character you want to get the pets collection summary from.
            character_name: The character name of the character you want to get the pets collection summary from.

        Return:
            The character pets collection summary.

        Raises:
            ValueError: If realm_slug is not provided.
            ValueError: If character_name is not provided.
        """

        api = f'/profile/wow/character/{realm_slug}/{character_name}/collections/pets'

        query_params = {
            'namespace': 'profile',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_character_toys_collection_summary(self, realm_slug: str, character_name: str, **kwargs: Any) -> Dict:
        """
        Returns a summary of the toys a character has obtained.

        Args:
            realm_slug: The realm slug of the character you want to get the toys collection summary from.
            character_name: The character name of the character you want to get the toys collection summary from.

        Return:
            The character toys collection summary.

        Raises:
            ValueError: If realm_slug is not provided.
            ValueError: If character_name is not provided.
        """

        api = f'/profile/wow/character/{realm_slug}/{character_name}/collections/toys'

        query_params = {
            'namespace': 'profile',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)

    def get_character_heirlooms_collection_summary(self, realm_slug: str, character_name: str, **kwargs: Any) -> Dict:
        """
        Returns a summary of the heirlooms a character has obtained.

        Args:
            realm_slug: The realm slug of the character you want to get the heirlooms collection summary from.
            character_name: The character name of the character you want to get the heirlooms collection summary from.

        Return:
            The character heirlooms collection summary.

        Raises:
            ValueError: If realm_slug is not provided.
            ValueError: If character_name is not provided.
        """

        api = f'/profile/wow/character/{realm_slug}/{character_name}/collections/heirlooms'

        query_params = {
            'namespace': 'profile',
        }

        query_params.update(kwargs)

        return super().get_api(api=api, query_params=query_params, **kwargs)
