from blizzardAPI.world_of_warcraft.profile_data.character_encounters import CharacterEncounters

class TestCharacterEncounters:

    def test_get_character_encounters_summary(self, api_settings : dict):
        """
        This function tests the get_character_encounters_summary function from the CharacterEncounters class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'character'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        character_encounters = CharacterEncounters(api_settings['client_id'], api_settings['client_secret'])
        result = character_encounters.get_character_encounters_summary(api_settings['realm_slug'], api_settings['character_name'])

        if not isinstance(result, dict):
            return False
        else:
            assert 'character' in result
    
    def test_get_character_dungeons(self, api_settings : dict):
        """
        This function tests the get_character_dungeons function from the CharacterEncounters class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'expansions'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        character_encounters = CharacterEncounters(api_settings['client_id'], api_settings['client_secret'])
        result = character_encounters.get_character_dungeons(api_settings['realm_slug'], api_settings['character_name'])

        if not isinstance(result, dict):
            return False
        else:
            assert 'expansions' in result

    def test_get_character_raids(self, api_settings : dict):
        """
        This function tests the get_character_raids function from the CharacterEncounters class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'expansions'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        character_encounters = CharacterEncounters(api_settings['client_id'], api_settings['client_secret'])
        result = character_encounters.get_character_raids(api_settings['realm_slug'], api_settings['character_name'])

        if not isinstance(result, dict):
            return False
        else:
            assert 'expansions' in result