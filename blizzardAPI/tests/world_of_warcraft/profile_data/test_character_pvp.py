from blizzardAPI.world_of_warcraft.profile_data.character_pvp import CharacterPvP

class TestCharacterPvp:

    def test_get_character_pvp_bracket_statistics(self, api_settings : dict):
        """
        This function tests the get_character_pvp_bracket_statistics function from the CharacterPvP class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'id'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        character_pvp = CharacterPvP(api_settings['client_id'], api_settings['client_secret'])
        result = character_pvp.get_character_pvp_bracket_statistics(api_settings['realm_slug'], api_settings['character_name'], api_settings['bracket'])

        if not isinstance(result, dict):
            return False
        else:
            assert 'id' in result

    def test_get_character_pvp_summary(self, api_settings : dict):
        """
        This function tests the get_character_pvp_summary function from the CharacterPvP class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'honor_level'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        character_pvp = CharacterPvP(api_settings['client_id'], api_settings['client_secret'])
        result = character_pvp.get_character_pvp_summary(api_settings['realm_slug'], api_settings['character_name'])

        if not isinstance(result, dict):
            return False
        else:
            assert 'honor_level' in result