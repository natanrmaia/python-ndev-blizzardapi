from blizzardAPI.world_of_warcraft.profile_data.character_quests import CharacterQuests

class TestCharacterQuests:

    def test_get_character_quests(self, api_settings : dict):
        """
        This function tests the get_character_quests function from the CharacterQuests class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'character'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        character_quests = CharacterQuests(api_settings['client_id'], api_settings['client_secret'])
        result = character_quests.get_character_quests(api_settings['realm_slug'], api_settings['character_name'])

        if not isinstance(result, dict):
            return False
        else:
            assert 'character' in result

    def test_get_character_completed_quests(self, api_settings : dict):
        """
        This function tests the get_character_completed_quests function from the CharacterQuests class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'character'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        character_quests = CharacterQuests(api_settings['client_id'], api_settings['client_secret'])
        result = character_quests.get_character_completed_quests(api_settings['realm_slug'], api_settings['character_name'])

        if not isinstance(result, dict):
            return False
        else:
            assert 'character' in result
