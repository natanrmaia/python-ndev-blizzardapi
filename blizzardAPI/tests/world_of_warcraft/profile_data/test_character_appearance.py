from blizzardAPI.world_of_warcraft.profile_data.character_appearance import CharacterAppearance

class TestCharacterAppearance:

    def test_get_character_appearance_summary(self, api_settings : dict):
        """
        This function tests the get_character_appearance_summary function from the CharacterAppearance class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'character'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        character_appearance = CharacterAppearance(api_settings['client_id'], api_settings['client_secret'])
        result = character_appearance.get_character_appearance_summary(api_settings['realm_slug'], api_settings['character_name'])

        if not isinstance(result, dict):
            return False
        else:
            assert 'character' in result