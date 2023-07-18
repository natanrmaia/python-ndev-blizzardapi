from blizzardAPI.world_of_warcraft.profile_data.character_collections import CharacterCollections

class TestCharacterCollections:

    def test_get_character_collections_index(self, api_settings : dict):
        """
        This function tests the get_character_collections_index function from the CharacterCollections class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'mounts'.
            - If the dict contains the key 'pets'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        character_collections = CharacterCollections(api_settings['client_id'], api_settings['client_secret'])
        result = character_collections.get_character_collections_index(api_settings['realm_slug'], api_settings['character_name'])

        if not isinstance(result, dict):
            return False
        else:
            assert 'mounts' in result
            assert 'pets' in result

    def test_get_character_mounts_collection_summary(self, api_settings : dict):
        """
        This function tests the get_character_mounts_collection_summary function from the CharacterCollections class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'mounts'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        character_collections = CharacterCollections(api_settings['client_id'], api_settings['client_secret'])
        result = character_collections.get_character_mounts_collection_summary(api_settings['realm_slug'], api_settings['character_name'])

        if not isinstance(result, dict):
            return False
        else:
            assert 'mounts' in result

    def test_get_character_pets_collection_summary(self, api_settings : dict):
        """
        This function tests the get_character_pets_collection_summary function from the CharacterCollections class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'pets'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        character_collections = CharacterCollections(api_settings['client_id'], api_settings['client_secret'])
        result = character_collections.get_character_pets_collection_summary(api_settings['realm_slug'], api_settings['character_name'])

        if not isinstance(result, dict):
            return False
        else:
            assert 'pets' in result

    def test_get_character_toys_collection_index(self, api_settings : dict):
        """
        This function tests the get_character_toys_collection_index function from the CharacterCollections class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'toys'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        character_collections = CharacterCollections(api_settings['client_id'], api_settings['client_secret'])
        result = character_collections.get_character_toys_collection_summary(api_settings['realm_slug'], api_settings['character_name'])

        if not isinstance(result, dict):
            return False
        else:
            assert 'toys' in result

    def test_get_character_heirlooms_collection_index(self, api_settings : dict):
        """
        This function tests the get_character_heirlooms_collection_index function from the CharacterCollections class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'heirlooms'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        character_collections = CharacterCollections(api_settings['client_id'], api_settings['client_secret'])
        result = character_collections.get_character_heirlooms_collection_summary(api_settings['realm_slug'], api_settings['character_name'])

        if not isinstance(result, dict):
            return False
        else:
            assert 'heirlooms' in result