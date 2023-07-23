from blizzardAPI.world_of_warcraft.profile_data.character_soulbinds import CharacterSoulbinds

class TestCharacterSoulbinds:

    def test_get_character_soulbinds(self, api_settings : dict):
        """
        This function tests the get_character_soulbinds function from the CharacterSoulbinds class.

        This function will test the following:
            - If the function returns a dict.
            - If the dict contains the key 'character'.

        Args:
            api_settings (dict): A dictionary containing the api args required for test.

        Returns:
            A boolean value indicating if the test passed.
        """

        character_soulbinds = CharacterSoulbinds(api_settings['client_id'], api_settings['client_secret'])
        result = character_soulbinds.get_character_soulbinds(api_settings['realm_slug'], api_settings['character_name'])

        if not isinstance(result, dict):
            return False
        else:
            assert 'character' in result
