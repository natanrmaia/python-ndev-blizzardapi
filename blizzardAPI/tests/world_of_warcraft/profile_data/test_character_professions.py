from blizzardAPI.world_of_warcraft.profile_data.character_professions import CharacterProfessions

class TestCharacterProfessions:

    def test_get_CharacterProfessions(self, api_settings : dict):
        """
        This function tests the get_character_professions_summary function from the CharacterProfessions class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'character'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        character_professions = CharacterProfessions(api_settings['client_id'], api_settings['client_secret'])
        result = character_professions.get_character_professions_summary(api_settings['realm_slug'], api_settings['character_name'])

        if not isinstance(result, dict):
            return False
        else:
            assert 'character' in result