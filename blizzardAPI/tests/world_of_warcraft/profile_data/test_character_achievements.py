from blizzardAPI.world_of_warcraft.profile_data.character_achievements import CharacterAchievements

class TestCharacterAchievements:

    def test_get_character_achievements_summary(self, api_settings : dict):
        """
        This function tests the get_character_achievements_summary function from the CharacterAchievements class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'achievements'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        character_achievements = CharacterAchievements(api_settings['client_id'], api_settings['client_secret'])
        result = character_achievements.get_character_achievements_summary(api_settings['access_token'], api_settings['realm_slug'], api_settings['character_name'])

        if not isinstance(result, dict):
            return False
        else:
            assert 'achievements' in result

    def test_get_character_achievements_statistics(self, api_settings : dict):
        """
        This function tests the get_character_achievements_statistics function from the CharacterAchievements class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'categories'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        character_achievements = CharacterAchievements(api_settings['client_id'], api_settings['client_secret'])
        result = character_achievements.get_character_achievements_statistics(api_settings['access_token'], api_settings['realm_slug'], api_settings['character_name'])

        if not isinstance(result, dict):
            return False
        else:
            assert 'categories' in result