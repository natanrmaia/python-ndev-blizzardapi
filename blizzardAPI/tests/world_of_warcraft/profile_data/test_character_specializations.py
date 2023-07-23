from blizzardAPI.world_of_warcraft.profile_data.character_specializations import CharacterSpecializations

class TestCharacterSpecializations:

    def test_get_character_specializations_summary(self, api_settings : dict):
        """
        This function tests the get_character_specializations_summary function from the CharacterSpecializations class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'specializations'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        character_specializations = CharacterSpecializations(api_settings['client_id'], api_settings['client_secret'])
        result = character_specializations.get_character_specializations_summary(api_settings['realm_slug'], api_settings['character_name'])

        if not isinstance(result, dict):
            return False
        else:
            assert 'specializations' in result