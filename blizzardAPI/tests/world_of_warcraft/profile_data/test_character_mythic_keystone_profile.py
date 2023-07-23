from blizzardAPI.world_of_warcraft.profile_data.character_mythic_keystone_profile import CharacterMythicKeystoneProfile

class TestCharacterMythicKeystoneProfile:

    def test_get_character_mythic_keystone_profile_index(self, api_settings : dict):
        """
        This function tests the get_character_mythic_keystone_profile_index function from the CharacterMythicKeystoneProfile class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'current_period'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        character_mythic_keystone_profile = CharacterMythicKeystoneProfile(api_settings['client_id'], api_settings['client_secret'])
        result = character_mythic_keystone_profile.get_character_mythic_keystone_profile_index(api_settings['realm_slug'], api_settings['character_name'])

        if not isinstance(result, dict):
            return False
        else:
            assert 'current_period' in result

    def test_get_character_mythic_keystone_season_details(self, api_settings : dict):
        """
        This function tests the get_character_mythic_keystone_season_details function from the CharacterMythicKeystoneProfile class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'season'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        character_mythic_keystone_profile = CharacterMythicKeystoneProfile(api_settings['client_id'], api_settings['client_secret'])
        result = character_mythic_keystone_profile.get_character_mythic_keystone_season_details(api_settings['realm_slug'], api_settings['character_name'], api_settings['season_id'])

        if not isinstance(result, dict):
            return False
        else:
            assert 'season' in result