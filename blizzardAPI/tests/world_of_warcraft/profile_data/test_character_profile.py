from blizzardAPI.world_of_warcraft.profile_data.character_profile import CharacterProfile

class TestCharacterProfile:

    def test_get_character_profile_summary(self, api_settings : dict):
        """
        This function tests the get_character_profile_summary function from the CharacterProfile class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'id'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        character_profile = CharacterProfile(api_settings['client_id'], api_settings['client_secret'])
        result = character_profile.get_character_profile_summary(api_settings['realm_slug'], api_settings['character_name'])

        if not isinstance(result, dict):
            return False
        else:
            assert 'id' in result

    def test_get_character_profile_status(self, api_settings : dict):
        """
        This function tests the get_character_profile_status function from the CharacterProfile class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'id'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        character_profile = CharacterProfile(api_settings['client_id'], api_settings['client_secret'])
        result = character_profile.get_character_profile_status(api_settings['realm_slug'], api_settings['character_name'])

        if not isinstance(result, dict):
            return False
        else:
            assert 'id' in result